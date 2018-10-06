import pymysql

db = pymysql.connect("192.168.0.101", "root", "sunck", "kaige")
cursor = db.cursor()

# 检查表是否存在，如果存则删除
cursor.execute("drop table if exists bandcard")
#建表
sql = 'create table bandcard(id int auto_increment primary key, money int not null)'
cursor.execute(sql)


cursor.close()
db.close()

