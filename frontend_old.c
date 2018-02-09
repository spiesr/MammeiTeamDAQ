#include <string.h>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <errno.h>
#include <time.h>

#include "CAENVMEtypes.h"
#include "CAENVMEoslib.h"
#include "CAENVMElib.h"
#include "console.h"
#include "files.h"
#include "qadc.h"
#include "lvds.h"
#include "V812.h"
#include "V895.h"

#define HAVE_QADC
#define HAVE_LVDS

#define HAVE_V895
#define HAVE_V812

#undef HAVE_QADC
//#undef HAVE_LVDS

#undef HAVE_V895
//#undef HAVE_V812

//From https://gist.github.com/sevko/d23646ba07c77c15fde9
long getMicrotime() 
{
  struct timeval currentTime;
  gettimeofday(&currentTime, NULL);
  return currentTime.tv_sec * (int)1e6 + currentTime.tv_usec;
}

int main(int argc, char *argv[])
{
  uint32_t event, num_words, time_tag, basaddr, error_code; 
  //addr, poll_adc, adc_basaddr, data;
  uint32_t event_mask = 0xFF;
  uint32_t time_tag_mask = 0x80000000;
  uint32_t error_mask = 0xF0000000;
  //uint32_t ready = 0x0001;
  int i, j, events, run_name_1, run_name_2;
  //int k;
  //int events_ptr[50];
  short Link, Device;
  CVBoardTypes VMEBoard = cvV1718; //used to declare the type of VME controller that is connected to the computer
  int32_t BHandle;
  FILE *data_log;
  char filename_string[17];
  //long timePassed;

/*#ifdef HAVE_QADC
  uint32_t ready = 0x0001;
  uint32_t addr, data, adc_basaddr, poll_adc;
  int k;
#endif*/
  
  //Test to see if there was a number of events given
  if (argc == 1)
  {
    printf("Error: number of events not given...\n");
    printf("Program is terminating...\n");
    return 0;
  }
  if (argc == 2)
  {
    printf("Error: number for filename not given \n");
    printf("Program is terminating...\n");
    return 0;
  }
  if (argc == 3)
  {
    printf("Error: number for filename not given \n");
    printf("Program is terminating...\n");
    return 0;
  }
  
  sscanf(argv[1],"%d",&events);
  sscanf(argv[2],"%d",&run_name_1);
  sscanf(argv[3],"%d",&run_name_2);
  sprintf(filename_string,"run%04i_%02i.data",run_name_1,run_name_2);
  printf("simpleDAQ initialized...\n");
  printf("%d events will be gathered...\n",events);
  
  //Test to see if the VME controller is connected and powered on
  Link = 0;
  Device = 0;
  if( CAENVME_Init(VMEBoard, Link, Device, &BHandle) != cvSuccess )
  {
    printf("Error opening the device...\n");
    printf("Program is terminating...\n");
    return 0;
  }
  
  printf("VME found, starting experiment...\n");
  //printf("How many events should this run gather?: ");
  //scanf("%i",events_ptr);
  //events = *events_ptr;

  data_log = fopen(filename_string,"w+");
  //fprintf(data_log,"Run: \n");
  fprintf(data_log,"Number of events: %i\n",events);
  //fprintf(data_log,"Events are below: \n\n");
  printf("Logfile initialized...\n");

#ifdef HAVE_V895
  V895_init(BHandle);
#endif

#ifdef HAVE_V812
  V812_init(BHandle);
#endif

//#ifdef HAVE_LVDS
  lvds_init(BHandle);
  printf("Boards initialized...\n");
  lvds_start(BHandle);
  printf("Run started...\n");
//  fprintf(data_log,"Start time: %ld\n",getMicrotime());
  basaddr = control_card_reader("LVDS_BASE_ADDR"); //Reads values from control.in like the base address of the V1495 in this instance
  fprintf(data_log,"Start time: %ld\n",getMicrotime());
  for (i=1; i<events; i++)
  {
    if (((i % 100) == 0) & (i != 0))
    {
      printf("Gathered %d events\n",i);
    }
    if (i == (events-1))
    {
      printf("Gathering last event...\n");
    }
    while (1)
    {
      //Read a word of data from the V1495, and see if it has the right structure for an event from the V1495
      CAENVME_ReadCycle(BHandle,basaddr,&event,cvA32_U_DATA,cvD32);
      num_words = event&event_mask;
      time_tag = event&time_tag_mask;
      error_code = event&error_mask;
      num_words -= 1;
      //If there are no words, no time tag, an error code, or the wrong number of words for the channels expected, move on
      if ((num_words == 0) || (time_tag != 0x80000000) || (error_code == 0xF0000000))
      {
        continue;
      }
      /*else if (num_words != 0x12)
      {
        for (j=0; j<num_words; j++)
        {
          CAENVME_ReadCycle(BHandle,basaddr,&event,cvA32_U_DATA,cvD32);
        }
        continue;
      }
      else if (error_code == 0xF0000000)
      {
        //CAENVME_ReadCycle(BHandle,basaddr,&event,cvA32_U_DATA,cvD32);
        //CAENVME_ReadCycle(BHandle,basaddr,&event,cvA32_U_DATA,cvD32);
        sleep(1);
        continue;
      }*/
      else
      {
        break;
      }
    }
    fprintf(data_log,"%x \n",event);
    //Read in the rest of the event after determining that it is the right event type
    for (j=0; j<num_words; j++)
    {
      CAENVME_ReadCycle(BHandle,basaddr,&event,cvA32_U_DATA,cvD32);
      fprintf(data_log,"%x \n",event);
    }
    //delay(11);
  }
//#endif

/*#ifdef HAVE_QADC
  lvds_init(BHandle);
  qadc_init(BHandle);
  printf("Boards initialized...\n");
  lvds_start(BHandle);
  qadc_start(BHandle);
  printf("Run started...\n");
  
  adc_basaddr = control_card_reader("QADC_BASE_ADDR");
  basaddr = control_card_reader("LVDS_BASE_ADDR");
  //wait for first event to be gathered, then gather five more to have a buffer
  addr = adc_basaddr + 0x100E;
  for (i=0;i<5;i++)
  {
    while (1)
    {
      CAENVME_ReadCycle(BHandle,adc_basaddr+0x100E,&poll_adc,cvA32_U_DATA,cvD16);
      printf("%x \n",poll_adc);
      if ((poll_adc & ready) == 0x1)
      {
        printf("loop started...\n");
        for (;;)
        {
          if (i == 4)
          {
            printf("Reading in fifth event...\n");
          }
          CAENVME_ReadCycle(BHandle,adc_basaddr,&data,cvA32_U_DATA,cvD32);
          if (((data & 0x07000000)>>24)==0x4)
          {
            printf("Event from QADC found");
            break;
          }
        }
        break;
      }
    }
  }
  printf("getting address of LVDS...\n");
  //gather first event from LVDS
  basaddr = 0xEEEE0000;
  printf("reading event from %x...\n",basaddr);
  while (1)
    {
      //Read a word of data from the V1495, and see if it has the right structure for an event from the V1495
      CAENVME_ReadCycle(BHandle,basaddr,&event,cvA32_U_DATA,cvD32);
      num_words = event&event_mask;
      time_tag = event&time_tag_mask;
      num_words -= 1;
      if ((num_words == 0) || (time_tag != 0x80000000))
      {
        continue;
      }
      else
      {
        break;
      }
    }
  //Wait until the proper "first" event is read in"
  while (1)
    {
      if ((0x7FFFFC00 & event) == 0x0)
      //((event & 0x200) == 0x200) && ((event & 0x7FFFFC00) == 0x0))
      {
        printf("First event written..\n");
        fprintf(data_log,"Start time: %ld\n",getMicrotime());
        fprintf(data_log,"Events are below: \n\n");
        fprintf(data_log,"%x \n",event);
        break;
      }
      else
      {
        for (j=0; j<num_words; j++)
        {
          CAENVME_ReadCycle(BHandle,basaddr,&event,cvA32_U_DATA,cvD32);
        }
        CAENVME_ReadCycle(BHandle,basaddr,&event,cvA32_U_DATA,cvD32);
        printf("%x \n",event);
        num_words = event&event_mask;
        num_words -= 1;
      }
      //printf("Searching...");
    }  
  for (j=0; j<num_words; j++)
    {
      CAENVME_ReadCycle(BHandle,basaddr,&event,cvA32_U_DATA,cvD32);
      fprintf(data_log,"%x \n",event);
    }
  printf("First event gathered, gathering remaining...\n");
  events -= 1;
  //gather the remaining events
  for (k=0;k<events;k++)
  {
    if (((k % 1000) == 0) & (k != 0))
    {
      printf("Gathered %d events\n",k);
    }
    if (k == (events-1))
    {
      printf("Gathering last event...\n");
    }
    //Wait for an event to be grabbed from the QADC
    while (1)
    {
      CAENVME_ReadCycle(BHandle,adc_basaddr+0x100E,&poll_adc,cvA32_U_DATA,cvD16);
      if ((poll_adc & ready) == 0x1)
      {
        for (;;)
        {
          CAENVME_ReadCycle(BHandle,adc_basaddr,&data,cvA32_U_DATA,cvD32);
          if (((data & 0x07000000)>>24)==0x4)
          {
            break;
          }
        }
        break;
      }
    }
    while (1)
    {
     //Read a word of data from the V1495, and see if it has the right structure for an event from the V1495
      CAENVME_ReadCycle(BHandle,basaddr,&event,cvA32_U_DATA,cvD32);
      num_words = event&event_mask;
      time_tag = event&time_tag_mask;
      num_words -= 1;
      if ((num_words == 0) || (time_tag != 0x80000000) || ((event & 0xF0000000) == 0xF0000000))
      {
        if ((event & 0xF0000000) == 0xF0000000) {
          CAENVME_ReadCycle(BHandle,basaddr,&event,cvA32_U_DATA,cvD32);
          CAENVME_ReadCycle(BHandle,basaddr,&event,cvA32_U_DATA,cvD32);
        }
        continue;
      }
      else
      {
        break;
      }
    }
    fprintf(data_log,"%x \n",event);
    for (j=0; j<num_words; j++)
    {
      CAENVME_ReadCycle(BHandle,basaddr,&event,cvA32_U_DATA,cvD32);
      fprintf(data_log,"%x \n",event);
    }
  }
#endif*/

  fprintf(data_log,"\nEnd time: %ld\n",getMicrotime());
  printf("Data collected, run ending...\n");
  
  return 0;
}
