from flask import Flask, render_template,request, session, redirect, url_for
import logging
import json
from flask import flash, make_response, jsonify
from model.destinationForm import DestinationForm
from model.camping_dao import CampingDao
from model.dbModule import Database

# logging.basicConfig(filename="logs/project.log",level = logging.DEBUG)
app = Flask(__name__)
app.secret_key = f"#!#FSFSD#$$hf*^~io"

def to_json_array(results):
    jsons =  json.dumps( [dict(ix) for ix in results] ) #CREATE JSON
    return jsons

@app.route('/')
def init_view():
    return render_template("index.html")

@app.route('/ranking')
def get_top_ten():
    camping_dao = CampingDao()
    top_ten = camping_dao.get_top_ten_viewed()
    result_json = to_json_array(top_ten)
    return result_json

@app.route('/get_every_camping_locations')
def get_campings():
    camping_dao = CampingDao()
    searching_result = camping_dao.get_every_camping_locations()
    result_json = to_json_array(searching_result)
    return result_json 

@app.route('/search')
def search():
    camping_dao = CampingDao()
    data = []
    sido= request.args["sido"]
    gu = request.args["gu"]
    try:
        camping_info = camping_dao.search_camping_info(sido,gu)
        print(sido+gu)
    except:
        print("error occured")
    if camping_info != []: 
        data = to_json_array(camping_info)
    return data


@app.route('/main',methods = ['GET','POST'])
def main():
    search = DestinationForm(request.form)
    if request.method == 'POST':
        return search_results(search)
    return render_template("search_side_bar.html",form=search)

@app.route('/community')
def view_review(user):
    return render_template("community.html")

# ###### login - ssparts ##########
# @app.route('/login',methods=['GET','POST'])
# def login():

if __name__=='__main__':
    # ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS)
    # ssl_context.load_cert_chain(certfile='newcert.pem',keyfile='newkey.pem',password='secret')
    app.run(host='0.0.0.0',port=5000,debug=True,ssl_context = ('/work/vueapp/carprj/flask/server.crt','/work/vueapp/carprj/flask/server.key'))