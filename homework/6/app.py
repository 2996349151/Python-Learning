from ast import Delete
from flask import Flask,request,json,jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import pymysql
from flask_cors import CORS
pymysql.install_as_MySQLdb()

app=Flask(__name__)
CORS(app)
SQLALCHEMY_TRACK_MODIFICATIONS = True
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = False

HOSTNAME = "192.168.30.128"
PORT = 3306
USERNAME = "root"
PASSWORD = "dw123456"
DATABASE = "Hwk6"
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}?charset=utf8mb4"

db=SQLAlchemy(app)

class Stu(db.Model):
    __tablename__ = 'student'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100))
    gender = db.Column(db.String(100))
    age = db.Column(db.Integer)
    grade = db.Column(db.String(100))
    enrollmentDate = db.Column(db.Date)

    def to_list(self):
        return [self.id,self.name,self.gender,self.age,self.grade,self.enrollmentDate]


def insert_data(data):
    if Stu.query.filter_by(name=data[0]).first() == True:
        return False
    stu = Stu(name=data[0],gender=data[1],age=data[2],grade=data[3],enrollmentDate=data[4])
    db.session.add(stu)
    db.session.commit()
    return True

def delete_data(stu_id):
    stu = Stu.query.filter_by(id=stu_id).first()
    if stu == None:
        return False
    db.session.delete(stu)
    db.session.commit()
    return True

def change_data(data):
    stu = Stu.query.filter_by(id=data[0]).first()
    stu.name=data[1]
    stu.gender=data[2]
    stu.age=data[3]
    stu.grade=data[4]
    stu.enrollmentDate=data[5]
    db.session.merge(stu)
    db.session.commit()
    return True

@app.route('/students',methods=['GET'])
def show_all():
    stus = Stu.query.filter().all()
    stu_list = list()
        
    for stu in stus:
        s = stu.to_list()
        stu_dict = dict()
        stu_dict['id'] = s[0]
        stu_dict['name'] = s[1]
        stu_dict['gender'] = s[2]
        stu_dict['age'] = s[3]
        stu_dict['grade'] = s[4]
        stu_dict['enrollmentDate'] = str(s[5])

        stu_list.append(stu_dict)
        
    return jsonify(stu_list)

@app.route('/students',methods=['POST'])
def add_stu():
    D = request.data.decode('utf-8')
    D = json.loads(D)
    data = list()
    data.append(D['name'])
    data.append(D['gender'])
    data.append(D['age'])
    data.append(D['grade'])
        
    d = datetime.strptime(D['enrollmentDate'], '%Y-%m-%d')
    data.append(d.date())
        
    insert_data(data)
    return data

@app.route('/students/<int:stu_id>',methods=['PUT'])
def change_stu(stu_id):
    
    D = request.data.decode('utf-8')
    D = json.loads(D)
    data = list()
    data.append(int(stu_id))
    data.append(D['name'])
    data.append(D['gender'])
    data.append(D['age'])
    data.append(D['grade'])
            
    d = datetime.strptime(D['enrollmentDate'], '%Y-%m-%d')
    data.append(d.date())
            
    change_data(data)    
    return data
@app.route('/students/<int:stu_id>',methods=['DELETE'])
def delete_stu(stu_id):
    delete_data(int(stu_id))
    return str(stu_id)

@app.route('/')
def test():
    stus = Stu.query.filter().all()
    stu_list = list()
        
    for stu in stus:
        s = stu.to_list()
        stu_dict = dict()
        stu_dict['id'] = s[0]
        stu_dict['name'] = s[1]
        stu_dict['gender'] = s[2]
        stu_dict['age'] = s[3]
        stu_dict['grade'] = s[4]
        stu_dict['enrollmentDate'] = str(s[5])

        stu_list.append(stu_dict)
    return stu_list


if __name__ == '__main__':
    
    app.run(host='127.0.0.1',port=5000,debug=True)
