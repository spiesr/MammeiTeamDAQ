from ROOT import gROOT, TCanvas, TH1D, TTree, TFile
from array import array
import string
import sys
import math

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

delta_t = 3.008796e-10
delta_t *= 2.0

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
    #filename = "run00" + str(runnumber) + "_01.data"
rootfile_name = "run" + str(runnumber) + ".root"
if runnumber >= 10:
    logfile_name = "logs_sr90_actual/log00" + str(runnumber) + ".txt"
    #logfile_name = "log00" + str(runnumber) + ".txt"
else:
    logfile_name = "logs_sr90_actual/log000" + str(runnumber) + ".txt"
f = TFile(rootfile_name,'create')

#logfile = open(logfile_name,'r')
#logline = logfile.readline()
plot_title = "Run" + str(runnumber)
#LVDSplot.GetXAxis().SetTitle("Channel Number")
#LVDSplot.GetYAxis().SetTitle("Counts")

simpleDAQ = TTree("simpleDAQ","Simple DAQ data")

num_event = array( 'I', [ 0 ])
#channel_counts = array( 'I', [0 for x in range(16)])
time_tag = array( 'I', [ 0 ])
event_number = array( 'I', [ 0 ])
#run_time = array('I', [ 0 ])
end_time_pointer = array('L', [ 0 ])
start_time_pointer = array('L', [ 0 ])
aggregate_total_pointer = array('I', [ 0 ])
rate_scint_pointer = array('d', [ 0 ])
rate_scint_delta_pointer = array('d', [ 0 ])
rate_det_pointer = array('d', [ 0 ])
rate_det_delta_pointer = array('d', [ 0 ])

simpleDAQ.Branch("num_event",num_event,"num_event/i")
simpleDAQ.Branch("det_events",aggregate_total_pointer,"det_events/i")
simpleDAQ.Branch("time_tag",time_tag,"time_tag/i")
simpleDAQ.Branch("event_number",event_number,"event_number/I")
simpleDAQ.Branch("start_time",start_time_pointer,"start_time/l")
simpleDAQ.Branch("end_time",end_time_pointer,"end_time/l")
#simpleDAQ.Branch("run_time",run_time,"run_time/I")
simpleDAQ.Branch("rate_scint",rate_scint_pointer,"rate_scint/D")
simpleDAQ.Branch("rate_scint_delta",rate_scint_delta_pointer,"rate_scint_delta/D")
simpleDAQ.Branch("rate_det",rate_det_pointer,"rate_det/D")
simpleDAQ.Branch("rate_det_delta",rate_det_delta_pointer,"rate_det_delta/D")

'''
if runnumber == 14:
    LVDSplot = TH1D("LVDS_channels",plot_title,100,0.0,33.0)
    for i in range(1,33):
        branchname = "channel_counts_" + str(i)
        branch_I = "channel_counts_" + str(i) + "/I"
        simpleDAQ.Branch(branchname,channel_dict[branchname],branch_I)
'''

LVDSplot = TH1D("LVDS_channels",plot_title,100,0.0,17.0)
for i in range(1,17):
    branchname = "channel_counts_" + str(i)
    branch_I = "channel_counts_" + str(i) + "/I"
    simpleDAQ.Branch(branchname,channel_dict[branchname],branch_I)
totals = [0] * 16

line_num = 0
for line in reversed(open(filename).readlines()):
    if (line_num == 0):
        eventline = line.rstrip()
    elif (line_num == 1):
        end_time_line = line.rstrip()
    elif (line_num == 2):
        start_time_line = line.rstrip()
    line_num += 1

datafile = open(filename,'r')
#eventline = datafile.readline()
eventline_contents = eventline.split()
events = int(eventline_contents[-1])
#start_time_line = datafile.readline()
start_time_contents = start_time_line.split()
start_time = int(start_time_contents[-1])
end_time_contents = end_time_line.split()
end_time = int(end_time_contents[-1])
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
aggregate = 0
strips_on = 0
for i in range(events):
    #if (i == 0):
    #    print i
    header = datafile.readline()
    if (header[0] != '8'):
        break
    #print header
#    if not header:
#        events = i
#        break
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
            totals[j-1] += int(readin,16)
            if (int(readin,16) > 0):
                strips_on += 1
    simpleDAQ.Fill()
    if (strips_on > 0):
        aggregate += 1
    strips_on = 0

start_time_pointer[0] = start_time
end_time_pointer[0] = end_time
num_event[0] = events
aggregate_total_pointer[0] = aggregate
datafile.readline()
#end_time_line = datafile.readline()
#print timeline
#end_time_contents = end_time_line.split()
#end_time = int(end_time_line_contents[-1])
time = end_time - start_time
#run_time[0] = time
time *= 1e-6
rate_scint = events/time
rate_det = aggregate/time
rate_scint_pointer[0] = rate_scint
rate_det_pointer[0] = rate_det
rate_scint_delta = time
rate_scint_delta *= math.sqrt(events)
rate_scint_delta += (events*delta_t)
rate_scint_delta /= math.pow(time,2)
rate_det_delta = time
rate_det_delta *= math.sqrt(aggregate)
rate_det_delta += (aggregate*delta_t)
rate_det_delta /= math.pow(time,2)
rate_scint_delta_pointer[0] = rate_scint_delta
rate_det_delta_pointer[0] = rate_det_delta
simpleDAQ.Fill()
datafile.close()
f.Write()
f.Close()

