from sqlalchemy import *
from sqlalchemy import MetaData
#from sqlalchemy import create_engine
#from sqlalchemy import String
#from sqlalchemy import Column

#engine = create_engine('sqlite:///database.db', echo=True)
engine = create_engine('sqlite:///database.db')
metadata = MetaData()

users = Table('users', metadata, autoload_with=engine)

# Получаем всех пользователей из базы данных
#with engine.connect() as conn:
#    result = conn.execute(select(users))
#    all_users = result.fetchall()
#    
#    print("Все пользователи:")
#    for user in all_users:
#        print(user)
conn = engine.connect()
result = conn.execute(select(users))
all_users = result.fetchall()

print("Все пользователи:")
#for user in all_users:
#    print(user)
print(*all_users, sep="\n")
