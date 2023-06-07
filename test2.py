import sqlite3

#creating database
conn = sqlite3.connect('test2.db')

with conn:
    cur = conn.cursor()
    # creating table w/ file names
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_files(\
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_fileName TEXT)")
    conn.commit()


conn = sqlite3.connect('test2.db')

#list of types of files
fileList = ('information.docx', 'Hello.txt', 'myImage.png', \
            'myMovie.mpg', 'World.txt', 'datatype.pdf', 'myPhoto.jpg')

#loop through each object in the list to find files that end with .txt.
for x in fileList:
    if x.endswith('.txt'):
        with conn:
            cur = conn.cursor()
        #inserting into db any value that ends with .txt.
            cur.execute("INSERT INTO tbl_files(col_fileName) VALUES (?)", (x,))
            print(x)

conn.close()
