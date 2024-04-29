host="localhost"
user="root"
password="pass123"

import mysql.connector as mysql

db = mysql.connect(
  host = host,
  user = user,
  password = password
)

cursor = db.cursor()
db.database = "mydatabase"
# cursor.execute('''
#   create table data_pelanggan(ID INT NOT NULL AUTO_INCREMENT,
#   nama VARCHAR(100) NOT NULL,
#   alamat TEXT NOT NULL,
#   tanggal DATE,
#   PRIMARY KEY ( ID )
#   );
# ''')
# db.commit()

# cursor.execute("DESC TABLE data_pelanggan")
# print(cursor.fetchall())

# cursor.execute("ALTER TABLE data_pelanggan DROP tanggal")
# cursor.execute("INSERT INTO data_pelanggan (nama, alamat) VALUES('adi', 'surabaya')")
# cursor.execute("DELETE FROM data_pelanggan WHERE nama='burhan'")
# db.commit()

cursor.execute("SELECT * FROM data_pelanggan WHERE nama='agus'")
data = cursor.fetchall()
for row in data:
  print(row)
