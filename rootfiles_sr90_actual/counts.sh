runstart=21
seqend=33
for i in `seq $runstart $seqend`;
do
	python counts.py $i >> counts.txt
done
