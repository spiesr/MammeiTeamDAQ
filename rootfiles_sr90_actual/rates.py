from ROOT import gROOT, TCanvas, TH1D, TTree, TFile
from array import array
import string
import sys
import math

'''
gROOT.ProcessLine(
"struct channelCount_t {\
Int_t channel_1;\
Int_t channel_2;\
Int_t channel_3;\
Int_t channel_4;\
Int_t channel_5;\
Int_t channel_6;\
Int_t channel_7;\
Int_t channel_8;\
Int_t channel_9;\
Int_t channel_10;\
Int_t channel_11;\
Int_t channel_12;\
Int_t channel_13;\
Int_t channel_14;\
Int_t channel_15;\
Int_t channel_16;\
}")
'''

channel_dict_1 = {"channel_counts_1_1":array( 'I', [ 0 ] ), \
"channel_counts_2_1":array( 'I', [ 0 ] ), \
"channel_counts_3_1":array( 'I', [ 0 ] ), \
"channel_counts_4_1":array( 'I', [ 0 ] ), \
"channel_counts_5_1":array( 'I', [ 0 ] ), \
"channel_counts_6_1":array( 'I', [ 0 ] ), \
"channel_counts_7_1":array( 'I', [ 0 ] ), \
"channel_counts_8_1":array( 'I', [ 0 ] ), \
"channel_counts_9_1":array( 'I', [ 0 ] ), \
"channel_counts_10_1":array( 'I', [ 0 ] ), \
"channel_counts_11_1":array( 'I', [ 0 ] ), \
"channel_counts_12_1":array( 'I', [ 0 ] ), \
"channel_counts_13_1":array( 'I', [ 0 ] ), \
"channel_counts_14_1":array( 'I', [ 0 ] ), \
"channel_counts_15_1":array( 'I', [ 0 ] ), \
"channel_counts_16_1":array( 'I', [ 0 ] ), \
"channel_counts_17_1":array( 'I', [ 0 ] ), \
"channel_counts_18_1":array( 'I', [ 0 ] ), \
"channel_counts_19_1":array( 'I', [ 0 ] ), \
"channel_counts_20_1":array( 'I', [ 0 ] ), \
"channel_counts_21_1":array( 'I', [ 0 ] ), \
"channel_counts_22_1":array( 'I', [ 0 ] ), \
"channel_counts_23_1":array( 'I', [ 0 ] ), \
"channel_counts_24_1":array( 'I', [ 0 ] ), \
"channel_counts_25_1":array( 'I', [ 0 ] ), \
"channel_counts_26_1":array( 'I', [ 0 ] ), \
"channel_counts_27_1":array( 'I', [ 0 ] ), \
"channel_counts_28_1":array( 'I', [ 0 ] ), \
"channel_counts_29_1":array( 'I', [ 0 ] ), \
"channel_counts_30_1":array( 'I', [ 0 ] ), \
"channel_counts_31_1":array( 'I', [ 0 ] ), \
"channel_counts_32_1":array( 'I', [ 0 ] )}

channel_dict_2 = {"channel_counts_1_2":array( 'I', [ 0 ] ), \
"channel_counts_2_2":array( 'I', [ 0 ] ), \
"channel_counts_3_2":array( 'I', [ 0 ] ), \
"channel_counts_4_2":array( 'I', [ 0 ] ), \
"channel_counts_5_2":array( 'I', [ 0 ] ), \
"channel_counts_6_2":array( 'I', [ 0 ] ), \
"channel_counts_7_2":array( 'I', [ 0 ] ), \
"channel_counts_8_2":array( 'I', [ 0 ] ), \
"channel_counts_9_2":array( 'I', [ 0 ] ), \
"channel_counts_10_2":array( 'I', [ 0 ] ), \
"channel_counts_11_2":array( 'I', [ 0 ] ), \
"channel_counts_12_2":array( 'I', [ 0 ] ), \
"channel_counts_13_2":array( 'I', [ 0 ] ), \
"channel_counts_14_2":array( 'I', [ 0 ] ), \
"channel_counts_15_2":array( 'I', [ 0 ] ), \
"channel_counts_16_2":array( 'I', [ 0 ] ), \
"channel_counts_17_2":array( 'I', [ 0 ] ), \
"channel_counts_18_2":array( 'I', [ 0 ] ), \
"channel_counts_19_2":array( 'I', [ 0 ] ), \
"channel_counts_20_2":array( 'I', [ 0 ] ), \
"channel_counts_21_2":array( 'I', [ 0 ] ), \
"channel_counts_22_2":array( 'I', [ 0 ] ), \
"channel_counts_23_2":array( 'I', [ 0 ] ), \
"channel_counts_24_2":array( 'I', [ 0 ] ), \
"channel_counts_25_2":array( 'I', [ 0 ] ), \
"channel_counts_26_2":array( 'I', [ 0 ] ), \
"channel_counts_27_2":array( 'I', [ 0 ] ), \
"channel_counts_28_2":array( 'I', [ 0 ] ), \
"channel_counts_29_2":array( 'I', [ 0 ] ), \
"channel_counts_30_2":array( 'I', [ 0 ] ), \
"channel_counts_31_2":array( 'I', [ 0 ] ), \
"channel_counts_32_2":array( 'I', [ 0 ] )}

