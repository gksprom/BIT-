calcgrammar: calcgrammar.tab.o lex.yy.o
	gcc -o calcgrammar calcgrammar.tab.o lex.yy.o -ll -lm

calcgrammar.tab.c calcgrammar.tab.h: calcgrammar.y
	bison -d calcgrammar.y

lex.yy.c: calcgrammar.l calcgrammar.tab.h
	flex calcgrammar.l

calcgrammar.tab.o: calcgrammar.tab.c
	gcc -c calcgrammar.tab.c

lex.yy.o: lex.yy.c
	gcc -c lex.yy.c

clean:
	rm -f calcgrammar calcgrammar.tab.* lex.yy.* *.o
