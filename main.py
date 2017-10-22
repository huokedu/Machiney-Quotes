from flask import Flask
from flask_bootstrap import Bootstrap
from flask import render_template
from random import randint, shuffle
from form import LoginForm

app = Flask(__name__)
app.config.from_object('config')
Bootstrap(app)

with open("source/Quotes.txt") as f:
    quotes = f.readlines()

with open("source/People.txt") as f:
    people = f.readlines()


def gen_carousel_quote(_img = ''):
    return {'quote_text': quotes[randint(0, len(quotes) - 1)],
            'person': people[randint(0, len(people) - 1)],
            'image': 'images/carousel/{}.jpg'.format(_img)}

def gen_block_quote(_img = ''):
    return {'quote_text': quotes[randint(0, len(quotes) - 1)],
            'person': people[randint(0, len(people) - 1)],
            'image': 'images/block/{}.jpg'.format(_img)}

@app.route('/')
def index():
    quote_list = [gen_carousel_quote(i) for i in range(1,3)]
    return render_template('index.html', quotes=quote_list)

@app.route('/latest')
def latest():
    quote_images = range(1,9)
    shuffle(quote_images)
    quote_list = [gen_block_quote(quote_images[i]) for i in range(8)]
    return render_template('list.html', quotes=quote_list)

@app.route('/quote')
def quote():
    quote_list = [gen_carousel_quote(i) for i in range(1,3)]
    return render_template('quote_page.html', quotes=quote_list)

# Test for forms
# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     form = LoginForm()
#     return render_template('form.html',
#                            title='Sign In',
#                            form=form)
