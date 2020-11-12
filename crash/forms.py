from django import forms


class CrashForm(forms.Form):
    bet_amount = forms.IntegerField(initial=1, min_value=1, max_value=10000,
                                    widget=forms.NumberInput(attrs={"class": "form-control",
                                                                    "style": "text-align:center"}))
