runstart=20
seqend=33
for i in `seq $runstart $seqend`;
do
	python rates.py $i
done
