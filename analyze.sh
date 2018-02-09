runstart=31
seqend=33
for i in `seq $runstart $seqend`;
do
	python analyzer.py $i 1
done
mv *.root rootfiles_sr90_actual/
