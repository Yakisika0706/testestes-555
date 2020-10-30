from flask import Flask
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

ref = db.reference()
 
@app.route('/')
def hello():
    hello = (ref.get())
    return hello
 
if __name__ == "__main__":
    app.run()
