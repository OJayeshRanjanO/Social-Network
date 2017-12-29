import pymysql.cursors


def dbConnect():
    return pymysql.connect(host='localhost',
                    user='root',
                    passwd='root',
                    db='social_network',
                    cursorclass=pymysql.cursors.DictCursor)