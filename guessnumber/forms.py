from django import forms


class LevelEasy(forms.Form):
    bet_amount = forms.DecimalField(initial=1, min_value=1, max_value=10000, decimal_places=2,
                                    widget=forms.NumberInput(attrs={"class": "form-control",
                                                                    "style": "text-align:center",
                                                                    "step": 0.5}))

    given_number = forms.IntegerField(min_value=1, max_value=5,
                                      widget=forms.NumberInput(attrs={"class": "form-control",
                                                                      "style": "text-align:center",
                                                                      "placeholder": "1 - 5"}))


class LevelNormal(forms.Form):
    bet_amount = forms.DecimalField(initial=1, min_value=1, max_value=10000, decimal_places=2,
                                    widget=forms.NumberInput(attrs={"class": "form-control",
                                                                    "style": "text-align:center",
                                                                    "step": 0.5}))

    given_number_1 = forms.IntegerField(min_value=1, max_value=10,
                                        widget=forms.NumberInput(attrs={"class": "form-control",
                                                                        "style": "text-align:center",
                                                                        "placeholder": "[1] 1 - 10"}))

    given_number_2 = forms.IntegerField(min_value=1, max_value=10,
                                        widget=forms.NumberInput(attrs={"class": "form-control",
                                                                        "style": "text-align:center",
                                                                        "placeholder": "[2] 1 - 10"}))


class LevelHard(forms.Form):
    bet_amount = forms.DecimalField(initial=1, min_value=1, max_value=10000, decimal_places=2,
                                    widget=forms.NumberInput(attrs={"class": "form-control",
                                                                    "style": "text-align:center",
                                                                    "step": 0.5}))

    given_number_1 = forms.IntegerField(min_value=1, max_value=15,
                                        widget=forms.NumberInput(attrs={"class": "form-control",
                                                                        "style": "text-align:center",
                                                                        "placeholder": "[1] 1 - 15"}))

    given_number_2 = forms.IntegerField(min_value=1, max_value=15,
                                        widget=forms.NumberInput(attrs={"class": "form-control",
                                                                        "style": "text-align:center",
                                                                        "placeholder": "[2] 1 - 15"}))

    lucky_number = forms.IntegerField(min_value=1, max_value=5,
                                      widget=forms.NumberInput(attrs={"class": "form-control",
                                                                      "style": "text-align:center",
                                                                      "placeholder": "[lucky number] 1 - 5"}))
