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
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) # Call to ModelForm constructor
        self.fields['comentario'].widget.attrs['style'] = 'width:100%; height:200px; resize: none;'
        self.fields['nome_comentario'].widget.attrs.update({'autocomplete': 'off'})
        self.fields['email_comentario'].widget.attrs.update({'autocomplete': 'off'})
