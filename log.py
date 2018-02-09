import sys
import string

run_number = int(sys.argv[1])
log_str = ""
logfile = open('log%d.txt' % run_number,'w')
while (1):
    test_type = input("What kind of test? (QWAD Threshold Test - 0, QWAD No Signal Tests - 1, QWAD Time Over Threshold - 2, QWAD Pulse Tests - 3) ")
    if (test_type == 0):
        log_str += "QWAD Threshold Tests - "
        bank_num = raw_input("What channel bank? (1,2,3) ")
        log_str += "Channel bank %s, " % (bank_num)
        voltage = raw_input("What voltage is the threshold at? (Enter a number like 4.2V) ")
        log_str += "%s Threshold" % (voltage)
        break
    elif (test_type == 1):
        log_str += "QWAD No Signal Tests - "
        bank_num = raw_input("What channel bank? (1,2,3) ")
        log_str += "Channel bank %s, " % (bank_num)
        state = raw_input("Is the QWAD on or off? ")
        log_str += "QWAD %s, " % (state)
        if (state == "on"):
            threshold = raw_input("Is the threshold internal or external? ")
            log_str += "%s threshold, " % (threshold)
            plug = raw_input("What is plugged in? (generator, terminator, or nothing) ")
            log_str += "%s plugged in" % (plug) 
        elif (state == "off"):
            plug = raw_input("What is plugged in? (generator, terminator, or nothing) ")
            log_str += "%s plugged in" % (plug)
        break
    elif (test_type == 2):
        log_str += "QWAD Time Over Threshold - Channel bank "
        channel_bank = raw_input("Which channel bank? (1,2,3) ")
        pulse_time = raw_input("How long is the pulse in us? (Enter a value like 100us) ")
        log_str += "%s, %s pulse length" % (channel_bank, pulse_time)
        break
    elif (test_type == 3):
        log_str += "QWAD Pulse Tests (V Threshold) - Channel Bank "
        channel_bank = raw_input("What channel bank is this? (1,2,3) ")
        signal_voltage = raw_input("What is the voltage of the pulse? (Enter a value like 10.0mV) ")
        signal_rate = raw_input("What is the signal frequency in Hz? (enter a value like 100Hz) ")
        trigger_rate = raw_input("What is the trigger frequency in Hz? (enter a value like 100Hz) ")
        log_str += "%s, %s %s signal, %s trigger" % (channel_bank, signal_voltage, signal_rate, trigger_rate)
        break
    elif (test_type == 4):
        log_str += "QWAD \"Asymmetry\" Tests - Channel bank "
        channel_bank = raw_input("What channel bank is this? (1,2,3) ")
        signal_rate = raw_input("What is the signal frequency in Hz? (enter a value like 100Hz) ")
        helicity = raw_input("What is the \"helicity\" in Hz? (enter a value like 100Hz) ")
        log_str += "%s, %s signal, %s helicity window" % (channel_bank, signal_rate, helicity)
        break
    else:
        print("Please enter a number from 0 to 4...\n")
logfile.write(log_str)
logfile.close()
