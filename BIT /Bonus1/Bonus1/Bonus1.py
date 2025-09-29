

import re
from collections import defaultdict, deque

def read_automaton(file_path):
    with open(file_path, 'r') as f:
        content = f.read()

    headers = {}
    for line in content.splitlines():
        m = re.match(r"^(\w+):\s*(.*)$", line.strip())
        if m:
            headers[m.group(1)] = m.group(2)

    if not all(k in headers for k in ["States", "Alphabet", "Start", "Final"]):
        raise ValueError("Missing required sections in the file.")

    states = headers["States"].split()
    alphabet = headers["Alphabet"].split()
    start = headers["Start"].strip()
    finals = headers["Final"].split()

    parts = re.split(r"Transitions:\s*", content, flags=re.IGNORECASE)
    if len(parts) < 2:
        raise ValueError("Transitions section not found.")
    
    transitions = defaultdict(list)
    for line in parts[1].splitlines():
        line = line.strip()
        if not line:
            continue
        parts = line.split()
        src, symbol = parts[0], parts[1]
        dests = parts[2:] if parts[2:] != ["-"] else []
        transitions[(src, symbol)].extend(dests)

    return states, alphabet, start, finals, transitions

def detect_type(states, alphabet, transitions):
    has_epsilon = any(symbol == 'ε' for (_, symbol) in transitions)
    for (state, symbol), dests in transitions.items():
        if len(dests) > 1:
            return "E-NFA" if has_epsilon else "NFA"
    if has_epsilon:
        return "E-NFA"
    return "DFA"

def epsilon_closure(state, transitions):
    stack = [state]
    closure = set([state])
    while stack:
        curr = stack.pop()
        for next_state in transitions.get((curr, 'ε'), []):
            if next_state not in closure:
                closure.add(next_state)
                stack.append(next_state)
    return closure

def e_nfa_to_nfa(states, alphabet, start, finals, transitions):
    new_trans = defaultdict(set)
    new_finals = set()
    for state in states:
        e_closure = epsilon_closure(state, transitions)
        for symbol in alphabet:
            dest = set()
            for ec_state in e_closure:
                dest.update(transitions.get((ec_state, symbol), []))
            new_dest = set()
            for d in dest:
                new_dest.update(epsilon_closure(d, transitions))
            if new_dest:
                new_trans[(state, symbol)].update(new_dest)
        if any(s in finals for s in e_closure):
            new_finals.add(state)
    return states, alphabet, start, list(new_finals), new_trans

def nfa_to_dfa(states, alphabet, start, finals, transitions):
    start_set = frozenset([start])
    dfa_states = {start_set}
    queue = deque([start_set])
    dfa_trans = {}
    dfa_finals = set()

    while queue:
        current = queue.popleft()
        for symbol in alphabet:
            dest = set()
            for s in current:
                dest.update(transitions.get((s, symbol), []))
            dest_set = frozenset(dest)
            if dest:
                dfa_trans[(current, symbol)] = dest_set
                if dest_set not in dfa_states:
                    dfa_states.add(dest_set)
                    queue.append(dest_set)

    for state in dfa_states:
        if any(s in finals for s in state):
            dfa_finals.add(state)

    state_names = {state: f"S{i}" for i, state in enumerate(sorted(dfa_states, key=lambda x: sorted(x)))}
    renamed_trans = {}
    for (src, sym), dest in dfa_trans.items():
        renamed_trans[(state_names[src], sym)] = state_names[dest]
    renamed_finals = {state_names[s] for s in dfa_finals}
    start_state = state_names[start_set]
    all_states = set(state_names.values())
    return all_states, alphabet, start_state, renamed_finals, renamed_trans

def minimize_dfa(states, alphabet, start, finals, transitions):
    non_finals = states - finals
    partition = [finals, non_finals]
    changed = True
    while changed:
        changed = False
        new_partition = []
        for group in partition:
            split = defaultdict(set)
            for state in group:
                key = tuple(next(
                    (i for i, g in enumerate(partition) if transitions.get((state, sym), None) in g),
                    -1
                ) for sym in alphabet)
                split[key].add(state)
            new_partition.extend(split.values())
            if len(split) > 1:
                changed = True
        partition = new_partition

    new_states = {"P"+str(i): group for i, group in enumerate(partition)}
    state_map = {}
    for name, group in new_states.items():
        for state in group:
            state_map[state] = name

    new_trans = {}
    for state in states:
        for sym in alphabet:
            dest = transitions.get((state, sym))
            if dest:
                new_trans[(state_map[state], sym)] = state_map[dest]

    new_finals = {state_map[s] for s in finals}
    new_states_set = set(state_map.values())
    new_start = state_map[start]
    return new_states_set, alphabet, new_start, new_finals, new_trans

def print_dfa(states, alphabet, start, finals, transitions):
    print("Minimized DFA:")
    print("States:", " ".join(sorted(states)))
    print("Alphabet:", " ".join(alphabet))
    print("Start:", start)
    print("Final:", " ".join(sorted(finals)))
    print("Transitions:")
    for (src, sym), dest in sorted(transitions.items()):
        print(f"{src} {sym} {dest}")

if __name__ == "__main__":
    path = input("Enter input file name (e.g., input_dfa.txt): ").strip()
    try:
        states, alphabet, start, finals, transitions = read_automaton(path)
        auto_type = detect_type(states, alphabet, transitions)
        print("Detected type:", auto_type)

        if auto_type == "E-NFA":
            states, alphabet, start, finals, transitions = e_nfa_to_nfa(states, alphabet, start, finals, transitions)
            auto_type = "NFA"

        if auto_type == "NFA":
            states, alphabet, start, finals, transitions = nfa_to_dfa(states, alphabet, start, finals, transitions)
            auto_type = "DFA"

        if auto_type != "DFA":
            raise ValueError("Conversion to DFA failed.")

        states, alphabet, start, finals, transitions = minimize_dfa(states, alphabet, start, finals, transitions)
        print_dfa(states, alphabet, start, finals, transitions)

    except Exception as e:
        print(f"Error: {e}")
