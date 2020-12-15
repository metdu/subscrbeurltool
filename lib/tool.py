'''from conf.setting import MYSQL_HOST,MYSQL_PORT,SQL_DB,SALT,MYRDS_HOST,MYRDS_PORT,RDS_DB,MYSQL_USER,MYSQL_PWD

def md5_passwd(str):
    str=str+SALT
    import hashlib
    md = hashlib.md5()
    md.update(str.encode())
    res = md.hexdigest()
    return res.upper()

def conn_mysql(sql):
    import pymysql
    conn = pymysql.connect(host=MYSQL_HOST,user =MYSQL_USER,password =MYSQL_PWD,db=SQL_DB,charset='utf8',port=MYSQL_PORT)
    cur = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cur.execute(sql)
    res = cur.fetchall()
    conn.commit()
    cur.close()
    conn.close()
    return res
'''


def my_json(dic):
    import json
    return json.dumps(dic,ensure_ascii=False)