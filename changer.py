import json
import random
import time


def modify_json(file_path):
    # Load the JSON data from the file
    with open(file_path, "r") as f:
        data = json.load(f)

    # Get the access points list
    access_points = data["access_points"]

    # Choose a random access point to modify
    index = random.randint(0, len(access_points) - 1)
    access_point = access_points[index]

    # Choose a random action to perform on the access point
    action = random.choice(["modify_snr", "modify_channel", "delete", "add"])
    ap_name = random.choice(["MyAP", "HisAP", "HerAP", "TheirAP", "OurAP", "YourAP"])

    # Perform the action
    if action == "modify_snr":
        access_point["snr"] = random.randint(1, 100)
    elif action == "modify_channel":
        access_point["channel"] = random.randint(1, 11)
    elif action == "delete":
        if len(access_points) < 2:
            print() # Don't delete the last access point
        else:
            del access_points[index]
    elif action == "add":
        access_points.append({
            "ssid": ap_name + str(random.randint(1, 100)),
            "snr": random.randint(1, 100),
            "channel": random.randint(1, 11)
        })
    
    # Save the modified JSON data back to the file
    with open(file_path, "w") as f:
        json.dump(data, f, indent=4)

# Call the modify_json function to modify the data.json file
while True:
    modify_json("access_points.json")
    time.sleep(1)

