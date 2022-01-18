import sqlite3
from math import sqrt

### PROCESSING FUNCTIONS ###
def createTable(TABLE_NAME):
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

	CURSOR.execute('''
		INSERT INTO
			clays (
				clay_name,
				shrink_rate,
				absorb_rate
			)
		VALUES (
			"M332",
			11,
			4
		)
	;''')
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
	print(genText(15, 12, 1, 20))
