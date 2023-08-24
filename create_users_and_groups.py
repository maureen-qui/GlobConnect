from app import db
from app.models import User, CollaborationGroup

def create_users_and_groups():
    # Create a new user
    new_user = User(username='john_doe', email='john@example.com', password='hashed_password')
    db.session.add(new_user)
    
    # Create a new collaboration group
    new_group = CollaborationGroup(name='Tech Enthusiasts', description='Group for tech discussions', creator=new_user)
    db.session.add(new_group)
    
    # Commit the changes to the database
    db.session.commit()

if __name__ == '__main__':
    create_users_and_groups()
    print("Users and groups created successfully!")