channel_dict_3 = {"channel_counts_1_3":array( 'I', [ 0 ] ), \
"channel_counts_2_3":array( 'I', [ 0 ] ), \
"channel_counts_3_3":array( 'I', [ 0 ] ), \
"channel_counts_4_3":array( 'I', [ 0 ] ), \
"channel_counts_5_3":array( 'I', [ 0 ] ), \
"channel_counts_6_3":array( 'I', [ 0 ] ), \
"channel_counts_7_3":array( 'I', [ 0 ] ), \
"channel_counts_8_3":array( 'I', [ 0 ] ), \
"channel_counts_9_3":array( 'I', [ 0 ] ), \
"channel_counts_10_3":array( 'I', [ 0 ] ), \
"channel_counts_11_3":array( 'I', [ 0 ] ), \
"channel_counts_12_3":array( 'I', [ 0 ] ), \
"channel_counts_13_3":array( 'I', [ 0 ] ), \
"channel_counts_14_3":array( 'I', [ 0 ] ), \
"channel_counts_15_3":array( 'I', [ 0 ] ), \
"channel_counts_16_3":array( 'I', [ 0 ] ), \
"channel_counts_17_3":array( 'I', [ 0 ] ), \
"channel_counts_18_3":array( 'I', [ 0 ] ), \
"channel_counts_19_3":array( 'I', [ 0 ] ), \
"channel_counts_20_3":array( 'I', [ 0 ] ), \
"channel_counts_21_3":array( 'I', [ 0 ] ), \
"channel_counts_22_3":array( 'I', [ 0 ] ), \
"channel_counts_23_3":array( 'I', [ 0 ] ), \
"channel_counts_24_3":array( 'I', [ 0 ] ), \
"channel_counts_25_3":array( 'I', [ 0 ] ), \
"channel_counts_26_3":array( 'I', [ 0 ] ), \
"channel_counts_27_3":array( 'I', [ 0 ] ), \
"channel_counts_28_3":array( 'I', [ 0 ] ), \
"channel_counts_29_3":array( 'I', [ 0 ] ), \
"channel_counts_30_3":array( 'I', [ 0 ] ), \
"channel_counts_31_3":array( 'I', [ 0 ] ), \
"channel_counts_32_3":array( 'I', [ 0 ] )}

channel_dict_4 = {"channel_counts_1_4":array( 'I', [ 0 ] ), \
"channel_counts_2_4":array( 'I', [ 0 ] ), \
"channel_counts_3_4":array( 'I', [ 0 ] ), \
"channel_counts_4_4":array( 'I', [ 0 ] ), \
"channel_counts_5_4":array( 'I', [ 0 ] ), \
"channel_counts_6_4":array( 'I', [ 0 ] ), \
"channel_counts_7_4":array( 'I', [ 0 ] ), \
"channel_counts_8_4":array( 'I', [ 0 ] ), \
"channel_counts_9_4":array( 'I', [ 0 ] ), \
"channel_counts_10_4":array( 'I', [ 0 ] ), \
"channel_counts_11_4":array( 'I', [ 0 ] ), \
"channel_counts_12_4":array( 'I', [ 0 ] ), \
"channel_counts_13_4":array( 'I', [ 0 ] ), \
"channel_counts_14_4":array( 'I', [ 0 ] ), \
"channel_counts_15_4":array( 'I', [ 0 ] ), \
"channel_counts_16_4":array( 'I', [ 0 ] ), \
"channel_counts_17_4":array( 'I', [ 0 ] ), \
"channel_counts_18_4":array( 'I', [ 0 ] ), \
"channel_counts_19_4":array( 'I', [ 0 ] ), \
"channel_counts_20_4":array( 'I', [ 0 ] ), \
"channel_counts_21_4":array( 'I', [ 0 ] ), \
"channel_counts_22_4":array( 'I', [ 0 ] ), \
"channel_counts_23_4":array( 'I', [ 0 ] ), \
"channel_counts_24_4":array( 'I', [ 0 ] ), \
"channel_counts_25_4":array( 'I', [ 0 ] ), \
"channel_counts_26_4":array( 'I', [ 0 ] ), \
"channel_counts_27_4":array( 'I', [ 0 ] ), \
"channel_counts_28_4":array( 'I', [ 0 ] ), \
"channel_counts_29_4":array( 'I', [ 0 ] ), \
"channel_counts_30_4":array( 'I', [ 0 ] ), \
"channel_counts_31_4":array( 'I', [ 0 ] ), \
"channel_counts_32_4":array( 'I', [ 0 ] )}

