from django.urls import path
from .views import RegisterView, DashboardView, LoginView, LogoutView, QuestionList

urlpatterns = [

    path('login/', LoginView.as_view(), name='login-view'),
    path('questions/',QuestionList.as_view(), name='question-view'),
    path('register/', RegisterView.as_view(), name='register-view'),
    path('dashboard/', DashboardView.as_view(), name='dashboard-view'),
    path('logout/', LogoutView.as_view(), name='logout-view'),

]