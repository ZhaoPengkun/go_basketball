import os
from app import create_app
from flask_script import Manager, Server

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)
server = Server(host='0.0.0.0', port=9000)
manager.add_command("runserver", server)

if __name__ == '__main__':
    manager.run()
