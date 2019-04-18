
from django import forms
from autos.models import Auto
from django.core.files.uploadedfile import InMemoryUploadedFile
from autos.humanize import naturalsize

# https://docs.djangoproject.com/en/2.1/topics/http/file-uploads/
# https://stackoverflow.com/questions/2472422/django-file-upload-size-limit
# https://stackoverflow.com/questions/32007311/how-to-change-data-in-django-modelform
# https://docs.djangoproject.com/en/2.1/ref/forms/validation/#cleaning-and-validating-fields-that-depend-on-each-other

# Create the form class.
class CreateForm(forms.ModelForm):
    
    class Meta:
        model = Auto
        fields = ['name', 'detail', 'mileage']  # Picture is manual

    def clean(self) :
        cleaned_data = super().clean()
       
    def save(self, commit=True) :
        instance = super(CreateForm, self).save(commit=False)

        if commit:
            instance.save()

        return instance

class CommentForm(forms.Form):
    comment = forms.CharField(required=True, max_length=500, min_length=3, strip=True)