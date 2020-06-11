import flask
from lib.tool import conn_mysql, md5_passwd, my_json
from conf.setting import MYRDS_HOST, MYRDS_PORT, RDS_DB
from flask import request
from data.msg import NOT_NULL

server = flask.Flask(__name__)
import redis
from urllib import parse
import base64
import ast

@server.route('/login', methods=['post'])
def login():
    username = request.json.get("username")
    password = request.json.get("password")
    password = md5_passwd(password)
    if username and password:
        r1 = redis.Redis(host=MYRDS_HOST, port=MYRDS_PORT, password='123456', db=RDS_DB)
        keys = r1.keys()
        if username.encode() in keys:
            return '{"msg": "你已经登录", "code": 800}'
        else:
            sql = 'select id,username,password from user where username ="%s";' % username
            res = conn_mysql(sql)
            if not res:
                return '{code":200,"msg":"用户名不存在}'
            elif res['password'] == password:
                r1.setex(username, 1, 1000)
                return '{"code":200,"msg":"登录成功"}'
            else:
                return '{"code":400,"msg":"密码输入错误"}'
    else:
        return my_json(NOT_NULL)


@server.route('/logout', methods=['GET', 'POST'])
def logout():
    url = 'https://www.google.com/search?newwindow=1&biw=1091&bih=763'

    params = parse.parse_qs(parse.urlparse(url).query)

    params['newwindow']

    print(params['bih'])
    return "heheheh"


@server.route('/netlify/<setting_id>', methods=['GET', 'POST'])
def subscribe(setting_id):
    sql = 'select user_type,user_status from fq_users where user_url ="%s";' % setting_id
    res = conn_mysql(sql)
    shuchu = ''
    if not res:
        return '{code":200,"msg":"用户不存在}'
    elif res[0]['user_type'] == '0':
        sql = "select *from fq_url  a where a.url_status in ('0','1','2')"
        res = conn_mysql(sql)
        for fqurl in res:
            shuchu=shuchu+(fqurl['url'])+'\n'
    elif res[0]['user_type'] == '1':
        sql = "select *from fq_url  a where a.url_status in ('1','2')"
        res = conn_mysql(sql)
        for fqurl in res:
            shuchu=shuchu+(fqurl['url'])+'\n'
    elif res[0]['user_type'] == '2':
        sql = "select *from fq_url  a where a.url_status in ('2')"
        res = conn_mysql(sql)
        for fqurl in res:
            shuchu=shuchu+(fqurl['url'])+'\n'
    else:
        return '{"code":400,"msg":"密码输入错误"}'
    encodestr = base64.b64encode(shuchu.encode('utf-8'))
    print(str(encodestr, 'utf-8'))
    return str(encodestr, 'utf-8')

@server.route('/quantumultx/<setting_id>', methods=['GET', 'POST'])
def subscribeqx(setting_id):
    sql = 'select user_type,user_status from fq_users where user_url ="%s";' % setting_id
    res = conn_mysql(sql)
    shuchu = ''
    if not res:
        return '{code":200,"msg":"用户不存在}'
    elif res[0]['user_type'] == '0':
        sql = "select *from fq_url  a where a.url_status in ('0','1','2')"
        res = conn_mysql(sql)
    elif res[0]['user_type'] == '1':
        sql = "select *from fq_url  a where a.url_status in ('1','2')"
        res = conn_mysql(sql)
    elif res[0]['user_type'] == '2':
        sql = "select *from fq_url  a where a.url_status in ('2')"
        res = conn_mysql(sql)
    else:
        return '{"code":400,"msg":"密码输入错误"}'
    for datares in res:
        data = datares['url'].replace("vmess://", "")
        str_url = base64.b64decode(data).decode("utf-8")
        url_dict = ast.literal_eval(str_url)
        openurl = "vmess=" + url_dict.get("add") + ":" + url_dict.get("port") + ", method=chacha20-ietf-poly1305, password="\
                  + url_dict.get("id") + ", obfs="+ url_dict.get("net") + ", obfs-uri=" + url_dict.get("path")\
                  + ",fast-open=false, udp-relay=false, tag=" + url_dict.get("ps")
        shuchu = shuchu + openurl+"\n"
    encodestr = base64.b64encode(shuchu.encode('utf-8'))
    print(str(encodestr, 'utf-8'))
    return str(encodestr, 'utf-8')


@server.route('/<setting_id>', methods=['GET', 'POST'])
def subscriberoot(setting_id):
    sql = 'select * from fq_users where user_url ="%s";' % setting_id
    res = conn_mysql(sql)
    shuchu = ''
    if not res:
        return '{code":200,"msg":"用户不存在}'
    else:
        shuchu = res[0]['fq_text']
    encodestr = base64.b64encode(shuchu.encode('utf-8'))
    print(str(encodestr, 'utf-8'))
    return str(encodestr, 'utf-8')


@server.route('/commitlogs', methods=['GET', 'POST'])
def getcommitlogs():
    file_object = open('/var/local/gitlog')
    # 不要把open放在try中，以防止打开失败，那么就不用关闭了
    try:
        file_context = file_object.read()
        # file_context是一个string，读取完后，就失去了对test.txt的文件引用
        #  file_context = open(file).read().splitlines()
        # file_context是一个list，每行文本内容是list中的一个元素
    finally:
        file_object.close()
    # 除了以上方法，也可用with、contextlib都可以打开文件，且自动关闭文件，
    # 以防止打开的文件对象未关闭而占用内存
    return file_context