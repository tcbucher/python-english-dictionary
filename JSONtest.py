import json

with open('C:/Users/Tim/Udemy/Python/data.json','r') as data_file:
    data = json.load(data_file)

iterator = 0
for word, definition_list in data.items():
    for definition in definition_list:
        iterator += 1

print(iterator)