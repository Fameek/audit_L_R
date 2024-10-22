"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import Flask, request, jsonify, make_response, render_template
from FlaskWebProject1 import app

@app.route('/')
def index():
    return render_template('index.html')

#���� ��� GET-��������
@app.route('/get-route', methods=['GET'])
def handle_get():
    if request.method == 'GET':
        params = request.args.to_dict()  # ������ ��������� �� GET-�������
        return jsonify(params)           # ���������� �� � ������� JSON
    else:
        return make_response("Method Not Allowed", 405)

#���� ��� POST-��������
@app.route('/post-route', methods=['POST'])
def handle_post():
    if request.method == 'POST':
        params = request.form.to_dict()  # �� �������� � ������� ����� �������� ��������� �� POST-�������
        return jsonify(params)           # ���������� �� � ������� JSON
    else:
        return make_response("Method Not Allowed", 405)

#���� ��� HEAD-��������
@app.route('/head-route', methods=['HEAD'])
def handle_head():
    if request.method == 'HEAD':
        response = make_response('', 200)
        response.headers['Content-Type'] = 'text/plain'
        return response
    else:
        return make_response("Method Not Allowed", 405)

#���� ��� OPTIONS-��������
@app.route('/options-route', methods=['OPTIONS'])
def handle_options():
    if request.method == 'OPTIONS':
        response = make_response('', 204)
        response.headers['Allow'] = 'OPTIONS, GET, POST, HEAD'
        return response
    else:
        return make_response("Method Not Allowed", 405)


