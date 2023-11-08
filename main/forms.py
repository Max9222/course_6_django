from django import forms

from main.models import Client, Mailling, Message

class StyleFormMixin:  # Стиль для Form
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control-lg'   # Меняем тут

class ClientForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = Client
        fields = '__all__'

class MessageForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = Message
        fields = '__all__'

class MaillingForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = Mailling
        fields = '__all__'


