import os, psycopg2, csv

DATABASE_URL = "postgresql://localhost/pridefarmers"
conn = psycopg2.connect(host="localhost",database="pridefarmers", user="postgres", password="justine")

csvfile = open("district.csv") 
reader = csv.reader(csvfile,delimiter=',')
print("Creating district table!")

cur = conn.cursor()

for name in reader:
	cur.execute("INSERT INTO accounts_district(name) VALUES(%s)",(name))

conn.commit()
print("Insert Completed!")