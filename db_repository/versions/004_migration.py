from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
nyt_articles = Table('nyt_articles', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('category', VARCHAR(length=128)),
    Column('rank', INTEGER),
    Column('title', VARCHAR(length=512)),
    Column('desc', VARCHAR(length=512)),
    Column('thumb', VARCHAR(length=256)),
    Column('link', VARCHAR(length=256)),
    Column('fetch_date', DATETIME),
    Column('day_id', DATE),
)

nyt_article = Table('nyt_article', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('category', String(length=128)),
    Column('rank', Integer),
    Column('title', String(length=512)),
    Column('desc', String(length=512)),
    Column('thumb', String(length=256)),
    Column('link', String(length=256)),
    Column('fetch_date', DateTime),
    Column('day_id', Date),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['nyt_articles'].drop()
    post_meta.tables['nyt_article'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['nyt_articles'].create()
    post_meta.tables['nyt_article'].drop()
