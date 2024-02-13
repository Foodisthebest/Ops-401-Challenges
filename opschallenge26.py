#! /usr/bin/env python3

# Ops Challenge - Event Loggin Tool Part 1 of 3

# Script:                     Event Logging
# Author:                     Renona Gay and Juan Cano
# Date of latest revision:    2/12/2024 
# Purpose:                    Ops 401 Challenge 26

import logging
# Configure logging settings to write to collections_tool.log
logging.basicConfig(filename='collections_tool.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
# Log the start of the script
logging.debug('Starting script execution.')
# Create a list
my_list = ['junk', 'stuff', 'house', 'car', 'cat', 'window', 'tree', 'pipe', 'dragonfruit', 'grape', 'nuts']
# Log the creation of the list
logging.debug('List created: %s', my_list)
# Print the entire list/array
print(my_list)
# Print the element at index 3 (fourth element) of the list/array called my_list
print(my_list[3])
# Print the last item in the list
print(my_list[-1])
# Print the fourth element on the list (again, as done above)
print(my_list[3])
# Print the sixth through the tenth element of the list (elements from index 5 to the end)
print(my_list[5:])
# Change the value of the seventh element (index 6) to "onion"
my_list[6] = "onion"
# Log the modification of the list
logging.debug('Modified list element at index 6 to "onion".')
# Print the entire list to show the updated list
print(my_list)
# Log the final state of the list
logging.debug('Final list: %s', my_list)
# Log the end of script execution
logging.debug('Script execution completed.')
