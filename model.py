import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy import inspect
engine = create_engine('mysql://root:varunasd1@localhost/test')
with engine.connect() as con:

    rs = con.execute('SELECT * FROM user natural join booking where user.id<2').fetchall()

    for row in rs:
        print(row[2])
print(rs[0])