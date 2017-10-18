from flask import Flask
from flask_bootstrap import Bootstrap
from flask import render_template
from random import randint

app = Flask(__name__)
Bootstrap(app)

@app.route('/home')
def index():
    return render_template('home.html')

quotes = '''Yes is my fate in that mind is true
Try a little bit is enjoying any other than a flame
The property, look like with stars shakes and actions
You have he written to feel the spine men
Be a phase is the straight of our human truth
Why come into you get every money in dying
Then what you will otherwise no make such mistakes
How me scratch twice out even no way long tv it
Who you can't afford any day would write that'll each other upon my soul
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
Mahatma Gandhi'''.split('\n')

@app.route('/quote')
def quote():
    display_quote = quotes[randint(0, len(quotes) - 1)]
    display_person = people[randint(0, len(people) - 1)]
    return render_template('quote_page.html', quote=display_quote, name=display_person)
