import pandas as pd
import numpy as np
import os
import xlrd
import re
from otti import db, models

TTI_file = '/var/www/otti/data/Texas Transfer Inventory_2016-17.xls'

xl_workbook = xlrd.open_workbook(TTI_file)
sheet_names = xl_workbook.sheet_names()
sheet_names = sheet_names[2:] # Names of institutions begin in third entry

def get_institution_name(sheet_name):
    xl_sheet = xl_workbook.sheet_by_name(sheet_name)
    col = xl_sheet.col(0)
    for entry in col:
        if entry != '':
            return str(entry.value)
    return None

for sheet_name in sheet_names:
    stuff = get_institution_name(sheet_name).split(' ')
    new_stuff = [e for e in stuff if e != '']
    college_name =' '.join(new_stuff)
    inst = models.Institution(name=college_name)
    db.session.add(inst)

db.session.commit()
