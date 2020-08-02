

while :
do
	echo "Run a1_ptt.py"
	python a1_ptt.py &

	timestamp=$(date +%s)
	#echo $timestamp
	timewait=480
	timestamp=$(( $timestamp + $timewait ))
	#echo $timestamp
	while [ $(date +%s) -lt $timestamp ]
	do
		echo $(date +%s)
		echo $timestamp
		sleep 10s
	done

	./kill.sh

	echo "a1_ptt.py done. sleep.."
	sleep 300s
done
