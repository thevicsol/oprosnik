import sqlite3

db = sqlite3.connect('form.db')
cur = db.cursor()
cur.execute(
    """CREATE TABLE answers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    q1` INTEGER,
    q2` INTEGER,
    q3` INTEGER,
    q4` INTEGER,
    q5` INTEGER,
    q6` INTEGER,
    q7` INTEGER,
    q8` INTEGER,
    q9` INTEGER,
    q10` INTEGER,
    q11` INTEGER,
    q12` INTEGER,
    q13` INTEGER,
    q14` INTEGER,
    q15` INTEGER,
    q16` INTEGER,
    q17` INTEGER,
    q18` INTEGER,
    q19` INTEGER,
    q20` INTEGER,
    q21` INTEGER,
    q22` INTEGER,
    q23` INTEGER,
    q24` INTEGER,
    q25` INTEGER,
    q26` INTEGER,
    q27` INTEGER,
    q28` INTEGER,
    q29` INTEGER,
    q30` INTEGER,
    q31` INTEGER,
    q32` INTEGER,
    q33` INTEGER,
    q34` INTEGER,
    q35` INTEGER,
    q36` INTEGER,
    q37` INTEGER,
    q38` INTEGER,
    q39` INTEGER,
    q40` INTEGER,
    q41` INTEGER,
    q42` INTEGER )
    """)

cur.execute(
    """CREATE TABLE 
    user ( 
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    gender TEXT,
    education TEXT,
    age INTEGER,
    english TEXT,
    langs TEXT,
    social TEXT,
    transport TEXT,
    picid INTEGER )
    """)

db.commit()
