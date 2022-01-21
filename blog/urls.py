from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    #path('', views.post_list, name='post_list'),
    path('', views.PostListView.as_view(), name='post_list'),
    path('send-email/', views.sendd_email, name='send-email'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail, name='post_detail'),
    path('about/', views.about, name='about'),
    path('zen-of-python/', views.zen_of_python, name='zen_of_python'),
    
]