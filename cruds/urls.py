from django.urls import path
from .views import index, show, update, delete

urlpatterns = [
    path('cruds/', index, name='home'),
    path('cruds/show/<int:id>', show, name='show'),
    path('cruds/update/<int:id>', update, name='update'),
    path('cruds/delete/<int:id>', delete, name='delete')
]
