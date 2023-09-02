from django.forms import ModelForm
from .models import CarDetail

class CarAddForm(ModelForm):
    class Meta:
        model = CarDetail
        fields =["Car_Name","Car_Brand","Car_Discription","Car_Rent","Car_Image"]