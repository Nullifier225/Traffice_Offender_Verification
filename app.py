from flask import Flask, render_template, request,redirect
from flask.helpers import url_for
import os

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('landing.html')

@app.route('/verify')
def login():
    return render_template('verify.html')

@app.route('/enroll')
def register():
    return render_template('enroll.html')

@app.route('/enroll' , methods=[ 'GET','POST'])
def upload_enroll():
    target = os.path.join(APP_ROOT,'/Users/SOWMIHARI/Documents/GitHub/Traffice_Offender_Verification/fingerprint-recognition/registered')
    file = request.files["fingerprint"]
    filename = request.form['identity']
    ext = file.filename[-4:]
    destination = "/".join([target,filename+ext])
    print(destination)
    file.save(destination)
    
    return redirect('/')

@app.route('/verify' , methods=[ 'GET','POST'])
def uploa_verify():
    target = os.path.join(APP_ROOT,'/Users/SOWMIHARI/Documents/GitHub/Traffice_Offender_Verification/fingerprint-recognition/sample')
    file = request.files["fingerprint"]
    filename = request.form['identity']
    ext = file.filename[-4:]
    destination = "/".join([target,filename+ext])
    print(destination)
    file.save(destination)
    
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)