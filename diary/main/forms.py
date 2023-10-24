from django import forms  
from diary.tasks import create_json_task

class MessageForm(forms.Form):
    username = forms.CharField(label="Имя", max_length=100, widget=forms.TextInput(attrs={'class':'form-control mb-3', 'id':'form-username'}))
    message = forms.CharField(label="Содержание", widget=forms.Textarea(attrs={'class':'form-control','rows':'7'}))

    def create_json(self):
        create_json_task.delay(self.cleaned_data["username"], self.cleaned_data["message"])