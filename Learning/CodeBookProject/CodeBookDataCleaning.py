import json

def clean_data(data):
    data["users"] = [user for user in data["users"] if user["name".strip()]]
    return data

data = json.load(open("CodeBookDataErrors.json"))
data = clean_data(data)
json.dump(data, open("CodeBookDataCleaned.json", "w"), indent=4)
print("Data has been cleaned")