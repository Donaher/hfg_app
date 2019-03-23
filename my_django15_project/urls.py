from django.urls import path, include
from django.contrib import admin

from myapp import views as v

urlpatterns = [
    path('', v.view_index),
    path('habitos/', v.view_habitos),
    path('personal/', v.view_personal),
    path('medico/', v.view_medico),
    path('nosotros/', v.view_nosotros),
    path('resultados/', v.view_resultados),
    path('inputPersonal/', v.form_personal),
    path('inputMedico/', v.form_medico),
]
