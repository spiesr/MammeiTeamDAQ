#include <string.h>
//#include <starg.h>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>

//Read a hex number from control.in from the appropriate line and export that value as a long int to write to a VME board register.
long control_card_reader(char *line_name)
{
  long output;
  //int i, j, k;
  char buffer[255], line_start[255];
  char compare[1] = "#";
  FILE *control_card;
  
  control_card = fopen("control.in", "r");
 
  while (fgets(buffer, 255, control_card)) {
    if (buffer[0] == compare[0]) {
      continue;
    }
    sscanf(buffer,"%s %i",&line_start,&output);
    if (strcmp(line_start,line_name) == 0) {
      break;
    }
  }
  
  fclose(control_card); 
  
  return output;
}
