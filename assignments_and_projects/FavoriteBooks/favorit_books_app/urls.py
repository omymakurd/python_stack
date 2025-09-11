from django.urls import path,include
from . import views
urlpatterns = [
  
   path('',views.index,name='index'),
   path('create_user',views.create_user,name="create_user"),
   path('login',views.log_in,name="login"),
   path('books',views.fav_book,name='books'),
   path('logout',views.logout,name="logout"),
   path('add_book',views.add_book,name="add_book"),
   path('books/<int:book_id>',views.book_detail,name="book_detail"),
   path('favorite/<int:book_id>', views.add_to_favorite, name='add_to_favorite'),
   path('unfavorite/<int:book_id>', views.unfavorite_book, name='unfavorite_book'),
   path('books/<int:book_id>/update', views.update_book, name="update_book"),
   path('books/<int:book_id>/delete', views.delete_book, name="delete_book"),
   path('my_favorites', views.my_favorites, name="my_favorites"),
   

]
