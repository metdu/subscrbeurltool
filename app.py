from flask import Flask
import os,sys
BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,BASE_PATH)
#from lib.interface import server
from conf.setting import SERVER_PORT
from  lib.subscribe import sub_se
from lib.mysql_util import conn_mysql

mysqlsesson = conn_mysql()


sub_se.run(host='0.0.0.0',port=SERVER_PORT,debug=True)
#app = Flask(__name__)


#@app.route('/')
#def hello_world():
#    return 'Hello World!'


#if __name__ == '__main__':
#    app.run()
