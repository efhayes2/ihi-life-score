from flask import Flask, render_template, request, flash, url_for, session, redirect
from flask_bootstrap import Bootstrap

from compute import compute_bmi, compute_stroke_risk, compute_heart_attack_risk, compute_cholesterol_risk
from model import UserDataForm, BmiForm, HeartAttackDataForm, NameForm, StrokeDataForm, CholesterolDataForm

app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config['SECRET_KEY'] = 'iko-iko'


@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash('Looks like you have changed your name!')
        session['name'] = form.name.data
        return redirect(url_for('index'))
    return render_template('index.html', form=form, name=session.get('name'))


@app.route('/user', methods=['GET', 'POST'])
def user():
    form = UserDataForm(request.form)
    update_session_variables_1(form)
    update_session_variables_2(form)
    update_session_variables_3(form)

    if request.method == 'POST' and form.validate():
        result, time_str = compute_bmi(form.Weight.data, form.Height.data)
    else:
        result = None

    return render_template('view.html', form=form, result=result)


@app.route('/stroke', methods=['GET', 'POST'])
def stroke_data():
    form = StrokeDataForm(request.form)
    update_session_variables_1(form)
    update_session_variables_2(form)

    if request.method == 'POST' and form.validate():
        result, time_str = compute_stroke_risk(form.SystolicBloodPressure.data)
    else:
        result = None

    return render_template('view.html', form=form, result=result)


def update_session_variables_1(form):
    if form.Age:
        session['age'] = form.Age
    if form.Gender:
        session['weight'] = form.Gender
    if form.ActivityLevel:
        session['activity'] = form.ActivityLevel


def update_session_variables_2(form):
    if form.SystolicBloodPressure:
        session['SystolicBloodPressure'] = form.SystolicBloodPressure
    if form.DiastolicBloodPressure:
        session['DiastolicBloodPressure'] = form.DiastolicBloodPressure
    if form.Diabetes:
        session['diabetes'] = form.Diabetes
    if form.SmokingHistory:
        session['smoking'] = form.SmokingHistory


def update_session_variables_3(form):
    if form.Height:
        session['height'] = form.Height
    if form.Weight:
        session['weight'] = form.Weight
    if form.HeartHistory:
        session['heart'] = form.HeartHistory
    if form.SmokingHistory:
        session['smoking'] = form.SmokingHistory


def update_session_variables_4(form):
    if form.Age:
        session['age'] = form.Age
    if form.Height:
        session['height'] = form.Height
    if form.Weight:
        session['weight'] = form.Weight
    if form.SystolicBloodPressure:
        session['SystolicBloodPressure'] = form.SystolicBloodPressure
    if form.DiastolicBloodPressure:
        session['DiastolicBloodPressure'] = form.DiastolicBloodPressure
    if form.Diabetes:
        session['diabetes'] = form.Diabetes
    if form.HeartHistory:
        session['heart'] = form.HeartHistory
    if form.SmokingHistory:
        session['smoking'] = form.SmokingHistory
    if form.ActivityLevel:
        session['activity'] = form.ActivityLevel


@app.route('/bmi', methods=['GET', 'POST'])
def bmi():
    form = BmiForm(request.form)
    if request.method == 'POST' and form.validate():
        result, time_str = compute_bmi(form.Weight.data, form.Height.data)
    else:
        result = None

    return render_template('view.html', form=form, result=result)


@app.route('/heart', methods=['GET', 'POST'])
def heart_attack_assessment():
    form = HeartAttackDataForm(request.form)
    if request.method == 'POST' and form.validate():
        result, time_str = compute_heart_attack_risk(form.SystolicBloodPressure.data)
    else:
        result = None

    return render_template('view.html', form=form, result=result)


def update_session_variables_cholesterol(form):
    if form.Age:
        session['age'] = form.Age
    if form.Gender:
        session['gender'] = form.Gender
    if form.LDL:
        session['ldl'] = form.LDL
    if form.HDL:
        session['hdl'] = form.HDL
    if form.Age:
        session['triglycerides'] = form.Triglycerides


@app.route('/cholesterol', methods=['GET', 'POST'])
def cholesterol_risk_assessment():
    form = CholesterolDataForm(request.form)
    update_session_variables_cholesterol(form)
    if request.method == 'POST' and form.validate():
        result, time_str = compute_cholesterol_risk(form.HDL.data, form.LDL.data, form.Gender.data)
    else:
        result = None

    return render_template('view.html', form=form, result=result)


if __name__ == '__main__':
    app.run(debug=True)
