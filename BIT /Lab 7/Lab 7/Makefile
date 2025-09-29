all: calc

calc: lex.yy.c calcgrammar.tab.c tree.o ir.o
	gcc -o calc lex.yy.c calcgrammar.tab.c tree.o ir.o -lm

calcgrammar.tab.c calcgrammar.tab.h: calcgrammar.y
	bison -d calcgrammar.y

lex.yy.c: calcgrammar.l calcgrammar.tab.h
	flex calcgrammar.l

tree.o: tree.c parsetree.h
	gcc -c tree.c

ir.o: ir.c ir.h parsetree.h
	gcc -c ir.c

clean:
	rm -f calc lex.yy.c calcgrammar.tab.* *.o