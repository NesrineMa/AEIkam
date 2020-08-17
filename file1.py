import mysql.connector

# BD connection

"""
mycursor.execute("desc profil")
print([column[0] for column in mycursor.fetchall()])
"""

def insertVariblesIntoTable(nom,id):
    try:      # BD connection

        mydb = mysql.connector.connect(host='localhost',
                                        database='test',
                                        user='nesrine',
                                        password='aei321')
        cursor = mydb.cursor()
        # create query
        mysql_insert_query = """ INSERT INTO profil ( nom,id)
         VALUES (%s, %s) """

        recordtuple = (nom,id)
        cursor.execute(mysql_insert_query, recordtuple)
        mydb.commit()
        print("Record inserted successfully into Laptop table")

    except mysql.connector.Error as error:
        print("Failed to insert into MySQL table {}".format(error))
    finally:
        if (mydb.is_connected()):
            cursor.close()
            mydb.close()
            print("MySQL connection is closed")


insertVariblesIntoTable('ABDENNADHER DESIGN', 102)
# insertVariblesIntoTable(3, 'MacBook Pro', 2499, '2019-06-20')

