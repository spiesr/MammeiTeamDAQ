read lastrun < lastrun_main.in
echo "The last run was: $lastrun"
runstart=$((lastrun + 1))
echo "How many runs are you having?"
read runs
seqend=$((runs + lastrun))
for i in `seq $runstart $seqend`;
do
        echo "The run number is: $i"
        python log_main.py $i
	echo "Run time in minutes? (420 without source, 180 with source)"
	read minutes
	./frontend $minutes $i 1
#       find . -maxdepth 1 -name "*.txt" -exec mv -i -t ~/logs
#	for j in `seq 1 20`;
#	do
#	        ./frontend 5000 $i $j
#		python nextrun.py
#	done
done
mv *.data data_sr90_actual/
mv *.txt logs_sr90_actual/
echo $seqend > lastrun_main.in
