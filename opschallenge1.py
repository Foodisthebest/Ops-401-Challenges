#!/usr/bin/env python3

# Done in collaboration with Cody Juhl

# Importing libraries for time and ping
import time
import datetime
from ping3 import ping

# Declare variable for future time stamp
ts = datetime.datetime.now()

# Function that carries out the execution
def uptime_sensor(ping_target):
    
    # Seeing if ping is successful
    success = ping(ping_target, timeout=1)

    if success:
        status = "Pinging is successful."

    else:
        status = "Ping failed."

    # Printing out status of the ping and telling if successful or not; {ts}= "timestamp"
    print (f"{ts} {status} to {ping_target}")
    time.sleep(2)

# This function asks for user input for IP address
ping_target = input("Please enter an IP address: ")

# This fuction calls back the variable ping_target
uptime_sensor(ping_target)