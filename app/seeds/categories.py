from app.models import db, Category, environment, SCHEMA
import datetime
from sqlalchemy.sql import text


def seed_categories():
    italian = Category(name='Italian')
    mexican = Category(name='Mexican')
    middle_eastern = Category(name='Middle Eastern')
    japanese = Category(name='Japanese')
    american = Category(name='American')

    db.session.add_all([italian, mexican, middle_eastern, japanese, american])
    db.session.commit()




def undo_categories():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.users RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM users"))

    db.session.commit()
