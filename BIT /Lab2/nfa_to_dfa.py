import re
import sys
import os
from collections import defaultdict


STUDENT_IDS = "1820253079, 1820253050"

def read_nfa(file_path):
   
    with open(file_path, 'r') as f:
        content = f.read()

    headers = {}
    for line in content.splitlines():
        line = line.strip()
        m = re.match(r"^(\w+):\s*(.*)$", line)
        if m:
            key, value = m.group(1), m.group(2)
            headers[key] = value

    states = headers.get("States", "").split()
    alphabet = headers.get("Alphabet", "").split()
    start_state = headers.get("Start", "").strip()
    final_states = headers.get("Final", "").split()

  
    parts = re.split(r"Transitions:\s*", content, flags=re.IGNORECASE)
    if len(parts) < 2:
        raise ValueError("Transitions section not found in the input file.")

    
    transitions = {}
    trans_lines = parts[1].splitlines()
    for line in trans_lines:
        line = line.strip()
        if not line:
            continue
        tokens = line.split()
       
        if len(tokens) < 2:
            continue
        current, symbol = tokens[0], tokens[1]
        dest_tokens = tokens[2:] if len(tokens) > 2 else []
       
        if dest_tokens == ["-"]:
            dest_states = tuple()
        else:
            dest_states = tuple(dest_tokens)
        transitions[(current, symbol)] = dest_states

    return states, alphabet, start_state, final_states, transitions

def convert_nfa_to_dfa(nfa):
    
    nfa_states, alphabet, nfa_start, nfa_finals, nfa_transitions = nfa

 
    dfa_start = tuple(sorted([nfa_start]))
    dfa_states = [dfa_start]
    dfa_transitions = {}
    dfa_finals = []
    queue = [dfa_start]
    processed = set()

    while queue:
        current = queue.pop(0)
        if current in processed:
            continue
        processed.add(current)
        for symbol in alphabet:
            new_state_set = set()
            
            for state in current:
                key = (state, symbol)
                if key in nfa_transitions:
                    new_state_set.update(nfa_transitions[key])
            if new_state_set:
                new_state = tuple(sorted(new_state_set))
            else:
                new_state = None  
            dfa_transitions[(current, symbol)] = new_state
            if new_state is not None and new_state not in dfa_states:
                dfa_states.append(new_state)
                queue.append(new_state)

    
    for state in dfa_states:
        if any(s in nfa_finals for s in state):
            dfa_finals.append(state)

    return dfa_states, alphabet, dfa_start, dfa_finals, dfa_transitions

def write_dfa(dfa, input_file):
   
    dfa_states, alphabet, dfa_start, dfa_finals, dfa_transitions = dfa
    match = re.search(r'\d+', os.path.basename(input_file))
    if match:
        number = match.group()
        output_file = f"DFA_output_{number}"

    with open(output_file, "w") as f:
        f.write(f"# Student IDs: {STUDENT_IDS}\n\n")
     
        def state_to_str(state):
            return "{" + ",".join(state) + "}"
        states_str = " ".join(state_to_str(state) for state in dfa_states)
        f.write(f"States: {states_str}\n")
        f.write(f"Alphabet: {' '.join(alphabet)}\n")
        f.write(f"Start: {state_to_str(dfa_start)}\n")
        finals_str = " ".join(state_to_str(state) for state in dfa_finals)
        f.write(f"Final: {finals_str}\n\n")
        f.write("Transitions:\n")
        
        transitions_list = []
        for (state, symbol), dest in dfa_transitions.items():
            if dest is not None:
                transitions_list.append((state_to_str(state), symbol, state_to_str(dest)))
        transitions_list.sort()
        for trans in transitions_list:
            f.write(f"{trans[0]} {trans[1]} {trans[2]}\n")
    print(f"DFA written to {output_file}")


if __name__ == "__main__":
   
    if len(sys.argv) < 2:
        print("Usage: python3 program_name input1.txt")
        sys.exit(1)
    input_file = sys.argv[1]

    
    nfa = read_nfa(input_file)
    dfa = convert_nfa_to_dfa(nfa)
    write_dfa(dfa, input_file)

