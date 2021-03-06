from flask import Flask, render_template, request,redirect
from flask.helpers import find_package, url_for
import os
import cv2
from pathlib import Path

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
    target = os.path.join(APP_ROOT,'F:/College/SemVI/Biometrics/Project/Traffice_Offender_Verification/fingerprint_recognition/registered')
    file = request.files["fingerprint"]
    filename = request.form['identity']
    ext = file.filename[-4:]
    destination = "/".join([target,filename+ext])
    print(destination)
    file.save(destination)
    
    return redirect('/')

@app.route('/verify' , methods=[ 'GET','POST'])
def upload_verify():
    target = os.path.join(APP_ROOT,'F:/College/SemVI/Biometrics/Project/Traffice_Offender_Verification/fingerprint_recognition/sample')
    file = request.files["fingerprint"]
    filename = request.form['identity']
    ext = file.filename[-4:]
    destination = "/".join([target,filename+ext])
    print(destination)
    file.save(destination)
    
    import fingerprint_recognition
    from fingerprint_recognition import fpr
     
    return render_template('verify.html',result = fpr.main(filename))
    os.remove(destination)
from flask import Flask, render_template, request,redirect
from flask.helpers import find_package, url_for
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
    target1 = os.path.join(APP_ROOT,'F:/College/SemVI/Biometrics/Project/Traffice_Offender_Verification/fingerprint_recognition/registered')
    target2 = os.path.join(APP_ROOT,'F:/College/SemVI/Biometrics/Project/Traffice_Offender_Verification/signature_recognition/registered')
    fp = request.files["fingerprint"]
    signature = request.files["signature"]
    filename = request.form['identity']
    ext1 = fp.filename[-4:]
    ext2 = signature.filename[-4:]
    destination1 = "/".join([target1,filename+ext1])
    destination2 = "/".join([target2,filename+ext2])
    # print(destination1)
    # print(destination2)
    if os.path.isfile(destination1):
        return render_template('enroll.html',result ="ID already exists")
    fp.save(destination1)
    signature.save(destination2)

    return redirect('/')

@app.route('/verify' , methods=[ 'GET','POST'])
def upload_verify():
    target1 = os.path.join(APP_ROOT,'F:/College/SemVI/Biometrics/Project/Traffice_Offender_Verification/fingerprint_recognition/sample')
    target2 = os.path.join(APP_ROOT,'F:/College/SemVI/Biometrics/Project/Traffice_Offender_Verification/signature_recognition/sample')
    fp = request.files["fingerprint"]
    signature = request.files["signature"]
    filename = request.form['identity']
    ext1 = fp.filename[-4:]
    ext2 = signature.filename[-4:]
    destination1 = "/".join([target1,filename+ext1])
    destination2 = "/".join([target2,filename+ext2])
    # print(destination1)
    # print(destination2)
    fp.save(destination1)
    signature.save(destination2)

    from fingerprint_recognition import fpr
    from signature_recognition import sr

    res1 = fpr.main(filename)
    res2 = sr.main(filename)

    if os.path.exists(destination1):
        os.path.exists(destination1)
        os.remove(destination1)
    if os.path.exists(destination2):
        os.path.exists(destination2)
        os.remove(destination2)

    return render_template('verify.html',result1 = res1,result2 = res2)


if __name__ == '__main__':
    app.run(debug=True)
if __name__ == '__main__':
    app.run(debug=True)