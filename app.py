from flask import Flask
from routes.home import home
from config import Config

app = Flask(__name__)
app.register_blueprint(home)
app.config.from_object(Config)

if __name__ ==  "__main__":
    app.run(debug=True)