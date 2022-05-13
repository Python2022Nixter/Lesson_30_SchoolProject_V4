# file names
FOLDER_CSV = "csv"
FOLDER_DATABASE = "database"
FILE_DATABASE = "school.db"
FILE_CSV_PERSONS = "Persons_School_Python.csv"
FILE_CSV_COURSES = "Courses_School_Python.csv"
FILE_CSV_POSITIONS = "Positions_School_Python.csv"
TABLE_NAME_PERSONS = "persons"
TABLE_NAME_COURSES = "courses"
TABLE_NAME_POSITIONS = "positions"

# Colors
SET_RED_FG = "\u001b[38;2;255;0;0m"
SET_BLACK_FG = "\u001b[38;2;0;0;0m"
SET_YELLOW_BG = "\u001b[48;2;255;255;0m"
SET_WHITE_BG = "\u001b[48;2;255;255;255m"
RESET_COLOR = "\u001b[0m"
SET_INFO_MESSAGE_COLOR = "\u001b[38;2;0;255;0m"
SET_GREEN_FG = "\u001b[38;2;0;255;0m"

# SQL queries
SQL_GET_USER_BY_LOGIN = F"""
SELECT * FROM {TABLE_NAME_PERSONS} WHERE login = ? AND password = ?;
"""

SQL_CREATE_TABLE_PERSONS = F"""
CREATE TABLE IF NOT EXISTS "{TABLE_NAME_PERSONS}" (
	"person_id"	INTEGER NOT NULL UNIQUE,
	"first_name"	TEXT,
	"last_name"	TEXT,
	"email"	TEXT,
	"address"	TEXT,
	"tel"	TEXT,
	"salary"	INTEGER,
	"login"	TEXT UNIQUE,
	"password"	TEXT,
	"position_id"	INTEGER,
	"course_id"	INTEGER,
	FOREIGN KEY("position_id") REFERENCES "positions"("position_id"),
	FOREIGN KEY("course_id") REFERENCES "courses"("course_id"),
	PRIMARY KEY("person_id" AUTOINCREMENT)
);

"""
SQL_CREATE_TABLE_COURSES = f"""
CREATE TABLE IF NOT EXISTS "{TABLE_NAME_COURSES}" (
	"course_id"	INTEGER NOT NULL UNIQUE,
	"course_name"	TEXT UNIQUE,
	"syllabus"	TEXT,
	"description"	TEXT,
	PRIMARY KEY("course_id" AUTOINCREMENT)
);
"""
SQL_CREATE_TABLE_POSITIONS = f"""
CREATE TABLE IF NOT EXISTS "{TABLE_NAME_POSITIONS}" (
	"position_id"	INTEGER NOT NULL UNIQUE,
	"position_name"	TEXT,
	"description"	TEXT,
	PRIMARY KEY("position_id" AUTOINCREMENT)
);
"""

SQL_ADD_RECORD_PERSONS = """
INSERT INTO "{TABLE_NAME_PERSONS}" 
("first_name","last_name","email","address","tel","salary","login","password","position_id","course_id") 
VALUES 
(?,?,?,?,?,?,?,?,?,?);"""
SQL_ADD_RECORD_COURSES = """"""
SQL_ADD_RECORD_POSITIONS = """"""


SQL_IMPORT_CSV_PERSONS = F"""
INSERT INTO "{TABLE_NAME_PERSONS}" 
("first_name","last_name","email","address","tel","salary","login","password","position_id","course_id") 
VALUES 
(?,?,?,?,?,?,?,?,?,?);

"""
SQL_IMPORT_CSV_COURSES = f"""
INSERT INTO "{TABLE_NAME_COURSES}" 
("course_name","syllabus","description")
VALUES (?, ?, ?);
"""
SQL_IMPORT_CSV_POSITIONS = f"""
INSERT INTO "{TABLE_NAME_POSITIONS}" 
("position_name","description")
VALUES (?, ?);
"""


SQL_DROP_TABLE_PERSONS = F"""
DROP TABLE IF EXISTS "{TABLE_NAME_PERSONS}"
"""
SQL_DROP_TABLE_POSITIONS = F"""
DROP TABLE IF EXISTS "{TABLE_NAME_POSITIONS}"
"""
SQL_DROP_TABLE_COURSES = F"""
DROP TABLE IF EXISTS "{TABLE_NAME_COURSES}"
"""


# menu items
MENU_ADMIN = (
    "Create table: PERSONS",
    "Add record to table: PERSONS",
    "Import table PERSONS from csv",
    "Drop table: PERSONS\n",
    
    "Create table: POSITIONS",
    "Add record to table: POSITIONS",
    "Import table POSITIONS from csv",
    "Drop table: POSITIONS\n",
    
    "Create table: COURSES",
    "Add record to table: COURSES",
    "Import table COURSES from csv",
    "Drop table: COURSES\n"
    
    
)

MENU_STUDENT = ()
MENU_TEACHER = ()
