from django.urls import path
from . import views


app_name = 'notes'


urlpatterns = [
    path('update/<int:note_id>', views.update_note, name='update'),
    path('create', views.create_note, name='create'),
    path('list', views.note_list, name='list'),
    path('detail/<int:note_id>', views.note_detail, name='detail'),
    path('delete/<int:note_id>', views.note_delete, name='delete'),
]