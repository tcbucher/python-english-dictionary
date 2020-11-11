import json
import mysql.connector

# This is a script I created to open a JSON data file and insert its contents into a mysql database table

user_name = 'python-app'
user_pass = ''
while user_pass == '':
    user_pass = input('Enter password for user %s:' % user_name)
db_name = 'english_dictionary'

cxn = mysql.connector.connect(
    user = user_name,
    password = user_pass,
    host = 'localhost',
    database = db_name
)

cursor = cxn.cursor()

# Get out all the words from the database and put them in a list.  There should be a list of about 60k
cursor.execute("SELECT WORD FROM %s.definitions"%db_name)

# results = cursor.fetchall()
# flat_results = [result[0] for result in results]
flat_results = [result[0] for result in cursor.fetchall()]

print(flat_results[0:5])