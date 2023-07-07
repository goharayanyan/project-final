import openpyxl
from polls.models import Category



def reading():
    wb = openpyxl.load_workbook('/Users/inakarapetyan/Desktop/finalik/file.xlsx')               #stegh excel filei pathy
    ws = wb['Sheet1']  
    intern_id = 1
    for row in ws.iter_rows(min_row=2):  # start at row 2 to skip header row
        if all(cell.value is None for cell in row):
            continue
        my_object = Category()
        my_object.name = row[2].value
        my_object.code = row[0].value
        intern_id+=1
        print(my_object.id, my_object.code, my_object.name)
        # repeat for all fields in your model
        my_object.save()

    return True