from django.db import models

class Class(models.Model):
    name = models.CharField('Name', max_length=100, null=False, blank=False)
    name_subclass = models.CharField('SubClass', max_length=50, null=True, blank=True,
        help_text="Name of a subclass, ex 'A', 'B', '1', '2', ...")
    
    class Meta:
        verbose_name = "Class"
        verbose_name_plural = "Classes"

    def __str__(self):
        return self.name + " (" + self.name_subclass + ")"