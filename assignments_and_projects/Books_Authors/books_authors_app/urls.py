
from django.urls import path
from  . import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('',views.index),
    path('add_book',views.add_book),
    path('books/<int:id>/',views.show_book),
    path('authors/',views.show_authors),
    path('authors/add_author',views.add_author),
    path('authors/<int:id>/',views.show_author_book)
]
