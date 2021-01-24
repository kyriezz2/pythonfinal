from flask import Flask,escape,url_for
import geo
# central registry ：中央登记中心，负责所有的页面（url\view functions\template...）登记
app = Flask(__name__)

# 1、(必要) url --> 路径
# ***** 不重要 ：装饰器（@装饰器名称.方法）
@app.route('/') # 路径的 endpoint（终结点）
# 2、(必要)视图函数 view functions
# 函数的概念：没有调用时，不占空间，且不运行
def hello_flask():
    """hello """
    return 'Hello Flask!'  # return -->结果直接在对应的url上展示出来

@app.route('/index')
def hello_world():
    """hello """
    return 'Hello world!'

# 变量规则
@app.route('/user/<username>',methods=['POST'])
def show_user_profile(username):
    # show the user profile for that user
    return 'hello %s' % escape(username)




@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id
#
# @app.route('/projects/')
# def projects():
#     return 'The project page'
#
# @app.route('/about')
# def about():
#     return 'The about page'

with app.test_request_context():
    # url_for : 通过视图函数重定向到url的路径（endpoint）
    print(url_for('hello_flask'))
    print(url_for('hello_world'))
    print(url_for('show_user_profile', username='zhichao'))
    print(url_for('show_post', post_id="12345"))


if __name__ == '__main__':
    app.run(host='127.0.0.1',port='8888',debug=True)
