from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import Candidato, Empresa

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, label='Usuário')
    password = forms.CharField(widget=forms.PasswordInput(), label='Senha')

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Entrar', css_class='btn btn-primary btn-block mt-3'))

class CandidatoForm(forms.ModelForm):
    class Meta:
        model = Candidato
        fields = ['nome', 'telefone', 'endereco', 'email']
        labels = {
            'nome': 'Nome',
            'telefone': 'Telefone',
            'endereco': 'Endereço',
            'email': 'E-mail',
        }

    def __init__(self, *args, **kwargs):
        super(CandidatoForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Cadastrar', css_class='btn btn-primary btn-block mt-3'))
        
class EmpresaForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = ['razao_social', 'telefone', 'cnpj', 'endereco', 'segmento']
        labels = {
            'razao_social': 'Razão Social',
            'telefone': 'Telefone',
            'cnpj': 'CNPJ',
            'endereco': 'Endereço',
            'segmento': 'Segmento',
        }

    def __init__(self, *args, **kwargs):
        super(EmpresaForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Cadastrar', css_class='btn btn-primary btn-block mt-3'))
