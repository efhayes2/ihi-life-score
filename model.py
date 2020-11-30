from wtforms import Form, FloatField, BooleanField, RadioField, SelectField, validators
from math import pi


class UserDataForm(Form):
    v = [validators.InputRequired()]
    Age = FloatField(label='Age', default=1.0, validators=v)
    Weight = FloatField(label='Weight (lbs)', default=0, validators=v)
    Height = FloatField(label='Height (in)', default=0, validators=v)
    SystolicBloodPressure = FloatField(label='Systolic Blood Pressure', default=0, validators=v)
    DiastolicBloodPressure = FloatField(label='Diastolic Blood Pressure', default=0,validators=v)

    choices = ['no', 'yes']
    Diabetes = SelectField(label='Do you have diabetes?', choices=choices, validators=v)
    HeartHistory = SelectField(label='Have you had a heart attack?', choices=choices, validators=v)

    choices = ['never', 'quit over 5 years ago', 'quit less than 5 years ago',
               '< 1 pack / day' , '> 1 pack / day']
    SmokingHistory = SelectField(label='Smoking history', choices=choices, validators=v)

    choices = ['sedentary', 'light', 'moderate', 'very active']
    ActivityLevel = SelectField(label='Activity Level', choices=choices, validators=v)



class HeartAttackDataForm(Form):
    Age = FloatField(
        label='Age', default=1.0,
        validators=[validators.InputRequired()])
    LDL = FloatField(
        label='Weight (lbs)', default=0,
        validators=[validators.InputRequired()])
    HDL = FloatField(
        label='Height (in)', default=0,
        validators=[validators.InputRequired()])
    SystolicBloodPressure = FloatField(label='Systolic Blood Pressure', default=0,
                                       validators=[validators.InputRequired()])
    DiastolicBloodPressure = FloatField(label='Diastolic Blood Pressure', default=0,
                                        validators=[validators.InputRequired()])
    Smoker = BooleanField(label='Do you smoke?', default=0, validators=[validators.InputRequired()])
    Diabetes = BooleanField(label='Do you have Diabetes?', default=0, validators=[validators.InputRequired()])
    choices = [('0-2', 'sedentary'), ('2-5', 'light'), ('6-10', 'moderate'), ('10+', 'very active')]
    # ActivityLevel = RadioField(label='Activity Level', choices=choices, validators=[validators.InputRequired()])
    ActivityLevel = SelectField(label='Activity Level', choices=choices, validators=[validators.InputRequired()])


class BmiForm(Form):
    Weight = FloatField(
        label='Weight (lbs)', default=0,
        validators=[validators.InputRequired()])
    Height = FloatField(
        label='Height (in)', default=0,
        validators=[validators.InputRequired()])
