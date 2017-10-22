from flask import Flask
from flask_bootstrap import Bootstrap
from flask import render_template
from random import randint
from form import LoginForm

app = Flask(__name__)
app.config.from_object('config')
Bootstrap(app)

quotes = '''Yes is my fate in that mind is true.
Try a little bit is enjoying any other than a flame
The property, look like with stars shakes and actions
You have he written to feel the spine men
Be a phase is the straight of our human truth
Why come into you get every money in dying
Then what you will otherwise no make such mistakes
Who you can't afford any day would write that'll each other upon my soul
Ones needs a sings to be, taught, but as touched, for grace.
Drink with their veil or a private refuge remains growth
Achieve, and character's entire unity in his bicycle
Who's it's a simple word for being
Everything is always a good thing to the lyrics
Safe was very much and stops a democratic world
Why come that I find do really see the films
Esteem in a single way we are a bad challenge
Huge school, all ballroom writing and in the sea
Achieve orders without being a precious of resentment or my league start
Wow is pretty voyage and piano to terrorists our learning than brad meets
Singing and the human part of, you know anything
There remain ones to make people know anything in nor plays
Never can't get any of those things now
Repeat today or finish into a little old ocean'''.split('\n')

people = '''Marilyn Monroe
Abraham Lincoln
Mother Teresa
John F. Kennedy
Martin Luther King
Nelson Mandela
Winston Churchill
Bill Gates
Muhammad Ali
Mahatma Gandhi
Paul McCartney
Plato
Queen Elizabeth I
Queen Victoria
John M Keynes
Mikhail Gorbachev
Jawaharlal Nehru
Leonardo da Vinci
Louis Pasteur
Leo Tolstoy
Pablo Picasso
Vincent Van Gogh
Franklin D. Roosevelt
Pope John Paul I
Thomas Edison
Rosa Parks
Lyndon Johnson
Oprah Winfrey
Indira Gandhi
Eva Peron
Benazir Bhutto
Desmond Tutu
Dalai Lama
Walt Disney
Neil Armstrong
Peter Sellers
Barack Obama
Malcolm X
J.K.Rowling
Richard Branson
Angelina Jolie
Jesse Owens
Ernest Hemingway
John Lennon
Henry Ford
Haile Selassie
Ludwig Beethoven'''.split('\n')

def gen_quote(_img):
    return {'quote_text': quotes[randint(0, len(quotes) - 1)],
            'person': people[randint(0, len(people) - 1)],
            'image': 'pic{}.jpg'.format(_img)}

@app.route('/home')
def index():
    quote_list = [gen_quote(i) for i in range(4,7)]
    return render_template('home.html', quotes=quote_list)

@app.route('/quote')
def quote():
    quote_list = [gen_quote(i) for i in range(4,7)]
    return render_template('quote_page.html', quotes=quote_list)

# Test for forms
# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     form = LoginForm()
#     return render_template('form.html',
#                            title='Sign In',
#                            form=form)
