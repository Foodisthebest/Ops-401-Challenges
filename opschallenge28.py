#!/usr/bin/env python3
# Script Name: Event Logging Tool Part 3 of 3
# Author: Renona Gay, in collaboration with Juan Miguel Cano and Rodolfo Gonzolez
# Date of latest revision: 02/14/2024
# Purpose: Event Logging Tool Part 3 of 3
        


import logging
from logging.handlers import TimedRotatingFileHandler
import os
import time

# Create logging settings
logger = logging.getLogger('myTimedLogger')
logger.setLevel(logging.DEBUG)

# Create and configure handler for timed rotating file logs
# This will rotate the log file every day, keeping 7 days of backup logs
handler = TimedRotatingFileHandler('timed_collections_tool.log', when="D", interval=1, backupCount=7)
handler.setLevel(logging.DEBUG)
handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(handler)

# Create and configure FileHandler for logging to a file
file_handler = logging.FileHandler('collections_tool.log')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(file_handler)
