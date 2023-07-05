from sqlalchemy import create_engine, text
import os
db_connection_string=os.environ['DB_CONNECTION_STRING']

engine = create_engine(db_connection_string,connect_args={
  "ssl":{
    "ssl_ca": "/etc/ssl/cert.pem"
  }
})

def load_jobs_from_db():
  # CREATE "LIST" OF all rows of database table with id
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    column_names = result.keys()
    result_dicts = []
    for row in result.all():
      result_dicts.append(dict(zip(column_names, row)))
    return (result_dicts)


      

