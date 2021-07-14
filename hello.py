"""
测试主页
"""
from flask import Flask, request, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)


@app.errorhandler(404)
def page_not_found(e):
    """
    404错误处理
    """
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    """
    500错误处理
    """
    return render_template('500.html'), 500


@app.route('/')
def index():
    """
    首页
    """
    return render_template('index.html')


@app.route('/user/<name>')
def user(name):
    """
    变量测试
    """
    return render_template('user.html', name=name)
