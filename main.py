from flask import Flask, render_template
import requests as rq

app = Flask(__name__)

count = 0


def exchange_rate():
    res = rq.get('https://www.cbr-xml-daily.ru/daily_json.js').json()['Valute']

    ans = ''

    for key in res.keys():
        val = res[key]
        nominal = val['Nominal']
        name = val['Name']
        value = val['Value']

        ans += f'{nominal} {name} стоит {value} руб.<br>'

    return ans


valutes = exchange_rate()


@app.route('/')
@app.route('/home')
def url_home():
    return render_template('index.html')


@app.route('/news')
def url_news():
    return render_template('web_page.html',
                           title='Страница с новостями',
                           text='Страница с новостями'
                           )


@app.route('/about')
def url_about():
    return render_template('web_page.html',
                           title='Сайт с новостями',
                           text='Сайт с новостями'
                           )


def fibonacci_value(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b

    return str(a)


@app.route('/fibonacci')
def url_fibonacci():
    a, b = 0, 1
    ans = ""

    for i in range(101):
        ans += str(a) + " "

        a, b = b, a + b

    return render_template('web_page.html',
                           title='Первые 100 чисел Фибоначчи',
                           text=ans
                           )


@app.route('/fibonacci/', defaults={'n': 0})
@app.route('/fibonacci/<int:n>')
def url_fibonacci_n(n):
    return fibonacci_value(n)


@app.route('/money')
def url_money():
    return render_template('web_page.html',
                           title='Курс валют',
                           text=valutes
                           )


@app.route('/random')
def url_random():
    params = {'method': 'getQuote', 'format': 'json'}
    res = rq.get('http://api.forismatic.com/api/1.0/', params=params).json()

    quote = res['quoteText']
    author = res['quoteAuthor']

    return render_template('web_page.html',
                           title='Цитата',
                           text=f'{quote}<br><br><b>{author}</b>'
                           )


@app.route('/count')
def url_count():
    global count
    count += 1

    return f'Вы зашли на эту страницу {count} раз(а)'


@app.route('/tutorial')
def url_tutorial():
    return render_template('tutorial.html')


if __name__ == "__main__":
    app.run(debug=True)
