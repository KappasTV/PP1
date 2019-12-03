from django.urls import path


from . import views

app_name = 'family'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('<int:family_id>/', views.detail, name = 'detail'),
    path('<int:family_id>/make_transaction/', views.make_transaction, name = 'make_transaction')
]