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
int V895_init(int32_t BHandle)
{
  basaddr = control_card_reader("V895_BASE_ADDR");

  //Set the channel mask
  addr = basaddr + 0x4A;
  data = control_card_reader("V895_PATERN_INHIBIT");
  CAENVME_WriteCycle(BHandle,addr,&data,cvA32_U_DATA,cvD16);
  
  //Set channel 0 threshold
  addr = basaddr + 0x00;
  data = control_card_reader("V895_THRESH_0");
  CAENVME_WriteCycle(BHandle,addr,&data,cvA32_U_DATA,cvD16);

  //Set channel 7 threshold
  addr = basaddr + 0x0E;
  data = control_card_reader("V895_THRESH_7");
  CAENVME_WriteCycle(BHandle,addr,&data,cvA32_U_DATA,cvD16);
  
  //Set majority level threshold
  addr = basaddr + 0x48;
  data = control_card_reader("V895_MAJ_THRESH");
  CAENVME_WriteCycle(BHandle,addr,&data,cvA32_U_DATA,cvD16);
  
  //Set majority level threshold
  addr = basaddr + 0x40;
  data = control_card_reader("V812_OUTPUT_WIDTH");
  CAENVME_WriteCycle(BHandle,addr,&data,cvA32_U_DATA,cvD16);  
    
  return 0;
}
