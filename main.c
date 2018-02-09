#include <string.h>
//#include <starg.h>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#include "CAENVMEtypes.h"
#include "CAENVMEoslib.h"
#include "CAENVMElib.h"
#include "console.h"

//#include "frontend.h"
#include "files.h"

#define HAVE_FADC
#define HAVE_LVDS

#undef HAVE_FADC

//From https://gist.github.com/sevko/d23646ba07c77c15fde9
long getMicrotime() {
  struct timeval currentTime;
  gettimeofday(&currentTime, NULL);
  return currentTime.tv_sec * (int)1e6 + currentTime.tv_usec;
}

int main()
{
  uint32_t readout, adc_basaddr;
  //int lognumber;
  int i;
  long timePassed;
  short Link, Device;
  CVBoardTypes VMEBoard = cvV2718;
  int32_t BHandle;
  //FILE *data_log;
  //readout = control_card_reader("LVDS_B_MASK");
  //readout = 0xFFFFFFFF;
  //printf("%u\n",readout);
  
  Link = 0;
  Device = 0;
  if( CAENVME_Init(VMEBoard, Link, Device, &BHandle) != cvSuccess )
  {
    printf("Error opening the device...\n");
    printf("Program is terminating...\n");
    return 0;
  }
  
  adc_basaddr = control_card_reader("QADC_BASE_ADDR");
  for (i=0;i<101;i++)
  {
    CAENVME_ReadCycle(BHandle,adc_basaddr+0x100E,&readout,cvA32_U_DATA,cvD16);
    timePassed = getMicrotime();
    printf("%ld \n",timePassed);
  }
  //lognumber = 1;
  //data_log = fopen("log1.data", "w+");
  //fprintf(data_log,"Run: %i\n",lognumber);
  //readout = 0xFFFFFFFF|0;
  //printf("%u\n",readout);
  return 0;
}
