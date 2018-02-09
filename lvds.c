#include <string.h>
//#include <starg.h>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>

#include "CAENVMEtypes.h"
#include "CAENVMEoslib.h"
#include "CAENVMElib.h"
#include "console.h"
#include "files.h"

uint32_t basaddr, data, addr;

//Intialize the settings for this experiment
int lvds_init(int32_t BHandle)
{
  basaddr = control_card_reader("LVDS_BASE_ADDR");

  //Clear the software
  addr = basaddr + 0x1014;
  data = 0x8;
  CAENVME_WriteCycle(BHandle,addr,&data,cvA32_U_DATA,cvD32);
  sleep(10);
  
  //Set acquistion control settings from control.in
  addr = basaddr + 0x1000;
  data = control_card_reader("LVDS_ACQ_CTRL");
  CAENVME_WriteCycle(BHandle,addr,&data,cvA32_U_DATA,cvD32);

  //Set channel mask for channel group A from control.in
  addr = basaddr + 0x1020;
  data = control_card_reader("LVDS_A_MASK");
  CAENVME_WriteCycle(BHandle,addr,&data,cvA32_U_DATA,cvD32);
  
  //Set channel mask for channel group B from control.in
  addr = basaddr + 0x1024;
  data = control_card_reader("LVDS_B_MASK");
  CAENVME_WriteCycle(BHandle,addr,&data,cvA32_U_DATA,cvD32);
  
  return 0;
}

//Clear the MEB and delay
int lvds_start(int32_t BHandle)
{
  basaddr = control_card_reader("LVDS_BASE_ADDR");

  addr = basaddr + 0x1014;
  data = 0x6;
  CAENVME_WriteCycle(BHandle,addr,&data,cvA32_U_DATA,cvD32);
  sleep(10);

  return 0;
}

/*uint32_t lvds_get_event_word(int32_t BHandle)
{
  uint32_t output;

  basaddr = control_card_reader("LVDS_BASE_ADDR");

  CAENVME_ReadCycle(BHandle,basaddr,&data,cvA32_U_DATA,cvD32);
  output = data;

  return output;
}*/
