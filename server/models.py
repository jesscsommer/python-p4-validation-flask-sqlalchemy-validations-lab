from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
db = SQLAlchemy()

class Author(db.Model):
    __tablename__ = 'authors'
    # Add validations and constraints 

    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String, unique=True, nullable=False)
    phone_number = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    @validates('name')
    def validate_name(self, key, name):
        if not len(name):
            raise ValueError('Author must have a name')
        return name
    
    @validates('phone_number')
    def validate_phone_number(self, key, num):
        if not len(num) == 10: 
            raise ValueError('Phone number must be 10 digits')
        return num

    def __repr__(self):
        return f'Author(id={self.id}, name={self.name})'

class Post(db.Model):
    __tablename__ = 'posts'
    # Add validations and constraints 

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.String)
    category = db.Column(db.String)
    summary = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    @validates('title')
    def validates_title(self, key, title):
        clickbait = ['Won\'t Believe', 'Secret', 'Top', 'Guess']
        if not len(title): 
            raise ValueError('Post must have a title')
        for bait in clickbait: 
            if bait in title: 
                return title 
        raise ValueError('Title must have clickbait')

    @validates('content')
    def validates_content(self, key, content):
        if len(content) < 250: 
            raise ValueError('Post content must be at least 250 characters')
        return content
    
    @validates('summary')
    def validates_summary(self, key, summary):
        if len(summary) >= 250: 
            raise ValueError('Summary must be less than 250 characters')
        return summary

    @validates('category')
    def validates_category(self, key, cat):
        if cat not in ['Fiction', 'Non-Fiction']:
            raise ValueError('Category must be Fiction or Non-Fiction')
        return cat
    
    def __repr__(self):
        return f'Post(id={self.id}, title={self.title} content={self.content}, summary={self.summary})'
