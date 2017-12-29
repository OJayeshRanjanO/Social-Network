from database_connect import dbConnect

def __createTables():
    try:
        connection = dbConnect()
        query = """CREATE TABLE userdata (
            userid int primary key auto_increment, 
            role varchar(32) not null, 
            username varchar(32) not null, 
            password varchar(32) not null, 
            last_name varchar(32) not null, 
            first_name varchar(32) not null
        )"""
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
    finally:
        connection.close()

def addUser(username, password,role,last_name,first_name):
    try:
        connection = dbConnect()
        query = "SELECT * FROM userdata where username = %s"
        cursor = connection.cursor()
        cursor.execute(query,(username,password))
        data = cursor.fetchall()
        if len(data) == 0:
            pass
        else:
            connection.close()
            return False

        query = "INSERT into userdata (username, password, role, last_name, first_name) values (%s, %s, %s, %s, %s)"
        cursor = connection.cursor()
        cursor.execute(query,(username,password,role,last_name,first_name))
        connection.commit()
        connection.close()
        return True
    except:
        connection.close()
        return False

def checkUserPresent(username,password):
    try:
        connection = dbConnect()
        query = "SELECT * FROM userdata where username = %s AND password = %s"
        cursor = connection.cursor()
        cursor.execute(query,(username,password))
        data = cursor.fetchall()
        return False if len(data) == 0 else True
    except:
        connection.close()
        return False

if __name__ == '__main__':
    __createTables()


