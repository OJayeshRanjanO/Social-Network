import pymysql.cursors


def dbConnect():
    return pymysql.connect(host='localhost',
                    user='root',
                    passwd='root',
                    db='social_network',
                    cursorclass=pymysql.cursors.DictCursor)

def __createCustomerTable():
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

def __circleDataTable():
    try:
        connection = dbConnect()
        query = """CREATE TABLE circle_data (
            circleid int primary key auto_increment, 
            circle_name varchar(255) not null,
            circle_type varchar(32) not null,
            userid int not null
        )"""
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
    finally:
        connection.close()

def __pageDataTable():
    try:
        connection = dbConnect()
        query = """CREATE TABLE page_data (
            pageid int primary key auto_increment, 
            post_count int not null,
            circle_id int not null
        )"""
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
    finally:
        connection.close()

def __postsDataTable():
    try:
        connection = dbConnect()
        query = """CREATE TABLE post_data (
            postid int primary key auto_increment, 
            date date not null,
            content text not null,
            comment_count int not null,
            pageid int not null
        )"""
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
    finally:
        connection.close()

def __commentsDataTable():
    try:
        connection = dbConnect()
        query = """CREATE TABLE comment_data (
            commentid int primary key auto_increment, 
            date date not null,
            content text not null,
            userid int not null,
            postid int not null
        )"""
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
    finally:
        connection.close()

# if __name__ == '__main__':
#     __circleDataTable()
    # try:
    #     # __postsDataTable()
    #     # __commentsDataTable()
    # except:
    #     print("Table exists already")


