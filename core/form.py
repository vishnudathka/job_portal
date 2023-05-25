from django import forms
from .models import JobCreateModel, CategoryModel

class JobForm(forms.ModelForm):
    class Meta:
        model = JobCreateModel
        fields = ["jobtitle","jobdescription","nature","salary","company","location","deadline","company_description","company_website","responsibilities","qualifications","image","category"]

class CategoryForm(forms.ModelForm):
    class Meta:
        model = CategoryModel
        fields = ["name"]
