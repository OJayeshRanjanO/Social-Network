from database_connect import dbConnect


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

def addCircle(circle_name,circle_type, userid):
    try:
        connection = dbConnect()
        query = "INSERT into circle_data (circle_name, circle_type, userid) values (\""+str(circle_name)+"\", \""+str(circle_type)+"\", "+str(userid)+")"
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        connection.close()
        circles = getCircles(userid)
        return (circles)[len(circles)-1]
    except:
        print("Something went wrong in addCircle")

def removeCircle(circleid):
    try:
        connection = dbConnect()
        query = "DELETE FROM circle_data WHERE circleid = " + str(circleid)
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        connection.close()
    except:
        print("Something went wrong in deleteCircle")


#RELOAD PAGE FUNCTIONS
def getUserID(username):
    try:
        connection = dbConnect()
        query = "SELECT userid FROM userdata where username = %s"
        cursor = connection.cursor()
        cursor.execute(query,(username,))
        data = cursor.fetchall()
        connection.close()
        return data[0]
    except:
        print("Something went wrong in getUserID")

def getCircles(userid):
    try:
        connection = dbConnect()
        query = "SELECT * FROM circle_data where userid = "+str(userid)
        cursor = connection.cursor()
        cursor.execute(query)
        data = cursor.fetchall()
        return data
    except:
        print("Something went wrong in getCircles")