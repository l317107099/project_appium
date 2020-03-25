import pymysql


class Database():
    def __init__(self):
        # 打开数据库连接
        self.db = pymysql.connect(host="120.79.145.212", user="gs", password="fkuhtxd3", database="meituan",
                             db="meituan_product")
        #
        # 使用 cursor() 方法创建一个游标对象 cursor
        self.cursor = self.db.cursor()

    def insert_db(self,data):

        # 使用 execute()  方法执行 SQL 查询
        # cursor.execute("SELECT VERSION()")

        # 使用 fetchone() 方法获取单条数据.
        # data = cursor.fetchone()

        # print("Database version : %s " % data)
        #
        print(type(data['title']))
        sql = "INSERT INTO meituan_product(%s,%s,%s,%s,%s,%s) VALUES(%s,%s,%s,%s,%s,%s)" %('title',"avgscore","commit","price","phone","address",repr(data["title"]),repr(data["avgScore"]),repr(data["commit"]),repr(data["price"]),repr(data["phone"]),repr(data["address"]))

        sql += "ON DUPLICATE KEY UPDATE %s=%s,%s=%s,%s=%s,%s=%s,%s=%s,%s=%s"%("title",repr(data["title"]),"avgscore",repr(data["avgScore"]),"commit",repr(data["commit"]),"price",repr(data["price"]),"phone",repr(data["phone"]),"address",repr(data["address"]))
        print(sql)
        # 丢失重连
        while 1:
            try:
                # 执行sql语句
                self.db.ping(reconnect=True)
                self.cursor.execute(sql)
                # 提交到数据库执行
                self.db.commit()
                print("insert success")
                break
            except Exception as e:
                print(e)
                # 如果发生错误则回滚
                print("fail")
                self.db.rollback()
        #
        # # 关闭数据库连接
        self.db.close()

if __name__ == '__main__':
    db = Database()
    data = {'title': '大众蛋糕屋（玉潭中路店）', 'avgScore': 5, 'commit': 842, 'price': 35, 'phone': '15084885221/13055162221',"address":"宁乡县玉潭中路101号（益丰大药房东行40米）"}
    db.insert_db(data)