import json
import mysql.connector

# This is a script I created to open a JSON data file and insert its contents into a mysql database table

user_name = 'python-app'
user_pass = input('Enter password for user %s:' % user_name)
db_name = "english_dictionary"

con = mysql.connector.connect(
    user = user_name,
    password = user_pass,
    host = 'localhost',
    database = db_name
)

cursor = con.cursor()
with open('C:/Users/Tim/Udemy/Python/data.json','r') as data_file:
    data = json.load(data_file)

iterator = 1
for word, definition_list in data.items():
    for definition in definition_list:
        statement = "INSERT INTO english_dictionary.definitions (word,definition) VALUES (%s, %s);"
        parameters = (word, definition)
        cursor.execute(statement, parameters)
        print(cursor.statement)
    iterator += 1
    if (iterator % 100 == 0):
        cursor.execute("COMMIT;")

cursor.execute("COMMIT;")