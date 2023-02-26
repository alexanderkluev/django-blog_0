from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/comment_new/<int:pk>/', views.comment_new, name='comment_new'),
    path('tag/<int:pk>/', views.tag_detail, name='tag_detail'),
    path('promo_email', views.get_promo_email, name='promo_email'),
    path('tags', views.tags_page, name='tags'),
    path('contacts', views.contacts_page, name='contacts')
]
