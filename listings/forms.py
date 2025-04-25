from django import forms
from django.forms import inlineformset_factory

from .models import *


STATE_CHOICES = [
    ("Izvorno", "Izvorno"),
    ("Novo", "Novo"),
    ("Renovirano", "Renovirano"),
    ("Lux", "Lux"),
]
HEATING_CHOICES = [
    ("Centralno", "Centralno"),
    ("Etažno", "Etažno"),
    ("Struja", "Struja"),
    ("Gas", "Gas"),
    ("TA", "TA"),
]
EQUIPMENT_CHOICES = [
    ("Namešten", "Namešten"),
    ("Polunamešten", "Polunamešten"),
    ("Prazan", "Prazan"),
]


class BuildingForm(forms.ModelForm):
    class Meta:
        model = Building
        fields = "__all__"


class ApartmentForm(forms.ModelForm):
    state = forms.ChoiceField(choices=STATE_CHOICES, label="Stanje")
    heating = forms.ChoiceField(choices=HEATING_CHOICES, label="Grejanje")
    equipment = forms.ChoiceField(choices=EQUIPMENT_CHOICES, label="Opremljenost")

    class Meta:
        model = Apartment
        fields = "__all__"
        exclude = ["building"]


class TermsForm(forms.ModelForm):
    class Meta:
        model = Terms
        fields = "__all__"
        widgets = {"available": forms.DateInput(attrs={"type": "date"})}


class ListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = "__all__"
        exclude = ["terms", "apartment"]


class SearchForm(forms.Form):
    location = forms.CharField(max_length=255)
    num_of_rooms = forms.IntegerField()
    price_from = forms.IntegerField()
    price_to = forms.IntegerField()
    m2_from = forms.IntegerField()
    m2_to = forms.IntegerField()
