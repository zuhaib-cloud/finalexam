from flask import Flask
import socket

app = Flask(__name__)
hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)

@app.route('/')
def hello_cloud():
  return 'Hello Cloud!Welcome to khan final test API server'
  
@app.route('/host')
def host_name():
  return hostname

@app.route('/ip')
def host_ip():
  return ip_address

app.run(host='0.0.0.0')
