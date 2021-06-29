import mysql.connector

def ConnectorMysql():

    mydb = mysql.connector.connect(
            host="",
            user="",
            passwd="",
            database="",
            auth_plugin='mysql_native_password'
    )
    return mydb

def get_data(_id):
    mydb = ConnectorMysql()
    mycursor = mydb.cursor()
    sql = "SELECT * FROM user WHERE id='{}'; ".format(_id)
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    if len(myresult) > 0: 
        for x in myresult:
            arr = {
                "_id" : x[0],
                "name" : x[1],
                "age" : int(x[2]),
                "address" : x[3]
                }
    return arr

def insert_data(name  , age , address):
    mydb = ConnectorMysql()
    mycursor = mydb.cursor()
    sql = "INSERT INTO user (name,age,address) VALUES (%s ,%s, %s)"
    val = (name , age , address)
    mycursor.execute(sql,val)
    mydb.commit()
    mycursor.close()
    mydb.close()
    

def update_data(_id ,name  , age , address):
    mydb = ConnectorMysql()
    mycursor = mydb.cursor()
    sql = "UPDATE user SET  name=%s , age=%s , address=%s  WHERE id=%s"
    val = (name , age , address , _id)
    mycursor.execute(sql,val)
    mydb.commit()
    mycursor.close()
    mydb.close()


def delete_data(_id):
    mydb = ConnectorMysql()
    mycursor = mydb.cursor()
    sql = "DELETE  FROM user WHERE id={}".format(_id)
    mycursor.execute(sql)
    mydb.commit()
    mycursor.close()
    mydb.close()



