import json

# Open and read the JSON file
with open('00_data.json', 'r') as file:
    data = json.load(file)

# Display the contents of the JSON file
print(data)
