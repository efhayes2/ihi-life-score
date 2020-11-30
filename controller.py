from model import UserDataForm, BmiForm, HeartAttackDataForm
from flask import Flask, render_template, request
from compute import compute_bmi
import sys
from flask_bootstrap import Bootstrap

try:
    template_name = sys.argv[1]
except IndexError:
    template_name = 'view0'

app = Flask(__name__)
bootstrap = Bootstrap(app)


@app.route('/user_data', methods=['GET', 'POST'])
def user_data():
    form = UserDataForm(request.form)
    if request.method == 'POST' and form.validate():
        result = compute_bmi(form.Weight.data, form.Height.data)
    else:
        result = None

    return render_template('view.html', form=form, result=result)


@app.route('/bmi', methods=['GET', 'POST'])
def bmi():
    form = BmiForm(request.form)
    if request.method == 'POST' and form.validate():
        result = compute_bmi(form.Weight.data, form.Height.data)
    else:
        result = None

    return render_template('view.html', form=form, result=result)


@app.route('/heart_attack_assessment', methods=['GET', 'POST'])
def heart_attack_assessment():
    form = HeartAttackDataForm(request.form)
    if request.method == 'POST' and form.validate():
        result = None  # compute_bmi(form.Weight.data, form.Height.data)
    else:
        result = None

    return render_template('view.html', form=form, result=result)


if __name__ == '__main__':
    app.run(debug=True)
