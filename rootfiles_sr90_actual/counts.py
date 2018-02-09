from ROOT import gROOT, TCanvas, TH1D, TTree, TFile
from array import array
import string
import sys
import math

temp_1 = [0]*16
temp_2 = [0]*16
temp_3 = [0]*16
temp_4 = [0]*16
temp_5 = [0]*16
counts_1 = [0]*16
counts_2 = [0]*16
counts_3 = [0]*16
counts_4 = [0]*16
counts_5 = [0]*16

runnumber = int(sys.argv[1])
filename = "run" + str(runnumber) + "_split.root"
f = TFile(filename,'open')
splitDAQ = f.Get("splitDAQ")
events = splitDAQ.GetEntries()

for i in range(events):
    splitDAQ.GetEntry(i)
    temp_1[0] = splitDAQ.channel_counts_1_1
    temp_1[1] = splitDAQ.channel_counts_2_1
    temp_1[2] = splitDAQ.channel_counts_3_1
    temp_1[3] = splitDAQ.channel_counts_4_1
    temp_1[4] = splitDAQ.channel_counts_5_1
    temp_1[5] = splitDAQ.channel_counts_6_1
    temp_1[6] = splitDAQ.channel_counts_7_1
    temp_1[7] = splitDAQ.channel_counts_8_1
    temp_1[8] = splitDAQ.channel_counts_9_1
    temp_1[9] = splitDAQ.channel_counts_10_1
    temp_1[10] = splitDAQ.channel_counts_11_1
    temp_1[11] = splitDAQ.channel_counts_12_1
    temp_1[12] = splitDAQ.channel_counts_13_1
    temp_1[13] = splitDAQ.channel_counts_14_1
    temp_1[14] = splitDAQ.channel_counts_15_1
    temp_1[15] = splitDAQ.channel_counts_16_1
    temp_2[0] = splitDAQ.channel_counts_1_2
    temp_2[1] = splitDAQ.channel_counts_2_2
    temp_2[2] = splitDAQ.channel_counts_3_2
    temp_2[3] = splitDAQ.channel_counts_4_2
    temp_2[4] = splitDAQ.channel_counts_5_2
    temp_2[5] = splitDAQ.channel_counts_6_2
    temp_2[6] = splitDAQ.channel_counts_7_2
    temp_2[7] = splitDAQ.channel_counts_8_2
    temp_2[8] = splitDAQ.channel_counts_9_2
    temp_2[9] = splitDAQ.channel_counts_10_2
    temp_2[10] = splitDAQ.channel_counts_11_2
    temp_2[11] = splitDAQ.channel_counts_12_2
    temp_2[12] = splitDAQ.channel_counts_13_2
    temp_2[13] = splitDAQ.channel_counts_14_2
    temp_2[14] = splitDAQ.channel_counts_15_2
    temp_2[15] = splitDAQ.channel_counts_16_2
    temp_3[0] = splitDAQ.channel_counts_1_3
    temp_3[1] = splitDAQ.channel_counts_2_3
    temp_3[2] = splitDAQ.channel_counts_3_3
    temp_3[3] = splitDAQ.channel_counts_4_3
    temp_3[4] = splitDAQ.channel_counts_5_3
    temp_3[5] = splitDAQ.channel_counts_6_3
    temp_3[6] = splitDAQ.channel_counts_7_3
    temp_3[7] = splitDAQ.channel_counts_8_3
    temp_3[8] = splitDAQ.channel_counts_9_3
    temp_3[9] = splitDAQ.channel_counts_10_3
    temp_3[10] = splitDAQ.channel_counts_11_3
    temp_3[11] = splitDAQ.channel_counts_12_3
    temp_3[12] = splitDAQ.channel_counts_13_3
    temp_3[13] = splitDAQ.channel_counts_14_3
    temp_3[14] = splitDAQ.channel_counts_15_3
    temp_3[15] = splitDAQ.channel_counts_16_3
    temp_4[0] = splitDAQ.channel_counts_1_4
    temp_4[1] = splitDAQ.channel_counts_2_4
    temp_4[2] = splitDAQ.channel_counts_3_4
    temp_4[3] = splitDAQ.channel_counts_4_4
    temp_4[4] = splitDAQ.channel_counts_5_4
    temp_4[5] = splitDAQ.channel_counts_6_4
    temp_4[6] = splitDAQ.channel_counts_7_4
    temp_4[7] = splitDAQ.channel_counts_8_4
    temp_4[8] = splitDAQ.channel_counts_9_4
    temp_4[9] = splitDAQ.channel_counts_10_4
    temp_4[10] = splitDAQ.channel_counts_11_4
    temp_4[11] = splitDAQ.channel_counts_12_4
    temp_4[12] = splitDAQ.channel_counts_13_4
    temp_4[13] = splitDAQ.channel_counts_14_4
    temp_4[14] = splitDAQ.channel_counts_15_4
    temp_4[15] = splitDAQ.channel_counts_16_4
    temp_5[0] = splitDAQ.channel_counts_1_5
    temp_5[1] = splitDAQ.channel_counts_2_5
    temp_5[2] = splitDAQ.channel_counts_3_5
    temp_5[3] = splitDAQ.channel_counts_4_5
    temp_5[4] = splitDAQ.channel_counts_5_5
    temp_5[5] = splitDAQ.channel_counts_6_5
    temp_5[6] = splitDAQ.channel_counts_7_5
    temp_5[7] = splitDAQ.channel_counts_8_5
    temp_5[8] = splitDAQ.channel_counts_9_5
    temp_5[9] = splitDAQ.channel_counts_10_5
    temp_5[10] = splitDAQ.channel_counts_11_5
    temp_5[11] = splitDAQ.channel_counts_12_5
    temp_5[12] = splitDAQ.channel_counts_13_5
    temp_5[13] = splitDAQ.channel_counts_14_5
    temp_5[14] = splitDAQ.channel_counts_15_5
    temp_5[15] = splitDAQ.channel_counts_16_5
    for j in range(16):
        if (temp_1[j] == 1):
            counts_1[j] += temp_1[j]
        if (temp_2[j] == 1):
            counts_2[j] += temp_2[j]
        if (temp_3[j] == 1):
            counts_3[j] += temp_3[j]
        if (temp_4[j] == 1):
            counts_4[j] += temp_4[j]
        if (temp_5[j] == 1):
            counts_5[j] += temp_5[j]

print("For run " + str(runnumber) + ":\n")
print("The counts for the first fifth were" + str(counts_1) + "\n")
print("The counts for the second fifth were" + str(counts_2) + "\n")
print("The counts for the third fifth were" + str(counts_3) + "\n")
print("The counts for the fourth fifth were" + str(counts_4) + "\n")
print("The counts for the fifth fifth were" + str(counts_5) + "\n")