channel_dict_5 = {"channel_counts_1_5":array( 'I', [ 0 ] ), \
"channel_counts_2_5":array( 'I', [ 0 ] ), \
"channel_counts_3_5":array( 'I', [ 0 ] ), \
"channel_counts_4_5":array( 'I', [ 0 ] ), \
"channel_counts_5_5":array( 'I', [ 0 ] ), \
"channel_counts_6_5":array( 'I', [ 0 ] ), \
"channel_counts_7_5":array( 'I', [ 0 ] ), \
"channel_counts_8_5":array( 'I', [ 0 ] ), \
"channel_counts_9_5":array( 'I', [ 0 ] ), \
"channel_counts_10_5":array( 'I', [ 0 ] ), \
"channel_counts_11_5":array( 'I', [ 0 ] ), \
"channel_counts_12_5":array( 'I', [ 0 ] ), \
"channel_counts_13_5":array( 'I', [ 0 ] ), \
"channel_counts_14_5":array( 'I', [ 0 ] ), \
"channel_counts_15_5":array( 'I', [ 0 ] ), \
"channel_counts_16_5":array( 'I', [ 0 ] ), \
"channel_counts_17_5":array( 'I', [ 0 ] ), \
"channel_counts_18_5":array( 'I', [ 0 ] ), \
"channel_counts_19_5":array( 'I', [ 0 ] ), \
"channel_counts_20_5":array( 'I', [ 0 ] ), \
"channel_counts_21_5":array( 'I', [ 0 ] ), \
"channel_counts_22_5":array( 'I', [ 0 ] ), \
"channel_counts_23_5":array( 'I', [ 0 ] ), \
"channel_counts_24_5":array( 'I', [ 0 ] ), \
"channel_counts_25_5":array( 'I', [ 0 ] ), \
"channel_counts_26_5":array( 'I', [ 0 ] ), \
"channel_counts_27_5":array( 'I', [ 0 ] ), \
"channel_counts_28_5":array( 'I', [ 0 ] ), \
"channel_counts_29_5":array( 'I', [ 0 ] ), \
"channel_counts_30_5":array( 'I', [ 0 ] ), \
"channel_counts_31_5":array( 'I', [ 0 ] ), \
"channel_counts_32_5":array( 'I', [ 0 ] )}

runnumber = int(sys.argv[1])

filename = "run" + str(runnumber) + ".root"
newfilename = "run" + str(runnumber) + "_split.root"

#f = TFile(filename,'open')
new_f = TFile(newfilename,'create')
splitDAQ = TTree("splitDAQ","split DAQ data")

for i in range(1,17):
    branchname = "channel_counts_" + str(i) + "_1"
    branch_I = "channel_counts_" + str(i) + "_1/I"
    splitDAQ.Branch(branchname,channel_dict_1[branchname],branch_I)
    branchname = "channel_counts_" + str(i) + "_2"
    branch_I = "channel_counts_" + str(i) + "_2/I"
    splitDAQ.Branch(branchname,channel_dict_2[branchname],branch_I)
    branchname = "channel_counts_" + str(i) + "_3"
    branch_I = "channel_counts_" + str(i) + "_3/I"
    splitDAQ.Branch(branchname,channel_dict_3[branchname],branch_I)
    branchname = "channel_counts_" + str(i) + "_4"
    branch_I = "channel_counts_" + str(i) + "_4/I"
    splitDAQ.Branch(branchname,channel_dict_4[branchname],branch_I)
    branchname = "channel_counts_" + str(i) + "_5"
    branch_I = "channel_counts_" + str(i) + "_5/I"
    splitDAQ.Branch(branchname,channel_dict_5[branchname],branch_I)

f = TFile(filename,'open')
simpleDAQ = f.Get("simpleDAQ")
'''
for i in range(1,17):
    channelstring = "channel_" + str(i)
    branchname = "channel_counts_" + str(i)
    simpleDAQ.SetBranchAddress(branchname,AddressOf(channelCount,channelstring))
'''
nentries = simpleDAQ.GetEntries()

