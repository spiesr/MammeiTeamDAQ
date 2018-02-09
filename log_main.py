import sys
import string

run_number = int(sys.argv[1])
log_str = ""
logfile = open('log%04d.txt' % run_number,'w')
threshold_voltage = raw_input("What was the threshold voltage applied to the comparators in volts? ")
log_str += "The threshold voltage was: "
log_str += threshold_voltage
log_str += "\n"
time_over_thresh = raw_input("What was the position of the source? (left, centre-left, centre, centre-right, right, none) ")
log_str += "The position of the source was: "
log_str += time_over_thresh
log_str += "\n"
detector_on = raw_input("Was the detector on? (yes/no) ")
log_str += "The detector was on?: "
log_str += detector_on
log_str += "\n"
out_of_time = raw_input("Where was the gate coming from? (AND gate, full delay) ")
log_str += "The gate came from: "
log_str += out_of_time
log_str += "\n"
logfile.write(log_str)
logfile.close()
