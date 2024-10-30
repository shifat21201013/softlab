from django import forms
from .models import Donor


class DonorForm(forms.ModelForm):
    class Meta:
        model = Donor
        fields = [
            "blood_group",
            "quantity",
            "when_needed",
            "contact_number",
            "description",
        ]
