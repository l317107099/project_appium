import pymysql
import time

class Database():
    def __init__(self):
        # 打开数据库连接
        self.db = pymysql.connect(host="120.79.145.212", user="gs", password="fkuhtxd3", database="meituan",charset='utf8mb4'
                             )
        #
        # 使用 cursor() 方法创建一个游标对象 cursor
        self.table = 'meituan_hotel2'
        self.cursor = self.db.cursor()


    def search_db(self):
        table = 'meituan_hotel2'
        sql = "select * from {table}".format(table=table)
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    #插入更新
    def insert_db(self,data):
        keys = ', '.join(data.keys())
        values = ', '.join(['%s']*len(data))
        sql = "INSERT INTO {table}({keys}) VALUES({values}) ON DUPLICATE KEY UPDATE ".format(table=self.table, keys=keys,values=values)
        update = ",".join(["{key}=%s".format(key=key) for key in data])
        sql += update
        # 丢失重连
        while 1:
            try:
                # 执行sql语句
                self.db.ping(reconnect=True)
                self.cursor.execute(sql,tuple(data.values())*2)
                # 提交到数据库执行
                self.db.commit()
                print("insert success")
                break
            except Exception as e:
                print("fail")
                print(e)
                # 如果发生错误则回滚
                time.sleep(5)
                self.db.rollback()
        self.db.close()

    #更新
    def update_db(self,data):
        sql = "UPDATE {table} SET phone={phone} WHERE poiid={poiid}".format(table=self.table,phone=repr(data["phone"]),poiid=repr(data["poiid"]))
        while 1:
            try:
                # 执行sql语句
                self.db.ping(reconnect=True)
                self.cursor.execute(sql)
                # 提交到数据库执行
                self.db.commit()
                print("update success")
                break
            except Exception as e:
                print(e)
                # 如果发生错误则回滚
                print("fail")
                self.db.rollback()
                time.sleep(2)
        self.db.close()

    #查询phone为空的
    def get_phone(self):
        sql = "SELECT  href FROM  {table} WHERE  id>22410".format(table=self.table)
        try:
            self.cursor.execute(sql)
        except Exception as e:
            print(e)
        return self.cursor.fetchall()


if __name__ == '__main__':
    db = Database()
    # href = db.get_phone()
    # for url in href:
    #     print(url[0])
    # # print(href)
    meituan_list = {}
    meituan_list["addr"] = "adfa"
    # 城市
    meituan_list["area"] = "adsfsaf"
    # hotel id
    meituan_list["poiid"] = "123"
    db.insert_db(meituan_list)





