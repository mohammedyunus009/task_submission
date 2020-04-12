from flask import Flask, session, render_template, request, redirect, g, url_for,redirect,jsonify
import os
import uuid
import sqlite3
#import src.prepare_data as pp_data

app = Flask(__name__)
app.secret_key = os.urandom(24)

db_path = '/home/yunus/simple_flask/test.db'
conn = sqlite3.connect(db_path,check_same_thread=False)
# conn = sqlite3.connect(db_path)

username = ['admin']
password = ['admin']

#app = Flask(__name__)
#APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        session.pop('user', None)

        if request.form['username'] in username:
            if request.form['password'] in password:
                session['user'] = request.form['username']
                return render_template('upload.html')

    return render_template('index.html')

@app.route('/success', methods=['GET'])
def success_page():
    return render_template("success.html")


#Below method is rest request

pat='/home/yunus/simple_flask/files'

@app.route('/upload_data', methods=['POST','GET'])
def upload_file():
    uid = str(uuid.uuid4().hex)
    print((request.values.to_dict()))
    st=''
    dic = request.values.to_dict()
    if request.values.to_dict()['Emp_id']:
        tu = (dic['Emp_id'],dic['name1'],dic['Email'],
            dic['age'],dic['salary'],dic['Phone'],
            dic['address'],uid)
        insertion(tu)
    else :
        print('No Emp_id')
        return render_template('failure.html')

    if request.files:
        fd = request.files['uploadedFile']
        destination_file_path = os.path.join(pat , uid + ".jpg")
        fd.save(destination_file_path)
        print("Destination file path: " + destination_file_path)
    print("complete!!!!!!!!!!!!!!!")
    return render_template('index.html')


@app.route('/data', methods=['POST'])
def admin():
    if request.method == 'POST':
        print(request.form)
        print(request.form['file'])
        # print('files',request.files['uploadedFile'])
        if request.files:
            fd = request.files['uploadedFile']
            fd.save(pat)
        #if request.form['Name']:
        #    session.pop('user', None)
    #print(request.form)
    tup=()
    #with conn as f:
    #f.execute('''INSERT INTO Employee  (ID ,NAME,AGE,ADDRESS,SALARY,email,Phone_no,emp_image)
    #Values(?,?,?,?,?,?,?,?);''',tup)

    return "<h1>Insertion successfull</h1>"

def insertion(tu):
    with conn as f:
        f.execute('''INSERT INTO Employee
            (ID ,NAME,email,AGE,SALARY,ADDRESS,Phone_no,emp_image)
    Values(?,?,?,?,?,?,?,?);''',tu)
        f.commit()

@app.route('/get_by_id', methods=['POST'])
def get_emp_by_id():
    tu = request.get_json()['Emp_id']
    li=[]
    with conn as f:
        tu = f.execute('''select * from Employee where ID=?;''',(tu,))
        for i in tu:
            li.append({
                'ID':i[0],'name':i[1],'email':i[2],'age':i[3],
                'salary':i[4],'address':i[5],'Phone_no':i[6],'image_loc':i[7]
                })

        f.commit()
    return jsonify(li)


@app.route('/get_bet_sal', methods=['POST'])
def get_between_salary():
    tu = (request.get_json()['start'],request.get_json()['end'])
    print(tu)
    li=[]
    with conn as f:
        tu = f.execute('''select * from Employee where salary between ? and ?;''',(tu))
        for i in tu:
            li.append({
                'ID':i[0],'name':i[1],'email':i[2],'age':i[3],
                'salary':i[4],'address':i[5],'Phone_no':i[6],'image_loc':i[7]
                })

        f.commit()
    return jsonify(li)

if __name__ == '__main__':
    app.run(debug=True)