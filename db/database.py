from sqlalchemy import create_engine, MetaData

engine = create_engine("mysql+pymysql://root:root@localhost:3320/test2")

meta = MetaData()

db = engine.connect()