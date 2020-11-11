import json
import mysql.connector
from difflib import SequenceMatcher
from difflib import get_close_matches

user_name = 'python-app'
user_pass = input('Enter password for user %s:' % user_name)
db_name = 'english_dictionary'

#TODO: add a try to this to handle connection failures
cxn = mysql.connector.connect(
    user = user_name,
    password = user_pass,
    host = 'localhost',
    database = db_name
)

def getDefsFromDB(word):
    cursor = cxn.cursor()
    query = "SELECT definition FROM %s.definitions WHERE WORD = '%s'"%(db_name,word)
    cursor.execute(query)
    return [result[0] for result in cursor.fetchall()]

def loadWords():
    cursor = cxn.cursor()
    cursor.execute("SELECT WORD FROM %s.definitions"%db_name)
    return [result[0] for result in cursor.fetchall()]

def getCorrection(message):
    return input(message).lower()

def getDefinition(key):
    lower_key = key.lower()

    # Check multiple casings of what the user typed
    casings = [lower_key]
    casings.append(key.capitalize())
    casings.append(key.upper())

    # If we can find an exact match, return definition(s)
    for casing in casings:
        if casing in words:
            results = getDefsFromDB(casing)
            return '\n'.join(results)

    # If no exact match, check the closest match and prompt user
    matches = get_close_matches(lower_key,words)
    if len(matches) > 0:
        correction = getCorrection('No word %s found.  Did you mean %s instead? (Y/N): ' % (key, matches[0]))
        if correction == 'y':
            return '\n'.join(getDefsFromDB(matches[0]))
        elif correction == 'n':
            return ("Sorry, could not find a match for %s.  Please try again." % key)

    # If there is no close match or user refuses it
    return ("No close match to %s.  Check your spelling and try again." % key) 

words = loadWords()

while True:
    entry = input("Enter a word (q to quit): ")

    if entry.lower() == 'q':
        break

    print(getDefinition(entry))