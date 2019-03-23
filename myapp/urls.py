from django.urls import path
from . import views

urlpatterns = [

    path('', views.view_index, name='view_index'),
    path('habitos', views.view_habitos, name='view_habitos'),
    path('personal', views.view_personal, name='view_personal'),
    path('medico', views.view_medico, name='view_medico'),
    path('nosotros', views.view_nosotros, name='view_nosotros'),
    path('resultados', views.view_resultados, name='view_resultados'),
    path('inputPersonal', views.form_personal, name='form_personal'),
    path('inputMedico', views.form_medico, name='form_medico'),
]
