from django.forms import ModelForm

from .models import Comentario
import requests


class FormComentario(ModelForm):
    def clean(self):
        raw_data = self.data

        recaptcha_response = raw_data.get('g-recaptcha-response')

        cleaned_data = self.cleaned_data

        nome = cleaned_data.get('nome_comentario')
        email = cleaned_data.get('email_comentario')
        comentario = cleaned_data.get('comentario')

        recaptcha_request = requests.post('https://www.google.com/recaptcha/api/siteverify',
            data={
                'secret': '6Lf9kvEeAAAAALC0SwAxZ0cYenl1c-5OZiUCSK0e',
                'response': recaptcha_response
            }
        )

        recaptcha_result = recaptcha_request.json()

        if not recaptcha_result.get('success'):
            self.add_error(
                'comentario',
                'Por favor, marque o campo "Não sou um robô".'
            )

        if len(comentario) < 10:
            self.add_error('comentario', 'Comentário deve ter mais que 10 caracteres')

        if len(nome) < 3:
            self.add_error('nome_comentario', 'Nome deve ter pelo menos 3 caracteres')
    
    class Meta:
        model = Comentario
        fields = ('nome_comentario', 'email_comentario', 'comentario')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) # Call to ModelForm constructor
        self.fields['comentario'].widget.attrs['style'] = 'resize: none;'
        self.fields['nome_comentario'].widget.attrs.update({'autocomplete': 'off'})
        self.fields['email_comentario'].widget.attrs.update({'autocomplete': 'off'})
