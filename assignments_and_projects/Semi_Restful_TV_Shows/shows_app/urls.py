from django.urls import path,include
from . import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('',views.all_shows,name='shows'),
    path('new',views.new_show,name='new_show'),
    path('create',views.add_show,name='create_show'),
    path('<int:id>',views.show_details,name='show_details'),
    path('<int:id>/edit',views.edit_show,name='edit_show'),
    path('<int:id>/update',views.update_show,name='update_show'),
    path('<int:id>/destroy',views.delete_show,name="delete_show")
]