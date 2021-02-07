from django.forms import ModelForm
from app.models import Produtos

# Create the form class.
class ProdutoForm(ModelForm):
    class Meta:
        model = Produtos
        fields = ['produto', 'quantidade', 'valor', 'descricao']