# pyLint: disable=invalid-name
import os
from logging.config import fileConfig
import app
import config


if not os.path.exists('logs'):
    os.mkdir('logs')
fileConfig(os.path.join(os.path.dirname(__file__), 'logging.ini'))

run_config = config.load_config()
application = app.create_app()
if __name__ == '__main__':
    application.run(host=run_config.SERVER_HOST, port=run_config.PORT)
    # server = WSGIServer((run_config.SERVER_HOST, run_config.SERVER_PORT), application)
    # server.serve_forever()
