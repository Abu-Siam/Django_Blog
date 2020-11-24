from django import forms
from crispy_forms.helper import FormHelper

class PathForm(forms.Form):
    source = forms.CharField(label='', max_length=100)

    destination = forms.CharField(label='Destination:', max_length=100)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-exampleForm'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.form_action = 'submit_survey'

        from crispy_forms.layout import Submit
        self.helper.add_input(Submit('submit', 'Submit'))


