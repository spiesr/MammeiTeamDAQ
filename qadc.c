#include <stdlib.h>

#include "CAENVMEtypes.h"
#include "CAENVMEoslib.h"
#include "CAENVMElib.h"
#include "console.h"
#include "files.h"

uint32_t basaddr, data, addr;

int qadc_init(int32_t BHandle)
{
  int i;
  basaddr = control_card_reader("QADC_BASE_ADDR");
  
  addr = basaddr + 0x1006;
  data = 0x80;
  CAENVME_WriteCycle(BHandle,addr,&data,cvA32_U_DATA,cvD16);
  sleep(10);
  addr = basaddr + 0x1008;
  CAENVME_WriteCycle(BHandle,addr,&data,cvA32_U_DATA,cvD16);
  
  data = control_card_reader("QADC_THRESHOLD");
  for(i=0;i<32;i++)
    {
      addr = basaddr + 0x1080 + i*2;
      CAENVME_WriteCycle(BHandle,addr,&data,cvA32_U_DATA,cvD16);
    }
  for(i=16; i< 32; i++)
    {
      addr = basaddr + 0x1080 + i*2 ;
      CAENVME_ReadCycle(BHandle,addr,&data,cvA32_U_DATA,cvD16);
      data = data | 0x0100;
      CAENVME_WriteCycle(BHandle,addr,&data,cvA32_U_DATA,cvD16);
    }
  
  data = control_card_reader("QADC_PEDESTAL");
  addr = basaddr + 0x1060;
  CAENVME_WriteCycle(BHandle,addr,&data,cvA32_U_DATA,cvD16);
  
  return 0;
}

int qadc_start(int32_t BHandle)
{
  basaddr = control_card_reader("QADC_BASE_ADDR");
  
  addr = basaddr + 0x1032;
  data = 0x0004;
  CAENVME_WriteCycle(BHandle,addr,&data,cvA32_U_DATA,cvD16);
  addr = basaddr + 0x1034;
  data = 0x0004;
  CAENVME_WriteCycle(BHandle,addr,&data,cvA32_U_DATA,cvD16);
  
  addr = basaddr + 0x1040;
  data = 0x0001;
  CAENVME_WriteCycle(BHandle,addr,&data,cvA32_U_DATA,cvD16);
  sleep(10);
  
  return 0;
}
