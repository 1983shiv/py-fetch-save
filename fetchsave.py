import requests
import mysql.connector

# Fetch records from remote API
response = requests.get("https://api.example.com/records")
records = response.json()

# Connect to MySQL database
cnx = mysql.connector.connect(user='user', password='password', host='host', database='database')
cursor = cnx.cursor()

# Insert records into MySQL database
for record in records:
    sql = "INSERT INTO table (column1, column2, column3) VALUES (%s, %s, %s)"
    values = (record['column1'], record['column2'], record['column3'])
    cursor.execute(sql, values)

# Commit changes to database and close cursor and connection
cnx.commit()
cursor.close()
cnx.close()
