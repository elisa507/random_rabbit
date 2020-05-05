import random
import time
from flask import render_template, redirect, url_for
from flask import current_app as app
from app.forms import OptionalFields

numbers = []
is_first_time = True
min_n = 0
max_n = 1000
max_t = 10


@app.route('/random_rabbit')
def random_rabbit():
    form = OptionalFields()
    global numbers, is_first_time, min_n, max_n, max_t
    numbers.append(random.randint(min_n, max_n))
    if not is_first_time:
        sleep_time = random.randint(1, max_t)
        time.sleep(sleep_time)
    string_numbers = ' '.join([str(elem) + ", " for elem in numbers])
    is_first_time = False
    return render_template('index.html',
                           form=form,
                           template='index',
                           str_num=string_numbers)


@app.route('/settings', methods=('GET', 'POST'))
def settings():
    form = OptionalFields()
    global min_n, max_n, max_t
    print("####")
    if form.validate_on_submit():
        print("***")
        print(form.data)
        if form.data['min_n']:
            min_n = int(form.data['min_n'])
        if form.data['max_n']:
            max_n = int(form.data['max_n'])
        if form.data['max_t']:
            max_t = int(form.data['max_t'])
        print(min_n, max_n, max_t)
        return redirect(url_for('random_rabbit'))
    return render_template('settings.html',
                           form=form,
                           template='form-template')


@app.route('/')
def main():
    return redirect(url_for('settings'))
