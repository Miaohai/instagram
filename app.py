from flask import Flask
from database.db import initialize_db
from flask_restful import Api
from resources.routes import initialize_routes
from flask_bcrypt import Bcrypt

app = Flask(__name__)
api = Api(app)
bcrypt = Bcrypt(app)


app.config['MONGODB_SETTINGS'] = {
    'host':'mongodb://localhost/instagram'
}

initialize_db(app)
initialize_routes(api)

def index():
    return render_template('index.html')

app.run()

# 