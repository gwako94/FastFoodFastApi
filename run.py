import os

from app.app import create_app
env_name = os.getenv('FLASK_ENV')
app = create_app(env_name)


if __name__ == '__main__':
    # run app
    app.run(debug=True)
