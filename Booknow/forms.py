from django.forms import ModelForm
from .models import Book

class BookAddForm(ModelForm):
    class Meta:
        model = Book
        fields =["numberofdays","Booker_Name","Address","Id_Proof"]