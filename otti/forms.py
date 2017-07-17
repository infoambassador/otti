from flask_wtf import Form
from wtforms import SelectField
from otti import db, models

class InstitutionForm(Form):
    institution_select_field = SelectField(u'Inst', coerce=int)
