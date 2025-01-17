import sqlite3
from math import sqrt

### PROCESSING FUNCTIONS ###
def createTable(TABLE_NAME):
    STARTING_CLAYS = [ # Using cone-6 for firing shrinkage, combined with drying shrinkage
                       # List of clays that are added to the program when it's ran the first time
        ("M332", 11.0, 4.0),
        ("M325", 11.5, 5.0),
        ("M340/M340S", 12.0, 2.5),
        ("M350", 12.0, 2.0),
        ("M390", 12.5, 2.0),
        ("M370", 13.0, 1.0),
        ("Polar Ice", 15.0, 0.0),
        ("M340GS", 11.0, 3.0)
    ]
    
    CONNECTION = sqlite3.connect(TABLE_NAME) # This will be repeated many times
    CURSOR = CONNECTION.cursor() # Create SQLite cursor

    CURSOR.execute('''
		CREATE TABLE clays (
			id INTEGER PRIMARY KEY,
			clay_name TEXT NOT NULL,
			shrink_rate REAL NOT NULL,
			absorb_rate REAL NOT NULL
		)
	;''') # Create clay table
    CONNECTION.commit()

    for i in range(len(STARTING_CLAYS)): # Insert data from list into table
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

def getClays(TABLE_NAME): # Retrieve clays from database (used for dropdown menus)
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

def calcShrink(SHRINK_RATE, ABSORB_RATE, DIMENSION): # Calculates shrinkage (calculations explained in documentation)
    PERCENTAGE = 1 - (SHRINK_RATE / 100)
    NEW_DIMENSION = DIMENSION * PERCENTAGE
    return NEW_DIMENSION

def addToTable(TABLE_NAME, CLAY_NAME, SHRINK_RATE, ABSORB_RATE): # Function used in add_clay.py to add the clay to the database
    CONNECTION = sqlite3.connect(TABLE_NAME)
    CURSOR = CONNECTION.cursor()

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
    ;''', (CLAY_NAME, SHRINK_RATE, ABSORB_RATE))
    CONNECTION.commit()

def fetchClay(TABLE_NAME, CLAY_NAME): # Get the ID based on a clay name. This increases security because the ID will always be unique
    CONNECTION = sqlite3.connect(TABLE_NAME)
    CURSOR = CONNECTION.cursor()

    CLAY_INDEX = CURSOR.execute(f'''
        SELECT
            id
        FROM clays
        WHERE
            clay_name = "{CLAY_NAME}"
    ;''').fetchone()
    return int(CLAY_INDEX[0])
def getShrink(TABLE_NAME, ID): # Get shrink ratio from the database for the chosen clay
    CONNECTION = sqlite3.connect(TABLE_NAME)
    CURSOR = CONNECTION.cursor()

    SHRINK_RATE = float(CURSOR.execute(f'''
        SELECT
            shrink_rate
        FROM clays
        WHERE
            id = {ID}
    ;''').fetchone()[0])
    return SHRINK_RATE

def calcShrink(SHRINK_RATE, FINAL_DIMENSION):
    FIRST_DIMENSION = FINAL_DIMENSION / (1 - (SHRINK_RATE / 100))
    return FIRST_DIMENSION

def deleteClay(TABLE_NAME, ID):
    CONNECTION = sqlite3.connect(TABLE_NAME)
    CURSOR = CONNECTION.cursor()

    CURSOR.execute(f'''
        DELETE FROM
            clays
        WHERE
            id = {ID}
    ;''')
    CONNECTION.commit()

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
a {round(DIMENSION, 2)}cm {DIMENSION_NAME}.
'''
    return MESSAGE

if __name__ == "__main__":
    getClays("test.db")
