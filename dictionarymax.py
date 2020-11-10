import json

with open('C:/Users/Tim/Udemy/Python/data.json','r') as data_file:
    data = json.load(data_file)

max_word = ''
max_definition = ''

for word in data.keys():
    if len(word) > len(max_word):
        max_word = word

for value in data.values():
    for definition in value:
        if len(definition) > len(max_definition):
            max_definition = definition

print("longest word (%s):"%(len(max_word)), max_word)
print("longest definition (%s):"%(len(max_definition)), max_definition)