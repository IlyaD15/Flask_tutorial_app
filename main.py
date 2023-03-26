from flask import Flask
import requests as rq

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    return "Главная страница"


@app.route('/news')
def news():
    return "Страница с новостями"


@app.route('/about')
def about():
    return "Сайт с новостями"


@app.route('/fibonacci')
def fibonacci():
    a, b = 0, 1
    ans = ""

    for i in range(101):
        ans += str(a) + " "

        a, b = b, a + b

    return ans


@app.route('/money')
def money():
    res = rq.get('https://www.cbr-xml-daily.ru/daily_json.js')
    res = res.json()['Valute']

    ans = ''

    for key in res.keys():
        val = res[key]
        nominal = val['Nominal']
        name = val['Name']
        value = val['Value']

        ans += f'{nominal} {name} стоит {value} руб.<br>'

    return ans


@app.route('/random')
def random():
    params = {'method': 'getQuote', 'format': 'json'}
    res = rq.get('http://api.forismatic.com/api/1.0/', params=params).json()

    quote = res['quoteText']
    author = res['quoteAuthor']

    return f'{quote}<br><br>{author}'


if __name__ == "__main__":
    app.run(debug=True)
