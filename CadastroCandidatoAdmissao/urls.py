from django.urls import path
from CadastroCandidatoAdmissao.views import login


urlpatterns = [
    path('', login)
]