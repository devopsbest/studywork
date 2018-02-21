# # By Vamei
# import sqlite3
#
# # test.db is a file in the working directory.
# conn = sqlite3.connect("test.db")
#
# c = conn.cursor()
#
# # create tables
# c.execute('''CREATE TABLE category
#       (id int primary key, sort int, name text)''')
# c.execute('''CREATE TABLE book
#       (id int primary key,
#        sort int,
#        name text,
#        price real,
#        category int,
#        FOREIGN KEY (category) REFERENCES category(id))''')
#
# # save the changes
# conn.commit()
#
# # close the connection with the database
# conn.close()



# import sqlite3
#
# conn = sqlite3.connect("test.db")
# c    = conn.cursor()
#
# books = [(1, 1, 'Cook Recipe', 3.12, 1),
#             (2, 3, 'Python Intro', 17.5, 2),
#             (3, 2, 'OS Intro', 13.6, 2),
#            ]
#
# # execute "INSERT"
# c.execute("INSERT INTO category VALUES (1, 1, 'kitchen')")
#
# # execute multiple commands
# c.executemany('INSERT INTO book VALUES (?, ?, ?, ?, ?)', books)
#
# conn.commit()
# conn.close()

# import sqlite3
#
# conn = sqlite3.connect('test.db')
# c = conn.cursor()
#
#
# c.execute('UPDATE book SET price=? WHERE id=?',(1000, 1))
# c.execute('DELETE FROM book WHERE id=2')
# conn.commit()
# conn.close()

# # retrieve one record
# c.execute('SELECT name FROM category ORDER BY sort')
# print(c.fetchone())
# print(c.fetchone())
#
# # retrieve all records as a list
# c.execute('SELECT * FROM book WHERE book.category=1')
# print(c.fetchall())
#
# # iterate through the records
# for row in c.execute('SELECT name, price FROM book ORDER BY sort'):
#     print(row)
import pymysql

conn = pymysql.Connect(host='127.0.0.1', port=3306, user='root', passwd='root', db='imooc', charset='utf8')
cursor = conn.cursor()
print(conn)
print(cursor)
cursor.close()
conn.close()
