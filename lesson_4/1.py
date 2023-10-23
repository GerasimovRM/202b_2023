import sqlite3

# con = sqlite3.connect(r"C:\Users\romag\PycharmProjects\tcs\202b_2023\lesson_4\db.sqlite")
con = sqlite3.connect("db.sqlite")

cur = con.cursor()

res = cur.execute("SELECT * FROM user")
data = res.fetchall()
print(data)
for user in data:
    print(user)

con.close()
