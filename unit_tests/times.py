timesfile = open("timing.txt","r")
times_array = []
for i in range(101):
    line_read = timesfile.readline()
    time_read = int(line_read)
    if (i > 0):
        time_to_append = time_read - time_last
        times_array.append(time_to_append)
    time_last = time_read
time_average = sum(times_array)/len(times_array)
print times_array
print "The average time is %i microseconds \n" % time_average
timesfile.close()
