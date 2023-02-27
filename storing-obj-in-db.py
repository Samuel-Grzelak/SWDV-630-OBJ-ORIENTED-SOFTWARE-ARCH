from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Create the engine for the SQLite database
engine = create_engine('sqlite:///example.db', echo=True)

# Create a session factory
Session = sessionmaker(bind=engine)

# Create a declarative base for our object model
Base = declarative_base()

# Define our object model
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)

    def __repr__(self):
        return f'<User(id={self.id}, name={self.name}, email={self.email})>'

# Create the table if it doesn't exist
Base.metadata.create_all(engine)

# Create a new user
user = User(name='John Doe', email='john@example.com')

# Add the user to the database5
session = Session()
session.add(user)
session.commit()

# Query the database for all users
users = session.query(User).all()
for user in users:
    print(user)

# Close the session
session.close()
