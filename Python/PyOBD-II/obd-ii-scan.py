
import os
import sys
import datetime
import obd  # Documentation at: https://python-obd.readthedocs.io/en/latest/

def main():
    
    try:
        # Establish connection with the OBD-II device
        connection = obd.OBD('/dev/tty.OBDII-SPPslave') # My device's MAC is: 00-1D-A5-06-92-5A

        # Initialize Datetime object for time comparison
        previousDateTimeRecorded = datetime.datetime.now()

        # Initialize lists for data points
        speedList = []
        rpmsList = []

        # While we're connected to the device, constantly check for basic information (i.e. Speed, RPMs, Current Gear)
        while (connection.is_connected()):
            rawSpeed = connection.query(obd.commands.SPEED).value.to("mph")
            rawRPMs = connection.query(obd.commands.RPM).value

            currentSpeed = rawSpeed.magnitude
            currentRPMs = rawRPMs.magnitude

            speedList.append(round(float(currentSpeed), 2))
            rpmsList.append(round(float(currentRPMs), 2))

            print("Time: %s" % (datetime.datetime.now().strftime("%m/%d/%Y %H:%M:%S")))
            print("Time within Snapshot: %s" % (datetime.datetime.now() - previousDateTimeRecorded))
            print("Speed: %s" % (currentSpeed))
            print("RPMs: %s" % (currentRPMs), end="\033[F\033[A\033[A")     # Used to overwrite the current terminal line.

            if ((datetime.datetime.now() - previousDateTimeRecorded) >= datetime.timedelta(minutes=1)):
                previousDateTimeRecorded = datetime.datetime.now()
                printedTime = previousDateTimeRecorded.strftime("%m/%d/%Y %H:%M")
                speed = round((sum(speedList)/len(speedList)), 2)
                rpms = round((sum(rpmsList)/len(rpmsList)), 2)

                with open('CarData.csv', 'a') as f:
                    f.write("%s,%s,%s,%i,%i\n" % (printedTime, str(speed), str(rpms), len(speedList), len(rpmsList)))
                    f.close()
                
                speedList = []
                rpmsList = []

    except Exception as e:
        print(e)    

main()