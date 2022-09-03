import sqlite3

conn = sqlite3.connect('serve.db')

cursor = conn.execute("SELECT NAME, TOPIC from SERVERS");
for row in cursor:
    print("Name = ", row[0])
    print("Topic = ", row[1])
print ("table created successfully")
conn.close()

def create_connection():
    conn = None
    try:
        conn = sqlite3.connect('serve.db')
    except Error as e:
        print(e)

    return conn

def searchname(conn, servercode):
    cur = conn.cursor()
    cur.execute("SELECT * FROM servers WHERE name=?", (servercode,))
    rows = cur.fetchall()
    compcode = ""
    for row in rows:
        compcode = row
    if compcode == servercode:
        return True
    else:
        return False
    
def addData(code, topic):
    cur = conn.cursor()
    cur.execute(f'''INSERT INTO servers
                (name, topic)
                VALUES
                ({code}, {topic})''')
    conn.commit()
    cur.close()
    return True