from flask import Flask, render_template, request, url_for
import json
from random import choice


app = Flask(__name__)


@app.route('/member')
def member():
    with open('templates/member.json', encoding='utf-8') as file:
        f = json.load(file)
    return render_template('member.html', f=f, n=choice([1, 2, 0]))


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')