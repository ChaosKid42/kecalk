#!/usr/bin/env python

from flask import Flask, jsonify
from sqlalchemy import create_engine, Column, Integer, Table,\
  String, Sequence, Date, Float, MetaData, select
from dateconverter import DateConverter

# Test: http://localhost:5000/menu/2017-12-11
# Test: http://localhost:5000/params

DBNAME = 'kecalc'
DBUSER = 'kecalc'
DBPASS = 'k8Calc'

engine = create_engine('mysql+mysqldb://{}:{}@/{}'.format(DBUSER, 
  DBPASS, DBNAME), pool_recycle=3600)

metadata = MetaData()
tblMenu = Table('menu', metadata,
  Column('me_id', Integer, Sequence('me_id_seq'), primary_key=True),
  Column('me_date', Date(), nullable=False),
  Column('me_date_id', Integer, nullable=False),
  Column('me_food', String(15), nullable=False),
  Column('me_measure', String(7), nullable=False),
  Column('me_amount', String(10), nullable=False),
  Column('me_ke', Float(), nullable=False)
)

tblParams = Table('params', metadata,
  Column('pa_id', Integer, Sequence('pa_id_seq'), primary_key=True),
  Column('pa_name', String(10), nullable=False),
  Column('pa_value', String(10), nullable=False),
)

metadata.create_all(engine)

app = Flask(__name__)
app.url_map.converters['date'] = DateConverter

@app.route('/menu/<date:date>', methods=['GET'])
def menu(date):

  s = select([tblMenu.c.me_food, tblMenu.c.me_measure,
    tblMenu.c.me_amount, tblMenu.c.me_ke]).\
      where(tblMenu.c.me_date == date).\
      order_by(tblMenu.c.me_date_id).limit(10)

  conn = engine.connect()
  result = conn.execute(s)
  conn.close()

  return jsonify([dict(r) for r in result])


@app.route('/params', methods=['GET'])
def params():
  s = select([tblParams.c.pa_name, tblParams.c.pa_value])

  conn = engine.connect()
  result = conn.execute(s)
  conn.close()

  return jsonify({r['pa_name']: r['pa_value'] for r in result})


# run the app for debug purposes.
if __name__ == '__main__':
  app.run(debug=True)
# this is used in production
else:
  import logging
  from logging import FileHandler
  file_handler = FileHandler('/var/log/kecalc.log')
  file_handler.setLevel(logging.WARNING)
  file_handler.setFormatter(logging.Formatter('%(asctime)s %(message)s'))
  app.logger.addHandler(file_handler)
