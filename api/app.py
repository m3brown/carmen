#!/usr/bin/env python
from flask import Flask, jsonify
from flask_cors import CORS
from datetime import datetime, timedelta
from iso3166 import countries
import random

app = Flask(__name__)
CORS(app)

class ChangingCountry:
  refresh_delta = timedelta(seconds=5)

  def __init__(self):
    self.latest_update = datetime.now()
    self.current_country = self.get_random_country()

  @staticmethod
  def get_random_country():
    return random.choice(list(countries))

  @property
  def country(self):
    self.refresh()
    return {
      'name': self.current_country.name,
      'code': self.current_country.numeric,
      'abbreviation': self.current_country.alpha2,
    }

  def refresh(self):
    now = datetime.now()
    elapsed = now - self.latest_update
    if elapsed > self.refresh_delta:
      self.current_country = self.get_random_country()
      self.latest_update = now

country = ChangingCountry()

@app.route('/')
def get_country():
  return jsonify(country.country)

if __name__ == '__main__':
  app.run(debug=True)
