# Flask_tutorial_app

## Мой первый проект на Flask

### Адреса страниц:

* / и /home приведут на страницу с текстом "Главная страница"

* /news приведёт на страницу с текстом "Страница с новостями"

* /about приведёт на страницу с текстом "Сайт с новостями"

* /fibonacci приведёт на страницу, содержащую 100 первых чисел Фибоначчи

* /fibonacci/n приведёт на страницу с n-числом из последовательности Фибоначчи

* /money приведёт на страницу, содержащую информацию о текущем курсе валют в рублях

* /random приведёт на страницу со случайной цитатой и её автором

* /count приведёт на страницу, где указано сколько раз вы её посетили

### Как запустить проект?

В консоли прописываем такую команду:
~~~bash
flask --app main.py run
~~~

Если же произошла ошибка и вам нужно её исправить, тогда используйте эту команду:
~~~bash
flask --app main.py --debug run
~~~

После запуска Flask предупреждает, что был запущен сервер по адресу http://127.0.0.1:5000/
