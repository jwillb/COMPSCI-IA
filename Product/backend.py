import sqlite3
from math import sqrt

### PROCESSING FUNCTIONS ###
def createTable(TABLE_NAME):
    STARTING_CLAYS = [ # Using cone-6 for firing shrinkage, combined with drying shrinkage
        ("M332", 11.0, 4.0),
        ("M325", 11.5, 5.0),
        ("M340/M340S", 12.0, 2.5),
        ("M350", 12.0, 2.0),
        ("M390", 12.5, 2.0),
        ("M370", 13.0, 1.0),
        ("Polar Ice", 15.0, 0.0),
        ("M340GS", 11.0, 3.0)
    ]
    
    CONNECTION = sqlite3.connect(TABLE_NAME)
    CURSOR = CONNECTION.cursor()

    CURSOR.execute('''
		CREATE TABLE clays (
			id INTEGER PRIMARY KEY,
			clay_name TEXT NOT NULL,
			shrink_rate REAL NOT NULL,
			absorb_rate REAL NOT NULL
		)
	;''')
    CONNECTION.commit()

    for i in range(len(STARTING_CLAYS)):
        CURSOR.execute('''
            INSERT INTO
                clays (
                    clay_name,
                    shrink_rate,
                    absorb_rate
                )
            VALUES (
                ?,?,?
            )
        ;''', STARTING_CLAYS[i])
        CONNECTION.commit()

def getClays(TABLE_NAME):
    CONNECTION = sqlite3.connect(TABLE_NAME)
    CURSOR = CONNECTION.cursor()

    CLAY_TUPLES = CURSOR.execute('''
        SELECT
            clay_name
        FROM clays
    ;''').fetchall()
    
    CLAY_LIST = []

    for i in range(len(CLAY_TUPLES)):
        CLAY_LIST.append(CLAY_TUPLES[i][0])
    return CLAY_LIST

def calcShrink():
    pass

### OUTPUT FUNCTIONS ###
def genText(DIMENSION, FINAL_DIMENSION, SHAPE, SHRINK_RATE):
    if SHAPE == 1:
        DIMENSION_NAME = "circumference"
    else:
        DIMENSION_NAME = "side length"

    MESSAGE = f'''
Your clay will shrink by {SHRINK_RATE}%,
so to achieve your final {DIMENSION_NAME} of
{FINAL_DIMENSION}cm, you will need to give your object
a {DIMENSION}cm {DIMENSION_NAME}.
'''
    return MESSAGE

if __name__ == "__main__":
    getClays("test.db")
