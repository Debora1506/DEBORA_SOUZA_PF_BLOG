from django.urls import path, include
from .views import about,index,detail,create,delete,update
appname = 'coder'

urls = [
    path('about/', about, name='about'),
    path('', index, name='index'),
    path('detail/<int:fornecedor_id>/', detail, name='detail'),
    path('create/', create, name='create'),
    path('delete/<int:fornecedor_id>/', delete, name='delete'),
    path('update/<int:fornecedor_id>/', update, name='update'),

    
]

coder_patterns = (urls,appname)

urlpatterns = [
    path('', include(coder_patterns)),
]