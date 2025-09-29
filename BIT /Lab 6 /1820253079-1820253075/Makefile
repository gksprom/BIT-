CC = gcc
CFLAGS = -Wall -g
LEX = flex
YACC = bison

all: parser

parser: calcgrammar.tab.o lex.yy.o tree.o
	$(CC) $(CFLAGS) $^ -o $@ -lm

calcgrammar.tab.o: calcgrammar.tab.c parsetree.h
	$(CC) $(CFLAGS) -c $<

lex.yy.o: lex.yy.c calcgrammar.tab.h
	$(CC) $(CFLAGS) -c $<

tree.o: tree.c parsetree.h
	$(CC) $(CFLAGS) -c $<

calcgrammar.tab.c calcgrammar.tab.h: calcgrammar.y
	$(YACC) -d $<

lex.yy.c: calcgrammar.l
	$(LEX) $<

clean:
	rm -f *.o parser calcgrammar.tab.* lex.yy.*

.PHONY: all clean