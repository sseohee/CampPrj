from flask import Flask, render_template, request, session, redirect, url_for
import logging
import json
from flask import flash, make_response, jsonify
from model.destinationForm import DestinationForm
from model.camping_dao import CampingDao
from model.dbModule import Database


class MyFlask(Flask):
    jinja_options = Flask.jinja_options.copy()
    jinja_options.update(dict(
        # Default is '{{', I'm changing this because Vue.js uses '{{' / '}}'
        variable_start_string='%%',
        variable_end_string='%%',
    ))


# logging.basicConfig(filename="logs/project.log",level = logging.DEBUG)
app = MyFlask(__name__)
app.secret_key = f"#!#FSFSD#$$hf*^~io"


def to_json_array(results):
    jsons = json.dumps([dict(ix) for ix in results])  # CREATE JSON
    return jsons


@app.route('/')
def init_view():
    return render_template("index.html")


@app.route('/home')
def vue_main():
    return render_template("index.html")

# @app.route('/test')
# def get_test():
#     test_data=  


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
    sido = request.args["sido"]
    gu = request.args["gu"]
    try:
        camping_info = camping_dao.search_camping_info(sido, gu)
        print(sido+gu)
    except:
        print("error occured")
    if camping_info != []:
        data = to_json_array(camping_info)
    return data

@app.route('/viewed_count')
def get_view_count():
    camping_dao = CampingDao()
    camping_index = 'CAMPING_INDEX 2'
    date = '20200113'
    time = '01'
    # try:
        # 1번째 인자는 캠핑 인덱스, 2번째 인자는 검색하려는 날짜, 3번째 인덱스는 검색하려는 시간을 의미합니다. 
    count = camping_dao.get_viewed_count(camping_index, date,time)
    print(count)
    return count

@app.route('/main', methods=['GET', 'POST'])
def main():
    # if request.method == 'POST':
    return render_template("search_side_bar.html", form=search)


@app.route('/community')
def view_review(user):
    return render_template("community.html")

# ###### login - parts ##########
# @app.route('/login',methods=['GET','POST'])
# def login():


if __name__ == '__main__':
    # ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS)
    # ssl_context.load_cert_chain(certfile='newcert.pem',keyfile='newkey.pem',password='secret')
    app.run(host='0.0.0.0', port=5000, debug=True, ssl_context=(
        '/data/works/test_copy2/flask/server.crt', '/data/works/test_copy2/flask/server.key'))
