from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)



def main():
    app.config['FLASK_ENV'] = 'development'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+asyncpg://postgres:postgres@localhost:5432/shelby_bot'
    app.config['SECRET_KEY'] = 'keykeykey'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

    db = SQLAlchemy(app)


@app.get('/')
def index():
    return render_template('index.html')







if __name__ == '__main__':
    main()
