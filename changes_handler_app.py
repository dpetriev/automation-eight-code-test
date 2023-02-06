import socket
from deepdiff import DeepDiff as dd
import json
import re

# Ready for socket connection
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("localhost", 12345))
server_socket.listen(1)
oldVersionBool = True

while True:
    # Accept connection
    client_socket, client_address = server_socket.accept()
    content = client_socket.recv(1024).decode("utf-8")
    try:
        # Try to load the content as JSON
        json_content = json.loads(content)
        client_socket.close()

        if oldVersionBool:
            # Save the first version of the JSON data
            oldVersion = json_content
            oldVersionBool = False
        else:
            # Compare the old version of the JSON data with the new version
            newVersion = json_content
            diff = dd(oldVersion, newVersion)
            
            # Print the changes
            if 'values_changed' in diff:
                for key in diff['values_changed']:
                    string = key
                    pattern_index = r'\[(\d+)\]'
                    match_index = re.search(pattern_index, string)
                    if match_index:
                        value_index = int(match_index.group(1)) # Find index of access point

                    pattern_parameter = r"\['(\w+)'\]$"
                    match_parameter = re.search(pattern_parameter, string)
                    if match_parameter:
                        value_parameter = str(match_parameter.group(1)) # Output e.g. 'snr'

                    print(f"{oldVersion['access_points'][value_index]['ssid']}'s {value_parameter} value changed from {diff['values_changed'][key]['old_value']} to {diff['values_changed'][key]['new_value']}")
            elif "iterable_item_removed" in diff:
                for key in diff['iterable_item_removed']:
                    string = key

                    pattern_index = r'\[(\d+)\]'
                    match_index = re.search(pattern_index, string)
                    if match_index:
                        value_index = int(match_index.group(1))

                    print(f"{oldVersion['access_points'][value_index]['ssid']} was removed from the list")
            elif "iterable_item_added" in diff:
                for key in diff['iterable_item_added']:
                    string = key

                    pattern_index = r'\[(\d+)\]'
                    match_index = re.search(pattern_index, string)
                    if match_index:
                        value_index = int(match_index.group(1))

                    print(f"{newVersion['access_points'][value_index]['ssid']} was added to the list with the following parameters: {diff['iterable_item_added'][key]}")
            else:
                print('changer.py tried to delete last element in access_points.json.')
            # Save the old version of the JSON data for further comparison
            oldVersion = newVersion

    # If the JSON is incorrect, print an error message
    except json.decoder.JSONDecodeError as e:
        print("Error while parsing JSON:", e)
        client_socket.close()

