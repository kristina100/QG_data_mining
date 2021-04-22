import pymysql.cursors


# 用来操作数据库的类
class MySqlCommand:
    # 类的初始化
    def __init__(self):
        # 光标
        self.host = "localhost"
        self.port = 3306
        # 用户名
        self.user = "root"
        # 密码
        self.password = "Annie19900919"
        # 数据库名称
        self.db = "test01"
        # 表名
        self.table = "user"
        self.conn = pymysql.connect(host=self.host, port=self.port, user=self.user,
                                    password=self.password, db=self.db, charset='utf8')
        self.cursor = self.conn.cursor()

    # 连接数据库
    def connectMySql(self):
        try:
            return self.cursor, self.conn
        except:
            print('Connect mysql error.')


def insert_movies(movies):
    """

    :type movie: object
    :param movie:
    :type movies: object
    """
    # 需要先对MySqlCommand初始化
    cursor, db = MySqlCommand().connectMySql()
    # 用于向表中插入新记录
    sql = """INSERT INTO user (movie_id, name, content, actor, date, country, types,
    rate, com_count, quote, url0, introduction) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
    try:
        # 这里的参数直接写sql语句！！！
        cursor.executemany(sql, movies)
        # 提交到数据库执行
        db.commit()
    except pymysql.Error:
        # 发生错误
        db.rollback()
    finally:
        cursor.close()
        db.close()
