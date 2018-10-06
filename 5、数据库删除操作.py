import pymysql

db = pymysql.connect("192.168.0.101", "root", "sunck", "kaige")
cursor = db.cursor()



sql = 'delete from bandcard where money = 400'
try:
    cursor.execute(sql)
    db.commit()
except:
    # 如果提交失败，回滚到上一次数据
    db.rollback()


cursor.close()
db.close()

