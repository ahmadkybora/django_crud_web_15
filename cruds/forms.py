from django import forms
from .models import Crud

class CrudForm(forms.ModelForm):
    class Meta:
        model = Crud
        fields = ("title", )

    title = forms.CharField(max_length=50)

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) < 2:
            raise forms.ValidationError("invlaid title")
        return title
    