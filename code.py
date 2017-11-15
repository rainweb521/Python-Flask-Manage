# -*- coding=utf8 -*-
# 导入Flask库
from flask import Flask
from flask import request
from flask import render_template
# 导入MySQL库
import MySQLdb

app = Flask(__name__)
# 写好的数据库连接函数，
# 传入的是table，数据表的名称，
# 返回值是数据表中所有的数据，以元祖的格式返回
def get_Table_Data(table):
    conn = MySQLdb.connect(
        host='127.0.0.1', port=3306,
        user='root', passwd='root',
        db='guanli', charset='utf8',
    )
    cur = conn.cursor()
    res = cur.execute("select * from " + table)
    res = cur.fetchmany(res)
    cur.close()
    conn.commit()
    conn.close()
    return res

# 启动服务器后运行的第一个函数，显示对应的网页内容
@app.route('/', methods=['GET', 'POST'])
def home():
    # return '<a href="/index"><h1 align="center">欢迎使用教务系统---点击进入</h1></a>'
    return render_template('login.html')

# 对登录的用户名和密码进行判断
@app.route('/login', methods=['POST'])
def login():
    # 需要从request对象读取表单内容：
    if request.form['username'] == 'student' and request.form['password'] == 'password':
        return render_template('student_index.html')
    return render_template('teacher_index.html')


# 显示学生首页的函数，可以显示首页里的信息
@app.route('/student_index', methods=['GET'])
def student_index():
    return render_template('student_index.html')

# 显示教师首页的函数，可以显示首页里的信息
@app.route('/teacher_index', methods=['GET'])
def teacher_index():
    return render_template('teacher_index.html')

# 显示教学计划的函数，当有请求发生时，去数据库里查找对应的数据，
# 然后将数据的格式用for循环进行遍历，变成列表的格式，然后返回到页面中，
# 再由页面进行显示数据
@app.route('/jxjh', methods=['GET'])
def jxjh():
    # 调用数据库函数，获取数据
    data = get_Table_Data('jihuaxijie')
    # 用列表的格式存放全部数据
    posts = []
    for value in data:
        dict_data = {}
        dict_data['a'] = value[0]
        dict_data['b'] = value[1]
        dict_data['c'] = value[2]
        dict_data['d'] = value[3]
        dict_data['e'] = value[4]
        dict_data['f'] = value[5]
        dict_data['g'] = value[6]
        posts.append(dict_data)
    # print posts
    return render_template('teacher.html', posts=posts)


# 显示管理班的函数页面
@app.route('/guanliban', methods=['GET'])
def guanliban():
    # 调用数据库函数，获取数据
    data = get_Table_Data('guanliban')
    # 用列表的格式存放全部数据
    posts = []
    for value in data:
        dict_data = {}
        dict_data['a'] = value[0]
        dict_data['b'] = value[1]
        dict_data['c'] = value[2]
        dict_data['d'] = value[3]
        dict_data['e'] = value[4]
        dict_data['f'] = value[5]
        posts.append(dict_data)
    # print posts
    return render_template('teacher.html', posts=posts)

# 显示排课信息的函数页面
@app.route('/paike_js', methods=['GET'])
def paike_js():
    # 调用数据库函数，获取数据
    data = get_Table_Data('paike_js')
    # 用列表的格式存放全部数据
    posts = []
    for value in data:
        dict_data = {}
        dict_data['a'] = value[0]
        dict_data['b'] = value[1]
        dict_data['c'] = value[2]
        dict_data['d'] = value[3]
        dict_data['e'] = value[4]
        dict_data['f'] = value[5]
        posts.append(dict_data)
    # print posts
    return render_template('teacher.html', posts=posts)

# 显示学生成绩的页面，包括调用学生成绩数据表
@app.route('/xscj', methods=['GET'])
def xscj():
    # 调用数据库函数，获取数据
    data = get_Table_Data('xueshengchengji')
    # 用列表的格式存放全部数据
    posts = []
    for value in data:
        dict_data = {}
        dict_data['a'] = value[0]
        dict_data['b'] = value[1]
        dict_data['c'] = value[2]
        dict_data['d'] = value[3]
        dict_data['e'] = value[4]
        dict_data['f'] = value[5]
        posts.append(dict_data)
    # print posts
    return render_template('teacher.html', posts=posts)

