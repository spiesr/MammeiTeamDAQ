########################################################################
#                                                                      
#              --- CAEN SpA - Computing Division ---                   
#                                                                      
#   CAENVMElib Software Project                                        
#                                                                      
#   Created  :  March 2004      (Rel. 1.0)                                             
#                                                                      
#   Auth: S. Coluccini                                                 
#                                                                      
########################################################################

EXE	=	frontend

CC	=	gcc

COPTS	=	-fPIC -DLINUX -Wall 
#COPTS	=	-g -fPIC -DLINUX -Wall 

FLAGS	=	-Wall -s
#FLAGS	=	-Wall

DEPLIBS	=       -l CAENVME -l curses

LIBS	=	

INCLUDEDIR =	-I.

OBJS	=	frontend.o files.o lvds.o CAENVMEDemoVme.o console.o qadc.o V812.o V895.o

INCLUDES =	CAENVMElib.h CAENVMEtypes.h CAENVMEoslib.h console.h qadc.h V812.h V895.h

#########################################################################

all	:	$(EXE)

clean	:
		/bin/rm -f $(OBJS) $(EXE)

$(EXE)	:	$(OBJS)
		/bin/rm -f $(EXE)
		$(CC) $(FLAGS) -o $(EXE) $(OBJS) $(DEPLIBS)

$(OBJS)	:	$(INCLUDES) Makefile

%.o	:	%.c
		$(CC) $(COPTS) $(INCLUDEDIR) -c -o $@ $<

