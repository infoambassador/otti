from flask import render_template, url_for
from otti import app, db, models
from .forms import InstitutionForm

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html',
                           title='About')

@app.route('/inventory', methods=['GET','POST'])
def inventory():
    return render_template('inventory.html',
                           title='Inventory')

@app.route('/inventory/offerings-by-institution', methods=['GET','POST'])
def offerings():
    form = InstitutionForm()
    form.institution_select_field.choices = [(inst.id,inst.name) for inst in models.Institution.query.all()]
    inst_id = form.institution_select_field.data
    school = None
    courses = None
    if inst_id:
        school = models.Institution.query.filter_by(id=form.institution_select_field.data).first().name
        courses = models.Course.query.filter_by(institution_id=inst_id)
    return render_template('offerings-by-institution.html',
                           title='Offerings',
                           form=form,
                           seletion=school,
                           courses=courses)

'''

    


    try:
        
    except:
        pass
        school = school_query.name
        return render_template('test.html',
                               selection=school,
                               courses=courses)
    return render_template('offerings-by-institution.html',
                           title='Offerings by Institution',
                           form=form)
'''

