import sqlite3
conn = sqlite3.connect('tk.db')
print("Opened database successfully")
cur = conn.cursor()
try:
    cur.execute('''CREATE TABLE tk_table(user_id integer primary key autoincrement,user_name varchar(20), 
                    user_score DECIMAL(3,1), user_time datetime)''')
    for i in range(1, 50):
        cur.execute("insert into tk_table (user_id, user_name, user_score, user_time) values(NULL, \
                    '张三', 50.2+%s, datetime('now'))" %(i, ))
        conn.commit()
except sqlite3.OperationalError:
    print('数据库已创建')
"""这个文件的作用是用于筛选数据，需要的数据格式被调用？"""


def menu(self):
    a = {
        1: '姓名',
        2: '分数',
        3: '时间'
        }
    return a[self]


class Sleep(object):

    def display(id, score):
        a = cur.execute("select * from tk_table where user_id=%s" % id).fetchone()
        conn.commit()
        try:
            return a[score]
        except TypeError:
            return 'None'

    def delete(id):
        cur.execute("delete from tk_table where user_id=%s" % (id))
        conn.commit()

    def add(name, score, time):
        cur.execute("insert into tk_table (user_id,user_name,user_score,user_time)values(NULL,'%s', %s, datetime('now'))" % (name, score))
        conn.commit()
        for tt in cur.execute("select * from tk_table where user_name='%s' and user_score =%s" % (name, score)).fetchone():
            conn.commit()
            return tt

    def update(name, score, data):
        u = cur.execute("update tk_table set user_name='%s',user_score=%s,user_time=datetime('now') where user_id = %s"
                        % (name, score, data))
        conn.commit()

    def count(self):
        for i in cur.execute("select count(*) from tk_table"):
            y = (i[0]//10)+1
            return y

    def select(name):
        pi = []
        try:
            for tt in cur.execute("select * from tk_table where user_name='%s'" % (name,)).fetchall():
                conn.commit()
                pi.append(tt)
            if pi:
                return pi
        except TypeError:
            return '没有找到数据'