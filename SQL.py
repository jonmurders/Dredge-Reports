import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine('mssql+pyodbc://jamurders:Weeks123!@HMA-S-003/')

Session = sessionmaker(bind = engine)

session = Session()
