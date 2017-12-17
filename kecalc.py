#!/usr/bin/env python

from flask import Flask, request, abort, jsonify
import MySQLdb

from dateconverter import DateConverter

app = Flask(__name__)
app.url_map.converters['date'] = DateConverter


# Test: http://localhost:5000/menu/2017-12-11

@app.route('/menu/<date:date>', methods=['GET'])
def menu(date):
  db = MySQLdb.connect(user='kecalc', passwd='k8Calc', db='kecalc')
  c = db.cursor(MySQLdb.cursors.DictCursor)
  c.execute('''SELECT `me_food`, `me_measure`,
   `me_amount`, `me_ke` FROM `menu` WHERE me_date=%s
   ORDER BY me_date_id ASC''', (date,))
  
  return jsonify(c.fetchall())

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
