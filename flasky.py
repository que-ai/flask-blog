"""
入口文件
"""
from app import create_app, db
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app.models import User, Role
import click

app = create_app('development')

manager = Manager(app)
Migrate(app, db)
manager.add_command("db", MigrateCommand)


@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User, Role=Role)


if __name__ == '__main__':
    manager.run()
