import json

def load_data(filename):
    with open(filename, "r") as f:
        data = json.load(f)
    return data

data = load_data("CodeBookData.json")

def display_users(data):
    for users in data['users']:
        print(f"{users['name']} is friends with {display_username_by_id(data, users['friends'])}")

def display_username_by_id(data, ids):
    userName = []
    userNameString = ""
    for id in ids:
        for users in data['users']:
            if users['id'] == id:
                userName.append(users['name'])
    for user in userName:
        userNameString += user
        userNameString += ","
    return userNameString

display_users(data)
#print(display_username_by_id(data, [1,2]))