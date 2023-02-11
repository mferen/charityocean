from djongo import models
from django import forms
from djongo.models import ObjectIdField

class Charity(models.Model):
    name = models.CharField(max_length=100)
    link = models.CharField(max_length=255)

    class Meta:
        abstract = True
    # def __str__(self):
    #     return self.name
        
class CharityForm(forms.ModelForm):
    name = models.CharField(max_length=100)
    class Meta:
        model = Charity
        fields = (
            'name', 'link'
        )

class Country(models.Model):
    _id = ObjectIdField()
    name = models.CharField(max_length=255) 
    flaglink =  models.CharField(max_length=255)
    code =  models.CharField(max_length=10)
    charity = models.EmbeddedField(
        model_container=Charity,
        model_form_class=CharityForm
    )
    
    objects = models.DjongoManager()
    class Meta:
        db_table = "country"

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs) 
