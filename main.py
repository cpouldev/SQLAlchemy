from config import crud
from config.crud import Session
from models.models import Author, Post, Category
from contextlib import contextmanager

@contextmanager
def db():
    session = Session()
    
    yield session
    
    session.close()


def restart_db():
    crud.recreate_database()

    posts = []
    
    with db() as session:
        
        for i in range(10):
            author = Author(name=f'author {i}')
            category = Category(name=f'category {i}')
            post = Post(title=f'title {i}', content=f'content {i}', author=author, category=category)
            
            posts.append(post)
            
        
        session.add_all(posts)
        
        session.commit()
        
        currCat = session.query(Category).first()
        currPost = currCat.post
        currAuthor = currCat.post.author

        print(currPost)
        print(currCat)
        print(currAuthor)


if __name__ == '__main__':
    restart_db()
    # with Session.begin() as session:
    #     p = session.query(Post).join(Category).filter(Post.pk == 1).first()
    #     print(p.category_id)
# LEFT OFF HERE
# https://docs.sqlalchemy.org/en/14/tutorial/dbapi_transactions.html
