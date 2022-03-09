from django.forms import ModelForm

from .models import Comentario


class FormComentario(ModelForm):
    def clean(self):
        data = self.cleaned_data
        nome = data.get('nome_comentario')
        email = data.get('email_comentario')
        comentario = data.get('comentario')

        if len(comentario) < 10:
            self.add_error('comentario', 'Comentário deve ter mais que 10 caracteres')
    
    class Meta:
        model = Comentario
        fields = ('nome_comentario', 'email_comentario', 'comentario')
    
