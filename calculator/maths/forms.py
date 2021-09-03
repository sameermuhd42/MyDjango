from django import forms


class CalcForm(forms.Form):
    num1 = forms.IntegerField()
    num2 = forms.IntegerField()

    def clean(self):
        print('valid')
