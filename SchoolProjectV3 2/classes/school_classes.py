import os
import pathlib
import sqlite3
import classes.school_constants as c


class Person():  
    
    def __init__(self, person_data: tuple[str]) -> None:  #  Person(res[0])
        # 
        self.person_id = int(person_data[0])
        self.first_name = person_data[1]
        self.last_name = person_data[2]
        self.email = person_data[3]
        self.address = person_data[4]
        self.tel = person_data[5]
        self.salary = float(person_data[6])
        self.login = person_data[7]
        self.password = person_data[8]
        self.position_id = int(person_data[9])
        self.course_id = int(person_data[10])
        pass
    
    def __str__(self) -> str:
        out_string = "Person: "
        out_string += F"id: {self.person_id} "
        out_string += F"name: {self.first_name} "
        out_string += F"last name: {self.last_name} "
        out_string += F"email: {self.email} "
        out_string += F"address: {self.address} "
        out_string += F"tel: {self.tel} "
        out_string += F"salary: {self.salary} "
        out_string += F"login: {self.login} "
        out_string += F"password: {self.password} "
        out_string += F"position id: {self.position_id} "
        out_string += F"course id: {self.course_id} "
        
        return out_string
    
    pass


class School:
    __default_admin = Person((0,"","","","","",0.0,"","",5,0))
    def __init__(self) -> None:
        self.PATH_TO_FILE_DATABASE = pathlib.Path(__file__).parent.parent.joinpath(c.FOLDER_DATABASE).joinpath(c.FILE_DATABASE)
        self.PATH_TO_CSV_PERSONS = pathlib.Path(__file__).parent.parent.joinpath(c.FOLDER_CSV).joinpath(c.FILE_CSV_PERSONS)
        self.PATH_TO_CSV_COURSES = pathlib.Path(__file__).parent.parent.joinpath(c.FOLDER_CSV).joinpath(c.FILE_CSV_COURSES)
        self.PATH_TO_CSV_POSITIONS = pathlib.Path(__file__).parent.parent.joinpath(c.FOLDER_CSV).joinpath(c.FILE_CSV_POSITIONS)
        pass
    
    def start(self):
        self.__login()
        pass
    
    def __login(self):
        # while - incorrect input
        # input name / passw
        # __check_user_credentials()
        # SET bg red color
        # os.system("\n")
        # print ("\u001b[93m")
        print ("User login")
        
        # Check if PERSONS table exists
        # handle error: sqlite3.OperationalError: no such table: 
        try:
            while True:
                user_name = input("Enter login name: ")
                user_password = input("Enter password: ")
                # query database
                with sqlite3.connect(self.PATH_TO_FILE_DATABASE) as conn:
                    cursor = conn.cursor() # Create cursor object to operate with DB
                    res = cursor.execute(c.SQL_GET_USER_BY_LOGIN, 
                                        (user_name, user_password)
                                        ).fetchall()  # Method chainig: 1. call a = cursor.execute(),  2 res =  a.fetchall()
                    print (F"Query result: \n {res}\n") # list of tuples" [(result row1), (result row2)]
                    if len(res) != 0 :
                        self.__registered_user = Person(res[0]) # call class constructor: pass tuple with single user data to class constructor
                        
                        break
                    print ("Incorrect user credentials, try again")
                    pass # END SQL
                pass # END input loop
        except sqlite3.OperationalError as err:
            print ("Persons database not detected, default admin loaded")
            self.__registered_user = School.__default_admin            
            pass 
        
        
        print (F"Welcome, user:\n{self.__registered_user.__str__()}")
        self.__process_menu()
        pass
     
    def __process_menu(self):        
        # Display menu
        match self.__registered_user.position_id:
            case 1:
                # Teacher detected (self.__registered_user.position_id = 1)
                
                pass
            case 2:
                # Sales person detected (self.__registered_user.position_id = 2)
                
                pass
            case 3:
                # Student detected
                
                pass
            case 4:
                # educationManager detected
                
                pass
            case 5:
                # Administrator detected (self.__registered_user.position_id = 5)
                # create menu text string
                
                # START - creating menu string 
                menu_string = "Administrator menu: \n"
                menu_string += F"press {0} to EXIT\n"
                for i in range(len(c.MENU_ADMIN)):
                    menu_string += F"press {i+1} to {c.MENU_ADMIN[i]}\n"
                    pass
                # END - creating menu string 
                
                while True:
                    match input(menu_string):
                        case "0":
                            # EXIT
                            break
                        # Manage PESONS
                        case "1":
                            # Create table: PERSONS
                            self.__create_table(c.SQL_CREATE_TABLE_PERSONS)
                            pass
                        case "2":
                            # Add record to table: PERSONS
                            self.__add_table_record(c.SQL_ADD_RECORD_PERSONS)
                            pass
                        case "3":
                            # Import table PERSONS from csv
                            self.__import_from_csv(self.PATH_TO_CSV_PERSONS, c.SQL_IMPORT_CSV_PERSONS)
                            pass
                        case "4":
                            # Drop table: PERSONS
                            self.__drop_table(c.SQL_DROP_TABLE_PERSONS)
                            
                            pass
                        
                        # Manage POSITIONS table 
                        case "5":
                            # Create table: POSITIONS
                            self.__create_table(c.SQL_CREATE_TABLE_POSITIONS)
                            pass
                        case "6":
                            # Add record to table: POSITIONS
                            self.__add_table_record(c.SQL_ADD_RECORD_POSITIONS)
                            pass
                        case "7":
                            # Import table POSITIONS from csv
                            self.__import_from_csv(self.PATH_TO_CSV_POSITIONS, c.SQL_IMPORT_CSV_POSITIONS)
                            pass
                        case "8":
                            # Drop table: POSITIONS
                            self.__drop_table(c.SQL_DROP_TABLE_POSITIONS)
                            
                            pass
                        
                        # Manage courses table 
                        case "9":
                            # Create table: COURSES
                            self.__create_table(c.SQL_CREATE_TABLE_COURSES)
                            pass
                        case "10":
                            # Add record to table: COURSES
                            self.__add_table_record(c.SQL_ADD_RECORD_COURSES)
                            pass
                        case "11":
                            # Import table COURSES from csv
                            self.__import_from_csv(self.PATH_TO_CSV_COURSES, c.SQL_IMPORT_CSV_COURSES)
                            pass
                        case "12":
                            # Drop table: COURSES
                            self.__drop_table(c.SQL_DROP_TABLE_COURSES)
                            
                            pass
 
                        case _:
                            print ("Incorrect input")

                            pass
                    
                
                
                pass
            
        # end match block

        
        
        pass
    
    def __import_from_csv (self, path_to_csv: str, sql: str):
        
        # read from file
        with open(path_to_csv) as f:
            headers_from_file = f.readline()
            rows_from_file = f.readlines()            
            pass
        print (len(list_from_file))
        print (rows_from_file[0])
        print (rows_from_file[1])
        print (rows_from_file[2])
        
        # create values list
        
        values_list = []
        for n_row in rows_from_file: values_list.append(n_row.strip().split(","))
        
        try:
            with sqlite3.connect(self.PATH_TO_FILE_DATABASE) as conn:
                cursor = conn.cursor()
                cursor.executemany(sql, rows_from_file)
        
        pass
    
    def __add_table_record(self, sql: str):
        
        
        pass
    
    def __create_table(self, sql: str):
        print(F"[__create_table(self, sql: str) - SQL query:\n{sql} ]")
        with sqlite3.connect(self.PATH_TO_FILE_DATABASE) as conn:
            cursor = conn.cursor()
            res = cursor.execute(sql)
            pass # END SQL
        pass
    
    def __drop_table(self, sql: str):
        print(F"[__drop_table(self, sql: str) - SQL query:\n{sql} ]")
        with sqlite3.connect(self.PATH_TO_FILE_DATABASE) as conn:
            cursor = conn.cursor()
            res = cursor.execute(sql)
            pass # END SQL
        pass
    
    def __menu_admin():
        # read menu items
        
        
        # display menu
        
        
        # process menu selection
        
        
        pass
    
    def __menu_sales():
        
        
        pass
    
    
    def create_tables():
        
        
        pass
    
    
    
    
    
    pass

class Person():  
    
    def __init__(self, person_data: tuple[str]) -> None:  #  Person(res[0])
        # 
        self.person_id = int(person_data[0])
        self.first_name = person_data[1]
        self.last_name = person_data[2]
        self.email = person_data[3]
        self.address = person_data[4]
        self.tel = person_data[5]
        self.salary = float(person_data[6])
        self.login = person_data[7]
        self.password = person_data[8]
        self.position_id = int(person_data[9])
        self.course_id = int(person_data[10])
        pass
    
    def __str__(self) -> str:
        out_string = "Person: "
        out_string += F"id: {self.person_id} "
        out_string += F"name: {self.first_name} "
        out_string += F"last name: {self.last_name} "
        out_string += F"email: {self.email} "
        out_string += F"address: {self.address} "
        out_string += F"tel: {self.tel} "
        out_string += F"salary: {self.salary} "
        out_string += F"login: {self.login} "
        out_string += F"password: {self.password} "
        out_string += F"position id: {self.position_id} "
        out_string += F"course id: {self.course_id} "
        
        return out_string
    
    pass