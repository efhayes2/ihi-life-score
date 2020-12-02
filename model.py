from wtforms import Form, FloatField,  SelectField, validators, StringField, SubmitField, HiddenField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired


v = [validators.InputRequired()]


class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    submit = SubmitField('Submit')


class UserDataForm(Form):
    choices = ['female', 'male']
    Gender = SelectField(label='Gender', choices=choices, validators=v)

    Age = FloatField(label='Age', default=50.0, validators=v)
    Weight = FloatField(label='Weight (lbs)', default=180, validators=v)
    Height = FloatField(label='Height (in)', default=70, validators=v)
    LDL = FloatField(label='LDL', default=100, validators=v)
    HDL = FloatField(label='HDL', default=100, validators=v)
    SystolicBloodPressure = FloatField(label='Systolic Blood Pressure', default=120, validators=v)
    DiastolicBloodPressure = FloatField(label='Diastolic Blood Pressure', default=80,validators=v)

    choices = ['no', 'yes']
    Diabetes = SelectField(label='Do you have diabetes?', choices=choices, validators=v)
    HeartHistory = SelectField(label='Have you had a heart attack?', choices=choices, validators=v)

    choices = ['never', 'quit over 5 years ago', 'quit less than 5 years ago',
               '< 1 pack / day' , '> 1 pack / day']
    SmokingHistory = SelectField(label='Smoking history', choices=choices, validators=v)

    choices = ['sedentary', 'light', 'moderate', 'very active']
    ActivityLevel = SelectField(label='Activity Level', choices=choices, validators=v)

    # GraphLink = HiddenField()


class HeartAttackDataForm(Form):

    choices = ['female', 'male']
    Gender = SelectField(label='Gender', choices=choices, validators=v)
    Age = FloatField(label='Age', default=50.0, validators=v)
    Weight = FloatField(label='Weight (lbs)', default=180, validators=v)
    Height = FloatField(label='Height (in)', default=70, validators=v)
    LDL = FloatField(label='LDL', default=100, validators=v)
    HDL = FloatField(label='HDL', default=100, validators=v)
    SystolicBloodPressure = FloatField(label='Systolic Blood Pressure', default=120, validators=v)
    DiastolicBloodPressure = FloatField(label='Diastolic Blood Pressure', default=80,validators=v)

    choices = ['no', 'yes']
    Diabetes = SelectField(label='Do you have diabetes?', choices=choices, validators=v)
    HeartHistory = SelectField(label='Have you had a heart attack?', choices=choices, validators=v)

    choices = ['never', 'quit over 5 years ago', 'quit less than 5 years ago',
               '< 1 pack / day' , '> 1 pack / day']
    SmokingHistory = SelectField(label='Smoking history', choices=choices, validators=v)

    choices = ['sedentary', 'light', 'moderate', 'very active']
    ActivityLevel = SelectField(label='Activity Level', choices=choices, validators=v)
    # GraphLink = HiddenField()


class DiabetesDataForm(Form):
    choices = ['female', 'male']
    Gender = SelectField(label='Gender', choices=choices, validators=v)
    Age = FloatField(label='Age', default=50.0, validators=v)

    choices = ['0', '1', '2']
    ParentsDiabetic = SelectField(label='How many parents have diabetes history?', choices=choices, validators=v)
    Girth = FloatField(label='Girth (in.)', default=32.0, validators=v)
    choices = ['sedentary', 'light', 'moderate', 'very active']
    ActivityLevel = SelectField(label='Activity Level', choices=choices, validators=v)
    # GraphLink = HiddenField()


class CholesterolDataForm(Form):
    choices = ['female', 'male']
    Gender = SelectField(label='Gender', choices=choices, validators=v)
    Age = FloatField(label='Age', default=50.0, validators=v)

    LDL = FloatField(label='LDL', default=100, validators=v)
    HDL = FloatField(label='HDL', default=50, validators=v)
    Triglycerides = FloatField(label='Triglycerides', default=150, validators=v)
    # GraphLink = HiddenField()


class StrokeDataForm(Form):

    choices = ['female', 'male']
    Gender = SelectField(label='Gender', choices=choices, validators=v)

    Age = FloatField(label='Age', default=50.0, validators=v)
    SystolicBloodPressure = FloatField(label='Systolic Blood Pressure', default=120, validators=v)
    DiastolicBloodPressure = FloatField(label='Diastolic Blood Pressure', default=80,validators=v)

    choices = ['no', 'yes']
    Diabetes = SelectField(label='Do you have diabetes?', choices=choices, validators=v)
    HBP_medication = SelectField(label='Do you take high-blood pressure medication?', choices=choices, validators=v)
    Irregular_ECG = SelectField(label='Have you had an irregular ECG?', choices=choices, validators=v)
    HeartHistory = SelectField(label='Have you had a heart attack?', choices=choices, validators=v)

    choices = ['never', 'quit over 5 years ago', 'quit less than 5 years ago',
               '< 1 pack / day' , '> 1 pack / day']
    SmokingHistory = SelectField(label='Smoking history', choices=choices, validators=v)

    choices = ['sedentary', 'light', 'moderate', 'very active']
    ActivityLevel = SelectField(label='Activity Level', choices=choices, validators=v)

    # GraphLink = HiddenField()


class BmiForm(Form):
    Weight = FloatField(label='Weight (lbs)', default=180, validators=v)
    Height = FloatField(label='Height (in)', default=70, validators=v)
    # GraphLink = HiddenField()


# {% extends "base.html" %}
# {% import "bootstrap/wtf.html" as wtf %}
#
# {% block title %}LifeScore{% endblock %}
#
# {% block page_content %}
# <div class="page-header">
#     <h1>Hello, {% if name %}{{ name }}{% else %}Stranger{% endif %}!</h1>
# </div>
# {{ wtf.quick_form(form) }}
# <p><input type=submit value=Submit></p>
# {% endblock %}
#
# <p>
# {% if result != None %}
# <img src="{{ result }}" width=500 alt="">
# {% endif %}
# </p>