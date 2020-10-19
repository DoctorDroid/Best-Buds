from flask_sqlalchemy import SQLAlchemy

DB = SQLAlchemy()


class User(DB.Model):
    id = DB.Column(DB.BigInteger, primary_key=True)
    username = DB.Column(DB.String(80), unique=False, nullable=False)
    email_addy = DB.Column(DB.String(120), unique=True, nullable=False)
    password = DB.Column(DB.String(18), nullable=False)
    reg_time_date = DB.Column(DB.DateTime, nullable=False)

    def __repr__(selfself):
        return '<User %r>' % self.username

class Strain(DB.Model):
    id = DB.Column(DB.BigInterger, primary_key=True)
