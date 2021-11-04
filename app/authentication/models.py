from app.extensions.database import db
from sqlalchemy.exc import IntegrityError
from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(80), index = True)
    email = db.Column(db.String(80), index = True, unique = True)
    password_hash = db.Column(db.String(128))
    rent_items = db.relationship('RentItem', backref='user', lazy=True)
    reading_list_items = db.relationship('ReadingListItem', backref='user', lazy = True)
    
    def __repr__(self):
        return self.name
    def set_password (self, password):
        self.password_hash = generate_password_hash(password)
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    def save(self):
      db.session.add(self)
      try: 
        db.session.commit()
      except IntegrityError as error:
        db.session.rollback()
        return error
    def delete(self):
      db.session.delete(self)
      db.session.commit()

class Book(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(), index = True)
    author = db.Column(db.String(), index = True)
    description = db.Column(db.String())
    status = db.Column(db.Boolean(), index = True)
    def save(self):
      db.session.add(self)
      try: 
        db.session.commit()
      except IntegrityError as error:
        db.session.rollback()
        return error
    def delete(self):
      db.session.delete(self)
      db.session.commit()
    def change_status(self):
      self.status = not self.status
      db.session.commit()


class RentItem(db.Model):
   id = db.Column(db.Integer, primary_key = True)
   start_date = db.Column(db.DateTime())
   end_date = db.Column(db.DateTime())
   book_id = db.Column(db.Integer, db.ForeignKey('book.id'))
   user_id = db.Column(db.Integer, db.ForeignKey('user.id'))  
   def save(self):
      db.session.add(self)
      db.session.commit()
   def delete(self):
      db.session.delete(self)
      db.session.commit()  

class ReadingListItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'))
    def save(self):
      db.session.add(self)
      db.session.commit()
    def delete(self):
      db.session.delete(self)
      db.session.commit()