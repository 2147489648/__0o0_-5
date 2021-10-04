#whole file is to keep the bot run 24/7
#idk how it works also
#just copied from Web
from flask import Flask

from threading import Thread



app = Flask('')



@app.route('/')

def home():

    return "I'm alive"



def run():

  app.run(host='0.0.0.0',port=8080)



def keep_alive():  

    t = Thread(target=run)

    t.start()

