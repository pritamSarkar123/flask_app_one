from carMarket import app
from carMarket.models import Item
from flask import render_template


@app.route('/')
@app.route('/home')
def to_home():
    items = Item.query.all()
    return render_template('home.html', items=items)
