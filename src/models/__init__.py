from sqlalchemy import create_engine
import pymysql 
from sqlalchemy.orm import sessionmaker, declarative_base
#create a SQLAlchemy engine

DATABASE_URL = 'mysql+pymysql://root:admin@localhost:3306/db_sena'
engine = create_engine(DATABASE_URL, echo=True)
connection = engine.connect()
# Sesión para hacer consultas (INSERT, SELECT, etc.)
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = Session()
# Base para crear tus modelos de tablas en el futuro
Base = declarative_base()
#   
Base.metadata.create_all(bind=engine)