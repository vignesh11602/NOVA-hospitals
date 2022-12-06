from flask import Flask, render_template,request, url_for, redirect
import json
import os
app = Flask(__name__)
picFolder = os.path.join('static', 'picture')
print(picFolder)
app.config['UPLOAD_FOLDER'] = picFolder

@app.route('/', methods = ['POST','GET'])
def index():
    pic = [os.path.join(app.config['UPLOAD_FOLDER'], 'img.jpg'),os.path.join(app.config['UPLOAD_FOLDER'], 'Logo.png')]
    if request.method == 'POST':
        data = {
            "firstname" : request.form['fname'],
            "lastname" : request.form['lname'],
            "dob" : request.form['dob'],
            "appoint" : request.form['appoint'],
            "time" : request.form['time'],
            "status" : "waiting"
        }
        # Opening JSON file
        with open('sample.json', 'r') as openfile:
        # Reading from json file
            json_object = json.load(openfile)
        print(json_object)
        a=json_object['data']
        a.append(data)
        data1 = {
            "data":a
        }
        json_object = json.dumps(data1, indent=4)
        # Writing to sample.json
        with open("sample.json", "w") as outfile:
            outfile.write(json_object)
    return render_template('index.html',pic=pic)

@app.route('/appointment', methods = ['POST','GET'])
def appointment():
    pic = [os.path.join(app.config['UPLOAD_FOLDER'], 'img.jpg'),os.path.join(app.config['UPLOAD_FOLDER'], 'Logo.png')]
    return render_template('appointment.html',pic=pic)

@app.route("/viewappointment", methods = ['POST','GET'])
def viewappointment():
    # Opening JSON file
    with open('sample.json', 'r') as openfile:
    # Reading from json file
        json_object = json.load(openfile)
    print(json_object)
    pic = [os.path.join(app.config['UPLOAD_FOLDER'], 'img.jpg'),os.path.join(app.config['UPLOAD_FOLDER'], 'Logo.png'),json_object]
    return render_template('viewappointment.html',pic=pic)

@app.route("/doctor", methods = ['POST', 'GET'])
def doctor():
    if request.method == 'GET':
        pic = [os.path.join(app.config['UPLOAD_FOLDER'], 'img.jpg'),os.path.join(app.config['UPLOAD_FOLDER'], 'Logo.png')]
        return render_template('doctorlogin.html',pic=pic)
    if request.method == 'POST':
        if (request.form['uname'] == 'admin')&(request.form['password'] == 'admin'):
            return redirect(url_for('doctorview'))
    pic = [os.path.join(app.config['UPLOAD_FOLDER'], 'img.jpg'),os.path.join(app.config['UPLOAD_FOLDER'], 'Logo.png')]
    return render_template('doctorlogin.html',pic=pic)

@app.route("/doctorview", methods = ['POST','GET'])
def doctorview():
    # Opening JSON file
    with open('sample.json', 'r') as openfile:
    # Reading from json file
        json_object = json.load(openfile)
    print(json_object)
    pic = [os.path.join(app.config['UPLOAD_FOLDER'], 'img.jpg'),os.path.join(app.config['UPLOAD_FOLDER'], 'Logo.png'),json_object]
    return render_template('doctorview.html',pic=pic)

@app.route("/accept", methods = ['GET','POST'])
def accept():
    if request.method == 'POST':
        # Opening JSON file
        with open('sample.json', 'r') as openfile:
        # Reading from json file
            json_object = json.load(openfile)
        print(json_object)
        data=json_object["data"]
        for i in data:
            if (i["firstname"]==request.form["firstname"])&(i["lastname"]==request.form["lastname"])&(i["dob"]==request.form["dob"])&(i["appoint"]==request.form["appoint"])&(i["time"]==request.form["time"]):
                i["status"]="approved"
                break
        data1 = {
            "data":data
        }
        json_object = json.dumps(data1, indent=4)
        # Writing to sample.json
        with open("sample.json", "w") as outfile:
            outfile.write(json_object)
    return redirect(url_for('doctorview'))

@app.route("/decline", methods = ['GET','POST'])
def decline():
    if request.method == 'POST':
        # Opening JSON file
        with open('sample.json', 'r') as openfile:
        # Reading from json file
            json_object = json.load(openfile)
        print(json_object)
        data=json_object["data"]
        for i in data:
            if (i["firstname"]==request.form["firstname"])&(i["lastname"]==request.form["lastname"])&(i["dob"]==request.form["dob"])&(i["appoint"]==request.form["appoint"])&(i["time"]==request.form["time"]):
                i["status"]="declined"
                break
        data1 = {
            "data":data
        }
        json_object = json.dumps(data1, indent=4)
        # Writing to sample.json
        with open("sample.json", "w") as outfile:
            outfile.write(json_object)
    return redirect(url_for('doctorview'))


if __name__ == "__main__":
    app.run(debug=True)