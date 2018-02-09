read lastrun < lastrun.in
echo "The last run was: $lastrun"
runstart=$((lastrun + 1))
echo "How many runs are you having?"
read runs
seqend=$((runs + lastrun))
for i in `seq $runstart $seqend`;
do
	echo "The run number is: $i"
	python log.py $i
#	find . -maxdepth 1 -name "*.txt" -exec mv -i -t ~/logs
	./frontend 10000
	mv run.data data/run$i.data
done
mv *.txt logs/
echo $seqend > lastrun.in
