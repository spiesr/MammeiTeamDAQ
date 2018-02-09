from ROOT import gROOT, TCanvas, TH1D, TTree, TFile
from array import array
import string
import sys

channel_dict = {"channel_counts_1":array( 'I', [ 0 ] ), \
"channel_counts_2":array( 'I', [ 0 ] ), \
"channel_counts_3":array( 'I', [ 0 ] ), \
"channel_counts_4":array( 'I', [ 0 ] ), \
"channel_counts_5":array( 'I', [ 0 ] ), \
"channel_counts_6":array( 'I', [ 0 ] ), \
"channel_counts_7":array( 'I', [ 0 ] ), \
"channel_counts_8":array( 'I', [ 0 ] ), \
"channel_counts_9":array( 'I', [ 0 ] ), \
"channel_counts_10":array( 'I', [ 0 ] ), \
"channel_counts_11":array( 'I', [ 0 ] ), \
"channel_counts_12":array( 'I', [ 0 ] ), \
"channel_counts_13":array( 'I', [ 0 ] ), \
"channel_counts_14":array( 'I', [ 0 ] ), \
"channel_counts_15":array( 'I', [ 0 ] ), \
"channel_counts_16":array( 'I', [ 0 ] ), \
"channel_counts_17":array( 'I', [ 0 ] ), \
"channel_counts_18":array( 'I', [ 0 ] ), \
"channel_counts_19":array( 'I', [ 0 ] ), \
"channel_counts_20":array( 'I', [ 0 ] ), \
"channel_counts_21":array( 'I', [ 0 ] ), \
"channel_counts_22":array( 'I', [ 0 ] ), \
"channel_counts_23":array( 'I', [ 0 ] ), \
"channel_counts_24":array( 'I', [ 0 ] ), \
"channel_counts_25":array( 'I', [ 0 ] ), \
"channel_counts_26":array( 'I', [ 0 ] ), \
"channel_counts_27":array( 'I', [ 0 ] ), \
"channel_counts_28":array( 'I', [ 0 ] ), \
"channel_counts_29":array( 'I', [ 0 ] ), \
"channel_counts_30":array( 'I', [ 0 ] ), \
"channel_counts_31":array( 'I', [ 0 ] ), \
"channel_counts_32":array( 'I', [ 0 ] )}

runnumber = int(sys.argv[1])
#analysis_type = int(sys.argv[2])

if not runnumber:
    print "No run number given, script will terminate"
    print "Try \"python analyzer.py runnumber\" where runnumber is replaced by an integer"
    sys.exit()

'''
if not analysis_type:
    print "Please specify either standard analysis (1), asymmetry analysis (2), or cosmics analysis (3)"
    sys.exit()
'''
'''
print "What is the run number?"
runnumber = input()
print "What data file is being analyzed?"
filename = raw_input()
'''
if runnumber < 10:
    filename = "data_sr90_actual/run000" + str(runnumber) + "_01.data"
else:
    filename = "data_sr90_actual/run00" + str(runnumber) + "_01.data"
rootfile_name = "run" + str(runnumber) + ".root"
if runnumber >= 10:
    logfile_name = "logs_sr90_actual/log00" + str(runnumber) + ".txt"
else:
    logfile_name = "logs_sr90_actual/log000" + str(runnumber) + ".txt"
f = TFile(rootfile_name,'create')

logfile = open(logfile_name,'r')
logline = logfile.readline()
plot_title = "Run" + str(runnumber) + " - " + logline
#LVDSplot.GetXAxis().SetTitle("Channel Number")
#LVDSplot.GetYAxis().SetTitle("Counts")

simpleDAQ = TTree("simpleDAQ","Simple DAQ data")

num_event = array( 'I', [ 0 ])
#channel_counts = array( 'I', [0 for x in range(16)])
time_tag = array( 'I', [ 0 ])
event_number = array( 'I', [ 0 ])
run_time = array('L', [ 0 ])

simpleDAQ.Branch("num_event",num_event,"num_event/I")
simpleDAQ.Branch("time_tag",time_tag,"time_tag/i")
simpleDAQ.Branch("event_number",event_number,"event_number/I")
simpleDAQ.Branch("run_time",run_time,"run_time/l")

if runnumber == 14:
    LVDSplot = TH1D("LVDS_channels",plot_title,100,0.0,33.0)
    for i in range(1,33):
        branchname = "channel_counts_" + str(i)
        branch_I = "channel_counts_" + str(i) + "/I"
        simpleDAQ.Branch(branchname,channel_dict[branchname],branch_I)
else:
    LVDSplot = TH1D("LVDS_channels",plot_title,100,0.0,17.0)
    for i in range(1,17):
        branchname = "channel_counts_" + str(i)
        branch_I = "channel_counts_" + str(i) + "/I"
        simpleDAQ.Branch(branchname,channel_dict[branchname],branch_I)

datafile = open(filename,'r')
eventline = datafile.readline()
eventline_contents = eventline.split()
events = int(eventline_contents[-1])
start_time_line = datafile.readline()
start_time_contents = start_time_line.split()
start_time = int(start_time_contents[-1])
#timeline = datafile.readline()
#timeline_contents = timeline.split()
#run_time[0] = int(timeline_contents[-1])
#simpleDAQ.Fill()
#junk = datafile.readline()
#junk = datafile.readline()
'''
while (1):
    header = datafile.readline()
    headerline = int(header,16)
    if ((headerline & 0x80000000) == 0x80000000):
        events -= 1
        if (((headerline & 0x200) == 0x200) and ((headerline & 0x7FFFFC00) == 0x0)):
            #Let's get this party started
            events += 1
            headerline = int(header,16)
            words = headerline & 0xFF
            words -= 1
            event_n = headerline & 0x2FFFF00
            event_number[0] = event_n >> 8
            for j in range(words):
                readin = datafile.readline()
                if (j == 0):
                    time_tag[0] = int(readin,16)
                else:
                    branchname = "channel_counts_" + str(j)
                    channel_dict[branchname][0] = int(readin,16)
                    LVDSplot.Fill(j,int(readin,16))
            simpleDAQ.Fill()
            break
    else:
        continue
'''
for i in range(events):
    #if (i == 0):
    #    print i
    header = datafile.readline()
    if (header[0] != '8'):
        break
    #print header
    if not header:
        events = i
        break
    headerline = int(header,16)
#    words = headerline & 0xFF
#    words -= 1
    event_n = headerline & 0x2FFFF00
    event_number[0] = event_n >> 8
    for j in range(17):
        readin = datafile.readline()
        if (j == 0):
            time_tag[0] = int(readin,16)
        else:
            branchname = "channel_counts_" + str(j)
            channel_dict[branchname][0] = int(readin,16)
            LVDSplot.Fill(j,int(readin,16))
    simpleDAQ.Fill()


num_event[0] = events
datafile.readline()
end_time_line = datafile.readline()
#print timeline
ent_time_contents = end_time_line.split()
end_time = int(timeline_contents[-1])
run_time[0] = end_time - start_time
simpleDAQ.Fill()
datafile.close()
f.Write()
f.Close()
