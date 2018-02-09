CC = gcc
#FLAGS = -WALL -g3
FLAGS = -g3
#OBJECTS = main.o files.o lvds.0
OBJECTS = tests.o CAENVMEDemoVme.o console.o
INCLUDES = CAENVMElib.h CAENVMEtypes.h CAENVMEoslib.h console.h
DEPLIBS =       -l CAENVME -l curses

%.o: %.c
	$(CC) $(FLAGS) -c -o $@ $<

tests: $(OBJECTS)
	$(CC) $(FLAGS) $(OBJECTS) -o $@ $(DEPLIBS)

clean:
	rm -rf *.o tests
