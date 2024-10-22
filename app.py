import os
from app import create_app

config_name = os.getenv('FLASK_CONFIG', 'default')
app = create_app(config_name)

port = app.config.get("PORT", 8000)

if __name__ == '__main__':
    app.run(port=port)
