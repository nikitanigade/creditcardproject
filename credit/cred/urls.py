from django.contrib import admin
from django.urls import path, include
from . import views

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', views.login_view, name='login'),
#     path('index/', views.index, name='index'),
#     path('credit_card/', views.credit_card, name='credit_card'),
#     path('predict_fraud/', views.predict_fraud, name='predict_fraud'),
#     path('logout/', views.user_logout, name='logout'),
# ]
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login_view, name='login'),  # Login is the first path
    path('index/', views.index, name='index'),  # Index should be here
    path('credit_card/', views.credit_card, name='credit_card'),
    path('predict_fraud/', views.predict_fraud, name='predict_fraud'),
    path('logout/', views.user_logout, name='logout'),
]