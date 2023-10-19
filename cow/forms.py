from django import forms
from .models import CowRegistration ,MasterVaccine

class CowRegistrationForm(forms.ModelForm):
    class Meta:
        model = CowRegistration
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(CowRegistrationForm, self).__init__(*args, **kwargs)
        
        # If a disease is selected, filter the available vaccines based on that disease
        selected_disease = self.initial.get('desease_name', None)
        if selected_disease:
            self.fields['vaccine_name'].queryset = selected_disease.masterdesease.mastermastervaccine_set.all()
        else:
            self.fields['vaccine'].queryset = MasterVaccine.objects.none()
