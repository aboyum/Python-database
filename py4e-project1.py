import sqlite3

# Make a database and make 5 colums. 4 integer and one autoincrement
conn = sqlite3.connect('amis.sqlite')
cur = conn.cursor()

# cur.execute('DROP TABLE IF EXISTS Amis')

cur.executescript('''
DROP TABLE IF EXISTS Amis;

CREATE TABLE Amis (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    speed INTEGER,
    period INTEGER,
    warning INTEGER,
    pair INTEGER
);
''')

linenumber = 0
# Open csv file and use colum 2,3,4 and 5
fhand = open('amis.csv')
for line in fhand:
    words = line.rstrip()
    words2 = words.split(",")
    if linenumber == 0:
        linenumber = linenumber + 1
        continue
    else:
        speed = words2[1]
        period = words2[2]
        warning = words2[3]
        pair = words2[4]

        if speed is None or period is None or warning is None or pair is None: 
            continue
        # print(speed, period, warning, pair)
        # Insert data into database
        cur.execute('''INSERT OR IGNORE INTO Amis 
        (speed, period, warning, pair) 
        VALUES ( ?, ?, ?, ? )''', ( speed, period, warning, pair) )
conn.commit()
print('*************FERDIG****************')

# Find info in the database

conn = sqlite3.connect('amis.sqlite')
cur = conn.cursor()
cur.execute("SELECT * FROM Amis")
 
rows = cur.fetchall()
 
# for row in rows:
#    print(row)


#########################visulize###############

from matplotlib import pyplot as plt
    
#Plot Data
fig = plt.figure(dpi = 128, figsize = (10,6))
plt.plot(highs, c = 'red') #Line 1
#Format Plot
plt.title("Speed", fontsize = 24)
plt.xlabel('Speed',fontsize = 16)
plt.ylabel("Period", fontsize = 16)
plt.tick_params(axis = 'both', which = 'major' , labelsize = 16)
plt.show()