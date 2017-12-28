from database_connect import connection

def createTables():
    try:
        query = "CREATE TABLE userdata (userid int not null auto_increment, username varchar(32) not null, last_name varchar(32) not null, first_name varchar(32) not null)"
        connection.cursor().execute(query)
        connection.commit()
    finally:
        connection.close()

def addUser(username,last_name,first_name):
    try:
        query = "INSERT into userdata (username, last_name, first_name) values (%s, %s, %s)"
        connection.cursor().execute(query,(username,last_name,first_name))
        connection.commit()
    finally:
        connection.close()

if __name__ == '__main__':
    createTables()


