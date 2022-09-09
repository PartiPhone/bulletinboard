from django.urls import path
from .views import ( index, other_page, by_rubric, BBLoginView, 
            BBLogoutView, profile, ChangeUserInfo, BBPasswordChangeView, 
            RegisterUserView, RegisterDoneView, user_activate, 
            DeleteUserView, UserPasswordResetView, 
            UserPasswordResetDoneView, UserPasswordResetConfirmView,
            UserPasswordResetCompleteView )

app_name = 'main'
urlpatterns = [
    path('accounts/password_reset/', UserPasswordResetView.as_view(), 
            name='password_reset'),
    path('accounts/password_reset/done/', UserPasswordResetDoneView.as_view(),
            name='password_reset_done'),    
    path('accounts/reset/<uidb64>/<token>/', UserPasswordResetConfirmView.as_view(),
            name='password_reset_confirm'),
    path('accounts/reset/done/', UserPasswordResetCompleteView.as_view(),
            name='password_reset_complete'), 
    path('accounts/profile/delete/', DeleteUserView.as_view(), 
            name='profile_delete'),
    path('accounts/register/activate/<str:sign>/', user_activate, 
            name='register_activate'),
    path('accounts/register/done', RegisterDoneView.as_view(), 
            name='register_done'),
    path('accounts/register/', RegisterUserView.as_view(), 
            name='register'),
    path('accounts/profile/change/', ChangeUserInfo.as_view(), 
            name='profile_change'),
    path('accounts/logout/', BBLogoutView.as_view(), name='logout'),
    path('accounts/password/change/', BBPasswordChangeView.as_view(),
            name='password_change'),
    path('accounts/profile/', profile, name='profile'),
    path('accounts/login/', BBLoginView.as_view(), name='login'),
    path('<int:pk>/', by_rubric, name='by_rubric'),
    path('<str:page>/', other_page, name='other'),
    path('', index, name='index'),
]

