from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, backref

Base = declarative_base()


class Author(Base):
    __tablename__ = "author"

    pk = Column(Integer, primary_key=True)
    name = Column(String)

    def __repr__(self):
        return f"Author< ID = {self.pk}, NAME = {self.name}>"


class Post(Base):
    __tablename__ = "post"

    pk = Column(Integer, primary_key=True)
    title = Column(String, unique=True)
    content = Column(String)

    category_id = Column(Integer, ForeignKey('category.pk', ondelete='SET NULL'))
    author_id = Column(Integer, ForeignKey('author.pk', ondelete='CASCADE'))
    
    category = relationship('Category', uselist=False, backref=backref('posts'))
    author = relationship('Author', uselist=False, backref=backref('posts'))

    def __repr__(self):
        return f"Post< ID = {self.pk}, TITLE = {self.title}," \
               f" CONTENT = {self.content}, CATEGORY = {self.category_id}," \
               f" AUTHOR = {self.author_id}>"


class Category(Base):
    __tablename__ = "category"

    pk = Column(Integer, primary_key=True)
    name = Column(String, unique=True)

    def __repr__(self):
        return f"Category< ID = {self.pk}, NAME = {self.name}>"
