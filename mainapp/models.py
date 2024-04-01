from django.db import models

class TableData(models.Model):
    column1 = models.CharField(max_length=200)
    column2 = models.CharField(max_length=200)
    column3 = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.column1} - {self.column2} - {self.column3}'
