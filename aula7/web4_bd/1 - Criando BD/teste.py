from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)


if __name__ == "__main__":
	with app.app_context():
		db.create_all()
		app.run(debug=True)

