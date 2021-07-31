from functools import wraps
from flask import abort
from flask_login import current_user
from .models import Permission


# 检查用户权限自定义的装饰器

# 新增装饰器
def permission_required(permission):  # permission是装饰器所需的参数
    def decorator(f):  # f 是要装饰的函数
        @wraps(f)   # functools.wraps对我们的装饰器函数进行了装饰，
        def decorated_function(*args, **kwargs):
            if not current_user.can(permission):
                abort(403)
            return f(*args, **kwargs)

        return decorated_function

    return decorator


def admin_required(f):
    return permission_required(Permission.ADMIN)(f)
