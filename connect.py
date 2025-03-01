from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker

url_to_db = "postgresql://postgres:0967181951@localhost:5432/my-db"
engine = create_engine(url_to_db)
Session = sessionmaker(bind=engine)
session = Session()
