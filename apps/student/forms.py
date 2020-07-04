from .models import Student
from datetime import datetime as dt

class StudentForm():    
    def __init__(self, data, allowAllData):
        self.form = {}
        all_fields = [f.name for f in Student._meta.get_fields()]
        forbidden_update_fields = ['pk', 'registration']
        for field in data:
            field = field if field != 'id' else 'pk'
            if field in all_fields:
                if allowAllData or (not allowAllData and field not in forbidden_update_fields):
                    if field == 'date_birth':
                        self.form[field] = dt.strptime(data[field], "%d/%m/%Y").date()
                    else:
                        self.form[field] = data[field]