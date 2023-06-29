from flask import Flask,render_template,\
    redirect,url_for,session,request,flash

#导入wtf扩展的表单类
from flask_wtf import FlaskForm
#导入自定义表单需要的字段
from wtforms import SubmitField,StringField,PasswordField
#导入wtf扩展提供的表单验证器
from wtforms.validators import DataRequired,EqualTo

app = Flask(__name__)
app.config['SECRET_KEY']='1'

#自定义表单类，文本字段、密码字段、提交按钮
class Login(FlaskForm):
    us = StringField(label='用户：', validators=[DataRequired()])
    ps = PasswordField(label='密码', validators=[DataRequired(), EqualTo('ps2', 'err')])
    ps2 = PasswordField(label='确认密码', validators=[DataRequired()])
    submit = SubmitField('提交')

@app.route('/login')
def login():
    return render_template('login.html')

#定义根路由视图函数，生成表单对象，获取表单数据，进行表单数据验证
@app.route('/',methods=['GET','POST'])
def index():
    form = Login()
    if form.validate_on_submit():
        name = form.us.data
        pswd = form.ps.data
        pswd2 = form.ps2.data
        print(name,pswd,pswd2)
        return redirect(url_for('login'))
    else:
        if request.method=='POST':
            flash(u'信息有误，请重新输入！')
        print(form.validate_on_submit())

    return render_template('index.html',form=form)

if __name__ == '__main__':
    app.run(debug=True)
