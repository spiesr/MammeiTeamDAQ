void cuts(int run_number)
{
  using namespace std;
  #include <cmath>
  #include <iostream>
  TFile *f = TFile::Open(Form("run%i.root",run_number));
  TFile *rates_file = new TFile("rate_plots_sr90.root","UPDATE");
  TTree *t = new TTree();
  TTree *simpleRates = new TTree(Form("simpleRates%i",run_number),Form("The rates for run %i",run_number));
  TH1F  *ratesHisto_1 = new TH1F("Channel_Rates",Form("Channel Rates for Run %i",run_number),100,0.0,100.0);
  t = (TTree*)f->Get("simpleDAQ");
  UInt_t time_tag_reading, time_tag_last, time_tag_first, time_tag_wraparound;
  Int_t i, j, k, n, m, wraparound, det_total, coinc_total, events, nentries;
  Float_t time_seconds, delta_total_rate, rates_total;
  Int_t counts[16], totals[16];
  ULong64_t start_time, end_time, start, end;
  Float_t rates[16], delta_counts[16], delta_rates[16];
  Float_t coinc_rate, delta_coinc_rate, det_rate, delta_det_rate;
  Float_t delta_T = 3.008796e-10;
  delta_T *= 2.0;
  bool is_noise, contains_data, is_data;
  t->SetBranchAddress("num_event",&nentries);
  t->SetBranchAddress("end_time",&end_time);
  t->SetBranchAddress("start_time",&start_time);
  for (i=0;i<16;i++)
  {
    j = i + 1;
    t->SetBranchAddress(Form("channel_counts_%i",j),&counts[i]);
  }
  i = 0;
  j = 0;
  k = 0;
  while (1)
  {
    t->GetEntry(i);
    if (j == 0)
    {
      if (nentries != 0)
      {
        events = nentries;
        k++;
      }
      else
      {
        continue;
      }
    }
    else if (j == 1)
    {
      if (start_time != 0)
      {
        start = start_time;
        k++;
      }
      else
      {
        continue;
      }
    }
    else if (j == 2)
    {
      if (end_time != 0)
      {
        end = end_time;
        k++;
      }
      else
      {
        continue;
      }
    }
    else if (j == 3)
    {
      break;
    }
    if (k == 0)
    {
      i++;
    }
    else if (k == 1)
    {
      i = 0;
      k = 0;
      j++;
    }
  }
  i = j = k = 0;
  for (i=0;i<events;i++)
  {
    t->GetEntry(i);
    k = 0;
    for (j=0;j<16;j++)
    {
      if (counts[j] >= 2)
      {
        k++;
      }
    }
    if (k == 1 || k == 2)
    {
      contains_data = true;
    }
    else if (k > 2)
    {
      is_noise = true;
    }
    else
    {
      is_data = true;
    }
    if ((contains_data || is_data) && !is_noise)
    {
       coinc_total++;
       if (is_data)
       {
         det_total++;
       }
    }
  }
  time_seconds = start - end;
  time_seconds *= 1e-6;
  coinc_rate = coinc_total/time_seconds;
  det_rate = det_total/time_seconds;
  delta_coinc_rate = time_seconds;
  delta_coinc_rate = sqrt(coinc_total);
  delta_coinc_rate += (delta_T*coinc_total);
  delta_coinc_rate /= pow(time_seconds,2.0);
  delta_det_rate = time_seconds;
  delta_det_rate = sqrt(det_total);
  delta_det_rate += (delta_T*det_total);
  delta_det_rate /= pow(time_seconds,2.0);
  cout << "For run number " << run_number << ": \n";
  cout << "The coincidence rate is: " << coinc_rate << "\n";
  cout << "The coincidence uncertainty is: " << delta_coinc_rate << "\n";
  cout << "The detector rate is: " << det_rate << "\n";
  cout << "The detector uncertainty is: " << delta_det_rate << "\n";
  f->Close();
}
