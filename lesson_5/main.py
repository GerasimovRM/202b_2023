from database.base_meta import session_factory
from database.user import User


def create_user():
    session = session_factory()
    user1 = User(full_name="User 1", phone="5464576548")
    session.add(user1)
    session.commit()
    session.close()


def select_user():
    session = session_factory()
    # user = session.get(User, 1)
    # user = session.query(User).get(1)
    user = session.query(User).where(User.id == 1).first()
    print(user.id, user.phone, user.full_name)
    session.close()


def update_user():
    session = session_factory()
    user = session.query(User).where(User.id == 1).first()
    user.phone = '8800333444555'
    print(user.id, user.phone, user.full_name)
    session.commit()
    session.close()


def delete_user():
    session = session_factory()
    user = session.query(User).where(User.id == 1).first()
    session.delete(user)
    session.commit()
    session.close()


# create_user()  # C
# select_user()  # R
# update_user()  # U
delete_user()    # D
