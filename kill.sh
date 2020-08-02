
ps aux | grep "python a1_ptt.py"

echo ""
echo ""

this_PID=$(ps aux | grep "python a1_ptt.py" | grep -v "grep" | cut -d " " -f3)
echo $this_PID
echo ""

this_PID=$(ps -ef | grep "python a1_ptt.py" | tr -s ' ' | cut -d ' ' -f2)
echo $this_PID
echo ""

this_PID=$(pidof python)
echo $this_PID
echo ""

kill -9 $this_PID
