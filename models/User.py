from sqlalchemy import Table, Column, Integer, ForeignKey

from .Like import like

from models.models import Base

class User(Base):
    __table__ = user_table
    pk = Column(Integer(), primary_key=True))
    author_id = Column(ForeignKey('author.pk'), unique=True)

    def __repr__(self):
        return f"PK:{self.pk}, AuthorID:{self.author_id}"
