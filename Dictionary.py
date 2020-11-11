import json
import mysql.connector
from difflib import SequenceMatcher
from difflib import get_close_matches

user_name = 'python-app'
user_pass = input('Enter password for user %s:' % user_name)
db_name = 'english_dictionary'

con = mysql.connector.connect(
    user = user_name,
    password = user_pass,
    host = 'localhost',
    database = db_name
)

def getCorrection(message):
    return input(message).lower()

def getDefinition(key):
    lower_key = key.lower()

    casings = [lower_key]
    casings.append(key.capitalize())
    casings.append(key.upper())

    for casing in casings:
        if casing in data:
            return '\n'.join(data[casing])

    matches = get_close_matches(lower_key,data.keys())
    if len(matches) > 0:
        correction = getCorrection('No word %s found.  Did you mean %s instead? (Y/N): ' % (key, matches[0]))
        if correction == 'y':
            return '\n'.join(data[matches[0]])
        elif correction == 'n':
            return ("Sorry, could not find a match for %s.  Please try again." % key)

    return ("No close match to %s.  Check your spelling and try again." % key)

with open('C:/Users/Tim/Udemy/Python/data.json','r') as data_file:
    data = json.load(data_file)

while True:
    entry = input("Enter a word (q to quit): ")

    if entry.lower() == 'q':
        break

    print(getDefinition(entry))