# 显示学生类别的页面，包括调用学生成绩数据表
@app.route('/xslb', methods=['GET'])
def xslb():
    # 调用数据库函数，获取数据
    data = get_Table_Data('xslb')
    # 用列表的格式存放全部数据
    posts = []
    for value in data:
        dict_data = {}
        dict_data['a'] = value[0]
        dict_data['b'] = value[1]
        dict_data['c'] = value[2]
        dict_data['d'] = value[3]
        dict_data['e'] = value[4]
        posts.append(dict_data)
    # print posts
    return render_template('teacher.html', posts=posts)


# 显示田楼教室的函数页面
@app.route('/tjiaoshi', methods=['GET'])
def tjiaoshi():
    # 调用数据库函数，获取数据
    data = get_Table_Data('tjiaoshi')
    # 用列表的格式存放全部数据
    posts = []
    for value in data:
        dict_data = {}
        dict_data['a'] = value[0]
        dict_data['b'] = value[1]
        dict_data['c'] = value[2]
        dict_data['d'] = value[3]
        dict_data['e'] = value[4]
        dict_data['f'] = value[5]
        posts.append(dict_data)
    # print posts
    return render_template('student.html', posts=posts)

# 显示课程的函数页面
@app.route('/kecheng', methods=['GET'])
def kecheng():
    # 调用数据库函数，获取数据
    data = get_Table_Data('kecheng')
    # 用列表的格式存放全部数据
    posts = []
    for value in data:
        dict_data = {}
        dict_data['a'] = value[0]
        dict_data['b'] = value[1]
        dict_data['c'] = value[2]
        dict_data['d'] = value[3]
        dict_data['e'] = value[4]
        dict_data['f'] = value[5]
        posts.append(dict_data)
    # print posts
    return render_template('student.html', posts=posts)

# 显示专业的函数页面
@app.route('/zhuanye', methods=['GET'])
def zhuanye():
    # 调用数据库函数，获取数据
    data = get_Table_Data('zhuanye')
    # 用列表的格式存放全部数据
    posts = []
    for value in data:
        dict_data = {}
        dict_data['a'] = value[0]
        dict_data['b'] = value[1]
        dict_data['c'] = value[2]
        dict_data['d'] = value[3]
        dict_data['e'] = value[4]
        posts.append(dict_data)
    # print posts
    return render_template('student.html', posts=posts)

# 显示学院的函数页面
@app.route('/xueyuan', methods=['GET'])
def xueyuan():
    # 调用数据库函数，获取数据
    data = get_Table_Data('xueyuan')
    # 用列表的格式存放全部数据
    posts = []
    for value in data:
        dict_data = {}
        dict_data['a'] = value[0]
        dict_data['b'] = value[1]
        dict_data['c'] = value[2]
        dict_data['d'] = value[3]
        posts.append(dict_data)
    # print posts
    return render_template('student.html', posts=posts)

# 显示教师信息的页面，
@app.route('/js', methods=['GET'])
def js():
    # 调用数据库函数，获取数据
    data = get_Table_Data('jiaoshi')
    # 用列表的格式存放全部数据
    posts = []
    for value in data:
        dict_data = {}
        dict_data['a'] = value[0]
        dict_data['b'] = value[1]
        dict_data['c'] = value[2]
        dict_data['d'] = value[3]
        dict_data['e'] = value[4]
        dict_data['f'] = value[5]
        dict_data['g'] = value[6]
        dict_data['h'] = value[7]
        dict_data['i'] = value[8]
        dict_data['j'] = value[9]
        posts.append(dict_data)
    # print posts
    return render_template('xscj.html', posts=posts)

# 主函数
if __name__ == '__main__':
    # app.debug = True
    app.run()