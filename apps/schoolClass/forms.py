from .models import Class
from datetime import datetime as dt

class StudentForm():    
    def __init__(self, data, allowAllData):
        self.form = {}
        all_fields = [f.name for f in Class._meta.get_fields()]
        forbidden_update_fields = ['pk']
        for field in data:
            field = field if field != 'id' else 'pk'
            if field in all_fields:
                if allowAllData or (not allowAllData and field not in forbidden_update_fields):
                    self.form[field] = data[field]