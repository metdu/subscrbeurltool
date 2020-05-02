import os
import sys

BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE_PATH)
from lib.interface import server
from conf.setting import SERVER_PORT

server.run(host='0.0.0.0', port=SERVER_PORT, debug=True)
