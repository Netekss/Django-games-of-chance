from django import forms


class LevelEasy(forms.Form):
    bet_amount = forms.DecimalField(initial=1, min_value=1, max_value=10000, decimal_places=2,
                                    widget=forms.NumberInput(attrs={"class": "form-control",
                                                                    "style": "text-align:center",
                                                                    "step": 0.5}))

    given_number = forms.IntegerField(min_value=1, max_value=5,
                                      widget=forms.NumberInput(attrs={"class": "form-control",
                                                                      "style": "text-align:center",
                                                                      "placeholder": "Input your lucky number"}))


class LevelNormal(forms.Form):
    bet_amount = forms.DecimalField(initial=1, min_value=1, max_value=10000, decimal_places=2,
                                    widget=forms.NumberInput(attrs={"class": "form-control",
                                                                    "style": "text-align:center",
                                                                    "step": 0.5}))

    given_number_1 = forms.IntegerField(min_value=1, max_value=10,
                                        widget=forms.NumberInput(attrs={"class": "form-control",
                                                                        "style": "text-align:center",
                                                                        "placeholder": "first number"}))

    given_number_2 = forms.IntegerField(min_value=1, max_value=10,
                                        widget=forms.NumberInput(attrs={"class": "form-control",
                                                                        "style": "text-align:center",
                                                                        "placeholder": "second number"}))


class LevelHard(forms.Form):
    bet_amount = forms.DecimalField(initial=1, min_value=1, max_value=10000, decimal_places=2,
                                    widget=forms.NumberInput(attrs={"class": "form-control",
                                                                    "style": "text-align:center",
                                                                    "step": 0.5}))

    given_number_1 = forms.IntegerField(min_value=1, max_value=15,
                                        widget=forms.NumberInput(attrs={"class": "form-control",
                                                                        "style": "text-align:center",
                                                                        "placeholder": "first number"}))

    given_number_2 = forms.IntegerField(min_value=1, max_value=15,
                                        widget=forms.NumberInput(attrs={"class": "form-control",
                                                                        "style": "text-align:center",
                                                                        "placeholder": "second number"}))

    lucky_number = forms.IntegerField(min_value=1, max_value=5,
                                      widget=forms.NumberInput(attrs={"class": "form-control",
                                                                      "style": "text-align:center",
                                                                      "placeholder": "lucky number"}))
