# coding: utf-8
from flask import Flask, render_template,request
app = Flask(__name__)

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("C:/Users/loot shirakagi/Desktop/yugioh regu key/my-ragulation-ygo-firebase-adminsdk-f6nlg-db192fde04.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://my-ragulation-ygo.firebaseio.com',
    'databaseAuthVariableOverride': {
        'uid': 'my-service-worker'
    }
})

ref = db.reference('Warrior')
 
@app.route('/')
def hello():
    hello = (ref.get())
    return hello

@app.route("/index") #アプリケーション/indexにアクセスが合った場合
def index():
    message = (db.reference('/W00001').get())
    my_dic = {}
    my_dic['name']='hermes'
    my_dic['deck']='power of unity'
    return render_template('index.html',message=message,Dictionary=my_dic)

@app.route('/index',methods=['POST'])
def post():
    name = request.form.get('name')
    message = (db.reference(name).get())
    return render_template('index.html',
                           message = message)
#/indexにアクセスが来たらtemplates内のindex.htmlが開きます
#ここがサーバーサイドからクライアントサイドへなにかを渡すときのポイントになります。
 
if __name__ == "__main__":
    app.run()
