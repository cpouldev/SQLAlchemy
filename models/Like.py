from sqlalchemy import Table, Column, Integer, ForeignKey

from models.models import Base

like_table = Table('like',
                   Base.metadata,
                   #Column('pk', Integer(), primary_key=True),
                   Column('user_id', ForeignKey('user.pk', ondelete='CASCADE'), index=True),
                   Column('post_id', ForeignKey('post.pk', ondelete='CASCADE'), index=True))

"""
class Like(Base):
   __table__ = like_table

    def __repr__(self):
        return f"PK:{self.pk}, UserID:{self.user_id}, PostId:{self.post_id}"
"""
