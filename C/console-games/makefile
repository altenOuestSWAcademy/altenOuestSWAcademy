IDIR =../Header
CC=gcc
CFLAGS=-I.
DEPS = common.h pong.h snake.h space_invaders.h 
ODIR=../obj

_OBJ = main.o 
OBJ = main.o

%.o: %.c $(DEPS)
	$(CC) -c -o $@ $< $(CFLAGS)
	
main: $(OBJ) 
	$(CC) -o main main.o 

clean:
	rm -f *.o *.exe