tables_file = open('run_tables_data.tex','a')
tablestring = "\n\\begin{table}[h!]\n\\centering\n"
tablestring += "\\begin{tablular}{|c|c|c|c|c|c|c|c|c|}\n"
tablestring += "  \\hline\n  \\multicolumn{9}{|c|}{\\textb{Run "
tablestring += str(runnumber)
tablestring += "}} \\\\\n  \\hline\n  \\hline\n"
tablestring += "  \\multicolumn{3}{|c|}{\\textb{duration (s)}} & \\multicolumn{3}{|c|}{\\textb{coincidence events}} & \\multicolumn{3}{|c|}{\\textb{detector events}} \\\\\n"
tablestring += "  \\hline\n  \\multicolumn{3}{|c|}{"
tablestring += "%.2f" % time
tablestring += "} & \\multicolumn{3}{|c|}{"
tablestring += str(events)
tablestring += "} & \\multicolumn{3}{|c|}{"
tablestring += str(aggregate)
tablestring += "} \\\\\n  \\hline\n"
stripstring_1 = "  \\textb{strip:} "
stripstring_2 = "  \\textb{strip:} "
countstring_1 = "  \\textb{counts:} "
countstring_2 = "  \\textb{counts:} "
for i in range(17):
    if (i == 0):
        continue
    elif (i < 9):
        stripstring_1 += "& "
        stripstring_1 += str(i)
        stripstring_1 += " "
        countstring_1 += "& "
        countstring_1 += str(totals[i-1])
        countstring_1 += " "
    else:
        stripstring_2 += "& "
        stripstring_2 += str(i)
        stripstring_2 += " "
        countstring_2 += "& "
        countstring_2 += str(totals[i-1])
        countstring_2 += " "
stripstring_1 += "\\\\\n  \\hline\n"
stripstring_2 += "\\\\\n  \\hline\n"
countstring_1 += "\\\\\n  \\hline\n"
countstring_2 += "\\\\\n  \\hline\n"
tablestring += stripstring_1
tablestring += countstring_1
tablestring += stripstring_2
tablestring += countstring_2
tablestring += "  \\multicolumn{2}{|c|}{${R}_{scint}$} & \\multicolumn{2}{|c|}{$\\Delta {R}_{scint}$} & \\multicolumn{2}{|c|}{${R}_{det}$} & \\multicolumn{2}{|c|}{$\\Delta {R}_{det}$} &  \\cellcolor[gray]{.1} \\\\\n  \\hline\n"
tablestring += "  \\multicolumn{2}{|c|}{"
tablestring += "%.2f" % rate_scint
tablestring += "} & \\multicolumn{2}{|c|}{"
tablestring += "%.2f" % rate_scint_delta
tablestring += "} & \\multicolumn{2}{|c|}{"
tablestring += "%.2f" % rate_det
tablestring += "} & \\multicolumn{2}{|c|}{"
tablestring += "%.2f" % rate_det_delta
tablestring += "} & \\cellcolor[gray]{.1} \\\\\n  \\hline\n"
tablestring += "\\end{tabular}\n\\caption{Table of values for run "
tablestring += str(runnumber)
tablestring += "}\n\\label{runvalues"
tablestring += str(runnumber)
tablestring += "}\n\\end{table}\n\n"
tables_file.write(tablestring)
tables_file.close()

logfile = open(logfile_name,'r')
thresholdline = logfile.readline()
sourceline = logfile.readline()
logfile.readline()
delayline = logfile.readline()
logfile.close()

desc_file = open('run_tables_desc.tex','a')
tablestring = ""
tablestring += "\n\\begin{table}[h!]\n\\centering\n"
tablestring += "\\begin{tablular}{|c|c|}\n"
tablestring += "  \\hline\n  \\multicolumn{\\textb{Run "
tablestring += str(runnumber)
tablestring += "} \\\\\n  \\hline\n  \\hline\n"
tablestring += "  \\textb{Threshold Voltage:} & "
thresholdline_contents = thresholdline.split()
tablestring += thresholdline_contents[-1]  
tablestring += " \\\\\n  \\hline\n"
tablestring += "  \\textb{The source was:} & "
sourceline_contents = sourceline.split()
if (sourceline_contents[-1] == "none"):
    tablestring += "absent"
else:
    tablestring += "present"
tablestring += " \\\\\n  \\hline\n"
tablestring += "  \\textb{The delay point was:} & "
delayline_contents = delayline.split()
if (delayline_contents[-1] == "delay"):
    tablestring += "the full delay point"
else:
    tablestring += "the AND gate point"
tablestring += " \\\\\n  \\hline\n"
tablestring += "\\end{tabular}\n\\caption{Run parameters for run "
tablestring += str(runnumber)
tablestring += "}\n\\label{rundesc"
tablestring += str(runnumber)
tablestring += "}\n\\end{table}\n\n"
desc_file.write(tablestring)
desc_file.close()
