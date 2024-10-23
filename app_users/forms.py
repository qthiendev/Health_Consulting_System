from django import forms
from django.contrib.auth.models import User
from .models import Profile, MedicalHistory
from django.core.exceptions import ValidationError
import re
from datetime import datetime

class ProfileForm(forms.ModelForm):
    first_name = forms.CharField(label="Tên", max_length=150)
    last_name = forms.CharField(label="Họ", max_length=150)
    birthdate = forms.CharField(label="Ngày sinh (dd/mm/yyyy)", max_length=10)

    class Meta:
        model = Profile
        fields = ['birthdate', 'address', 'weight', 'height', 'exercise_level']

    def __init__(self, *args, **kwargs):
        # Fetch the user from kwargs
        self.user = kwargs.pop('user', None)
        super(ProfileForm, self).__init__(*args, **kwargs)

        # Initialize first_name and last_name from the User model
        if self.user:
            self.fields['first_name'].initial = self.user.first_name
            self.fields['last_name'].initial = self.user.last_name

    def clean_birthdate(self):
        birthdate = self.cleaned_data.get('birthdate')

        # Validate the format 'dd/mm/yyyy'
        if not re.match(r'^\d{2}/\d{2}/\d{4}$', birthdate):
            raise ValidationError("Ngày sinh phải theo định dạng 'dd/mm/yyyy'.")

        # Split the date and check if it's a valid date
        day, month, year = map(int, birthdate.split('/'))
        try:
            datetime(year, month, day)  # Will raise ValueError if the date is invalid
        except ValueError:
            raise ValidationError("Ngày sinh không hợp lệ.")

        return birthdate

    def save(self, commit=True):
        profile = super(ProfileForm, self).save(commit=False)

        # Save first_name and last_name to the User model
        if self.user:
            self.user.first_name = self.cleaned_data['first_name']
            self.user.last_name = self.cleaned_data['last_name']
            self.user.save()

        # Store birthdate as a string in 'dd/mm/yyyy' format
        profile.birthdate = self.cleaned_data['birthdate']

        if commit:
            profile.save()

        return profile

class MedicalHistoryForm(forms.ModelForm):
    class Meta:
        model = MedicalHistory
        fields = ['item']
