"""
报错模块
"""
from . import main
from flask import render_template


@main.errorhandler(404)
def page_not_found(e):
    """
    404错误处理
    """
    return render_template('404.html'), 404


@main.errorhandler(500)
def internal_server_error(e):
    """
    500错误处理
    """
    return render_template('500.html'), 500
