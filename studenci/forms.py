from django import forms


class StudentLoginForm(forms.Form):
    login = forms.CharField(
        label="Twój login:",
        max_length=25,
        widget=forms.TextInput()
    )


class UczelniaForm(forms.Form):
    nazwa = forms.CharField(
        label="Nazwa uczelni:",
        max_length=30,
        widget=forms.TextInput()
    )