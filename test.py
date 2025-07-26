import mysql.connector
mycon=mysql.connector.connect(host='localhost',user='root',passwd='asher123',database='dealer_service')
mycur=mycon.cursor()
mycur.execute("SELECT Purchase_no FROM car_purchase ORDER BY Purchase_no DESC LIMIT 1")
last_row = mycur.fetchone()
a=int(last_row[0])+1
print(type(a))