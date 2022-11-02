from django import forms
from user_profile.models import Profile
from user_profile.models import PhysicalInfo

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'phone', 'email', 'role']
        widget = forms.Select(choices=fields)

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.some_flag = True
        if commit:
            instance.save()
            self.save_m2m()
        return instance

class PhysicalInfoForm(forms.ModelForm):
    class Meta:
        model = PhysicalInfo
        fields = ['gender', 'weight', 'height', 'age']
    
    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.some_flag = True
        if commit:
            instance.save()
            self.save_m2m()
        return instance