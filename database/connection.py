import mysql.connector 

conectar =  mysql.connector.connect(user = 'root', 
                                    password = 'JuanEstebanRiveroRoche',
                                    host = 'localhost', 
                                    database ='user',
                                    port = '3306')
print(conectar)