#!/usr/bin/env python

from flask import Flask, jsonify
import MySQLdb

from dateconverter import DateConverter

app = Flask(__name__)
app.url_map.converters['date'] = DateConverter

# Test: http://localhost:5000/menu/2017-12-11
# Test: http://localhost:5000/params

DBNAME = 'kecalc'
DBUSER = 'kecalc'
DBPASS = 'k8Calc'

@app.route('/menu/<date:date>', methods=['GET'])
def menu(date):
  db = MySQLdb.connect(user=DBUSER, passwd=DBPASS, db=DBNAME)
  c = db.cursor(MySQLdb.cursors.DictCursor)
  c.execute('''SELECT `me_food`, `me_measure`,
   `me_amount`, `me_ke` FROM `menu` WHERE me_date=%s
   ORDER BY me_date_id ASC''', (date,))
  result = c.fetchall()
  c.close()
  db.close()
  
  return jsonify(result)

@app.route('/params', methods=['GET'])
def params():
  db = MySQLdb.connect(user=DBUSER, passwd=DBPASS, db=DBNAME)
  c = db.cursor(MySQLdb.cursors.DictCursor)
  c.execute('SELECT `pa_name`, `pa_value` FROM `params`')
  result = {}
  for row in c:
    result[row['pa_name']] = row['pa_value']
  c.close()
  db.close()

  return jsonify(result)

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
