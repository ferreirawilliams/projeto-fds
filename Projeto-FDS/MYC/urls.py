from django.urls import path
from MYC.views import home,login, register_estabelecimento, register_usuario, register_create

app_name = 'MYC'

urlpatterns = [
    path('', home),
    path('login/', login, name="login"),
    path('RegistroUsuario/', register_usuario, name="usuario"),
    path('RegistroEstabelecimento/', register_estabelecimento, name="estab" ),
    path('RegistroUsuario/create/', register_create, name='create')
]