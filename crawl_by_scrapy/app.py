from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

def get_articles():
    conn = sqlite3.connect('vnexpress.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM articles')
    articles = cursor.fetchall()
    conn.close()
    return articles

@app.route('/')
def index():
    articles = get_articles()
    return render_template('index.html', articles=articles)

if __name__ == '__main__':
    app.run(debug=True)
