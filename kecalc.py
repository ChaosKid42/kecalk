#!/usr/bin/env python

from flask import Flask, jsonify
import sqlalchemy

from dateconverter import DateConverter

app = Flask(__name__)
app.url_map.converters['date'] = DateConverter

# Test: http://localhost:5000/menu/2017-12-11
# Test: http://localhost:5000/params

DBNAME = 'kecalc'
DBUSER = 'kecalc'
DBPASS = 'k8Calc'

connstr = 'mysql+mysqldb://{}:{}@/{}'.format(DBUSER, DBPASS, DBNAME)
engine = sqlalchemy.create_engine(connstr, pool_recycle=3600)

@app.route('/menu/<date:date>', methods=['GET'])
def menu(date):
  s = sqlalchemy.text('''SELECT `me_food`, `me_measure`,
    `me_amount`, `me_ke` FROM `menu` WHERE me_date=:date
    ORDER BY me_date_id ASC LIMIT 10''')
  conn = engine.connect()
  result = conn.execute(s, date = date).fetchall()
  conn.close()
  
  return jsonify([dict(r) for r in result])

@app.route('/params', methods=['GET'])
def params():
  s = sqlalchemy.text('SELECT `pa_name`, `pa_value` FROM `params`')
  conn = engine.connect()
  result = conn.execute(s).fetchall()
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