events = nentries-2
k = 1
fifths = math.floor(events/5)
for i in range(events):
    simpleDAQ.GetEntry(i)
    if (k == 1):
        channel_dict_1["channel_counts_1_1"][0] = simpleDAQ.channel_counts_1
        channel_dict_1["channel_counts_2_1"][0] = simpleDAQ.channel_counts_2
        channel_dict_1["channel_counts_3_1"][0] = simpleDAQ.channel_counts_3
        channel_dict_1["channel_counts_4_1"][0] = simpleDAQ.channel_counts_4
        channel_dict_1["channel_counts_5_1"][0] = simpleDAQ.channel_counts_5
        channel_dict_1["channel_counts_6_1"][0] = simpleDAQ.channel_counts_6
        channel_dict_1["channel_counts_7_1"][0] = simpleDAQ.channel_counts_7
        channel_dict_1["channel_counts_8_1"][0] = simpleDAQ.channel_counts_8
        channel_dict_1["channel_counts_9_1"][0] = simpleDAQ.channel_counts_9
        channel_dict_1["channel_counts_10_1"][0] = simpleDAQ.channel_counts_10
        channel_dict_1["channel_counts_11_1"][0] = simpleDAQ.channel_counts_11
        channel_dict_1["channel_counts_12_1"][0] = simpleDAQ.channel_counts_12
        channel_dict_1["channel_counts_13_1"][0] = simpleDAQ.channel_counts_13
        channel_dict_1["channel_counts_14_1"][0] = simpleDAQ.channel_counts_14
        channel_dict_1["channel_counts_15_1"][0] = simpleDAQ.channel_counts_15
        channel_dict_1["channel_counts_16_1"][0] = simpleDAQ.channel_counts_16
        splitDAQ.Fill()
    elif (k == 2):
        channel_dict_2["channel_counts_1_2"][0] = simpleDAQ.channel_counts_1
        channel_dict_2["channel_counts_2_2"][0] = simpleDAQ.channel_counts_2
        channel_dict_2["channel_counts_3_2"][0] = simpleDAQ.channel_counts_3
        channel_dict_2["channel_counts_4_2"][0] = simpleDAQ.channel_counts_4
        channel_dict_2["channel_counts_5_2"][0] = simpleDAQ.channel_counts_5
        channel_dict_2["channel_counts_6_2"][0] = simpleDAQ.channel_counts_6
        channel_dict_2["channel_counts_7_2"][0] = simpleDAQ.channel_counts_7
        channel_dict_2["channel_counts_8_2"][0] = simpleDAQ.channel_counts_8
        channel_dict_2["channel_counts_9_2"][0] = simpleDAQ.channel_counts_9
        channel_dict_2["channel_counts_10_2"][0] = simpleDAQ.channel_counts_10
        channel_dict_2["channel_counts_11_2"][0] = simpleDAQ.channel_counts_11
        channel_dict_2["channel_counts_12_2"][0] = simpleDAQ.channel_counts_12
        channel_dict_2["channel_counts_13_2"][0] = simpleDAQ.channel_counts_13
        channel_dict_2["channel_counts_14_2"][0] = simpleDAQ.channel_counts_14
        channel_dict_2["channel_counts_15_2"][0] = simpleDAQ.channel_counts_15
        channel_dict_2["channel_counts_16_2"][0] = simpleDAQ.channel_counts_16
        splitDAQ.Fill()
    elif (k == 3):
        channel_dict_3["channel_counts_1_3"][0] = simpleDAQ.channel_counts_1
        channel_dict_3["channel_counts_2_3"][0] = simpleDAQ.channel_counts_2
        channel_dict_3["channel_counts_3_3"][0] = simpleDAQ.channel_counts_3
        channel_dict_3["channel_counts_4_3"][0] = simpleDAQ.channel_counts_4
        channel_dict_3["channel_counts_5_3"][0] = simpleDAQ.channel_counts_5
        channel_dict_3["channel_counts_6_3"][0] = simpleDAQ.channel_counts_6
        channel_dict_3["channel_counts_7_3"][0] = simpleDAQ.channel_counts_7
        channel_dict_3["channel_counts_8_3"][0] = simpleDAQ.channel_counts_8
        channel_dict_3["channel_counts_9_3"][0] = simpleDAQ.channel_counts_9
        channel_dict_3["channel_counts_10_3"][0] = simpleDAQ.channel_counts_10
        channel_dict_3["channel_counts_11_3"][0] = simpleDAQ.channel_counts_11
        channel_dict_3["channel_counts_12_3"][0] = simpleDAQ.channel_counts_12
        channel_dict_3["channel_counts_13_3"][0] = simpleDAQ.channel_counts_13
        channel_dict_3["channel_counts_14_3"][0] = simpleDAQ.channel_counts_14
        channel_dict_3["channel_counts_15_3"][0] = simpleDAQ.channel_counts_15
        channel_dict_3["channel_counts_16_3"][0] = simpleDAQ.channel_counts_16
        splitDAQ.Fill()
    elif (k == 4):
        channel_dict_4["channel_counts_1_4"][0] = simpleDAQ.channel_counts_1
        channel_dict_4["channel_counts_2_4"][0] = simpleDAQ.channel_counts_2
        channel_dict_4["channel_counts_3_4"][0] = simpleDAQ.channel_counts_3
        channel_dict_4["channel_counts_4_4"][0] = simpleDAQ.channel_counts_4
        channel_dict_4["channel_counts_5_4"][0] = simpleDAQ.channel_counts_5
        channel_dict_4["channel_counts_6_4"][0] = simpleDAQ.channel_counts_6
        channel_dict_4["channel_counts_7_4"][0] = simpleDAQ.channel_counts_7
        channel_dict_4["channel_counts_8_4"][0] = simpleDAQ.channel_counts_8
        channel_dict_4["channel_counts_9_4"][0] = simpleDAQ.channel_counts_9
        channel_dict_4["channel_counts_10_4"][0] = simpleDAQ.channel_counts_10
        channel_dict_4["channel_counts_11_4"][0] = simpleDAQ.channel_counts_11
        channel_dict_4["channel_counts_12_4"][0] = simpleDAQ.channel_counts_12
        channel_dict_4["channel_counts_13_4"][0] = simpleDAQ.channel_counts_13
        channel_dict_4["channel_counts_14_4"][0] = simpleDAQ.channel_counts_14
        channel_dict_4["channel_counts_15_4"][0] = simpleDAQ.channel_counts_15
        channel_dict_4["channel_counts_16_4"][0] = simpleDAQ.channel_counts_16
        splitDAQ.Fill()
    elif (k == 5):
        channel_dict_5["channel_counts_1_5"][0] = simpleDAQ.channel_counts_1
        channel_dict_5["channel_counts_2_5"][0] = simpleDAQ.channel_counts_2
        channel_dict_5["channel_counts_3_5"][0] = simpleDAQ.channel_counts_3
        channel_dict_5["channel_counts_4_5"][0] = simpleDAQ.channel_counts_4
        channel_dict_5["channel_counts_5_5"][0] = simpleDAQ.channel_counts_5
        channel_dict_5["channel_counts_6_5"][0] = simpleDAQ.channel_counts_6
        channel_dict_5["channel_counts_7_5"][0] = simpleDAQ.channel_counts_7
        channel_dict_5["channel_counts_8_5"][0] = simpleDAQ.channel_counts_8
        channel_dict_5["channel_counts_9_5"][0] = simpleDAQ.channel_counts_9
        channel_dict_5["channel_counts_10_5"][0] = simpleDAQ.channel_counts_10
        channel_dict_5["channel_counts_11_5"][0] = simpleDAQ.channel_counts_11
        channel_dict_5["channel_counts_12_5"][0] = simpleDAQ.channel_counts_12
        channel_dict_5["channel_counts_13_5"][0] = simpleDAQ.channel_counts_13
        channel_dict_5["channel_counts_14_5"][0] = simpleDAQ.channel_counts_14
        channel_dict_5["channel_counts_15_5"][0] = simpleDAQ.channel_counts_15
        channel_dict_5["channel_counts_16_5"][0] = simpleDAQ.channel_counts_16
        splitDAQ.Fill()
    if (((i%fifths) == 0) and (i != 0) and (k != 5)):
        for j in range(1,17):
            branchname = "channel_counts_" + str(j) + "_1"
            channel_dict_1[branchname][0] = 0
            branchname = "channel_counts_" + str(j) + "_2"
            channel_dict_2[branchname][0] = 0
            branchname = "channel_counts_" + str(j) + "_3"
            channel_dict_3[branchname][0] = 0
            branchname = "channel_counts_" + str(j) + "_4"
            channel_dict_4[branchname][0] = 0
            branchname = "channel_counts_" + str(j) + "_5"
            channel_dict_5[branchname][0] = 0
        k += 1

f.Close()

#new_f = TFile(newfilename,'create')
new_f.Write()
new_f.Close()
