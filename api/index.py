from flask import Flask, jsonify, render_template
from flask_cors import CORS, cross_origin
from flask import request
import requests
from time import sleep, time, strftime, localtime
import re
from pymongo import MongoClient

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['JSON_AS_ASCII'] = False

@app.route('/', methods=['GET'] )
@cross_origin(origin='*')
def home():

    ip = requests.get('https://api.ipify.org').content.decode('utf8')
    return ip

@app.route('/checkoder', methods=['POST'] )
@cross_origin(origin='*')
def check_oders():
    oders = request.get_json(force=True)['oders']
    return "hello"

@app.route('/checkoder1', methods=['GET'] )
@cross_origin(origin='*')
def check_oders1():
    oderid = request.args.get('oderid')
    try:
        check = check_oder(oderid)["conversion_status"]
        if check == 1:
          return "đơn đang xử lý"
        if check == 2:
          return "có đơn"
        if check == 3:
          return "đơn bị hủy"
        if check == 4:
          return "chưa thanh toán"
    except:
        return "rớt"

