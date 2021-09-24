#!/bin/bash
# A battery alert shell script (infinite loop) that runs in macOS (if you're using a third party battery app like coconutBattery, that does not support alerts with the free version). By default, script runs and sleeps for 60 seconds. An AppleScript runs when the battery reaches 10%, stating the battery is low.

sleeptime=60

BatteryAlert(){
percentage=$(pmset -g batt | egrep "([0-9]+\%).*" -o | cut -f1 -d';' | sed 's/%//' | bc)
alertlevel=10

if [ "$percentage" -le "$alertlevel" ]
then
	if [ ! -f "./batteryalert_lock" ] 
	then
	/usr/bin/osascript <<-EOF
    	tell application "System Events"
       		activate
        	display dialog "Your battery is at $percentage%. It is recommended you plug into a power outlet, or shut down!"
    	end tell
	EOF

	touch ./batteryalert_lock
	fi

	echo "Battery life is at $percentage%. Battery is running low."

elif [ "$percentage" -gt "$alertlevel" ]
then
	echo "Battery life is at $percentage%. No need to worry... yet."
	
	if [ -f "./batteryalert_lock" ]
	then
	rm ./batteryalert_lock
	fi

else
	echo "Error"
	# Do nothing
fi
}

while (true)
do
	BatteryAlert;
	sleep $sleeptime;
done