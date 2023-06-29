# 导入Flask类
from flask import Flask,redirect,make_response,request,render_template,url_for

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text

from flask_bootstrap import Bootstrap4
import redis

#Flask类接收一个参数__name__
app = Flask(__name__)
Bootstrap4(app)

# 获取mysql数据库连接
app.config.from_object('dbconfig')
db = SQLAlchemy(app)

# 定义学生
class Student(db.Model):
    no = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(10))
    age = db.Column(db.Integer)
    classno = db.Column(db.Integer)

# 获取redis数据库连接
r = redis.StrictRedis(host="localhost", port=6379, db=0)
#r = redis.StrictRedis(host="redisNet", port=6379, db=0)

# redis存入键值对
r.set(name="key", value=int(1))

#mysql数据库检索
@app.route('/', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        grade = request.form.get('grade')

        sql = text("SELECT no , " \
                "name , " \
                "age , " \
                "classno " \
                " FROM student" \
                " WHERE classno = :class_1")
        #  返回的是rawProxy对象，还需要转为前端可以接受的Dict
        stock_list = db.session.execute(sql, {'class_1': grade})
        students = [dict(zip(row._mapping.keys(), row)) for row in stock_list]
        
        print(students)
        #students = Student.query.filter_by(classno=grade).all()
        return render_template('search.html', students=students)
    else:
        return render_template('search.html')

@app.route('/res')
def rediscount():
    myintvar = int(r.get("key"))
    r.set(name="key", value=myintvar+1)
    return render_template('bootindex.html',myintvar=myintvar)


# 装饰器的作用是将路由映射到视图函数index
#@app.route('/')
#def index():
#    return 'Hello World'

@app.route('/user/<string:id>')
def hello_itcast(id):
    return 'hello user %d' %id,999

@app.route('/ksic')
def go_ksic():
    return redirect('https://www.kubota.com.cn/ksic/index.html')

@app.errorhandler(500)
def error(e):
    return '页面访问有错误：%s'%e

@app.route('/cookie')
def set_cookie():
    resp = make_response('this is to set cookie')
    resp.set_cookie('username', 'ksic')
    return resp

@app.route('/request')
def resp_cookie():
    resp = request.cookies.get('username')
    return resp

@app.route('/var')
def indexvar():
    mydict = {'key':'silence is gold'}
    mylist = ['Speech', 'is','silver']
    myintvar = 0

    return render_template('vars.html',
                           mydict=mydict,
                           mylist=mylist,
                           myintvar=myintvar
                           )

@app.route('/ul1/')
def redirect1():
    return url_for('index',_external=True)

@app.route('/ul2/')
def redirect2():
    return url_for('index')

# 模板用过滤器
@app.template_filter('alantest')
def testfilter(ls):
    return '**add filter**: %s'%ls

@app.route('/temp1/')
def template1():
    return render_template('temp1.html')

@app.route('/temp2/')
def template2():
    return render_template('temp2.html')

# Flask应用程序实例的run方法启动WEB服务器
if __name__ == '__main__':
    app.run()