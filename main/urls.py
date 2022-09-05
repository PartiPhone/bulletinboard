from django.urls import path

from .views import index, other_page, BBLoginView, BBLogoutView, profile, \
                    ChangeUserInfo, BBPasswordChangeView, DeleteUserView

app_name = 'main'
urlpatterns = [
    path('accounts/profile/delete/', DeleteUserView.as_view(), name='profile_delete'),
    path('accounts/profile/change/', ChangeUserInfo.as_view(), name='profile_change'),
    path('accounts/logout/', BBLogoutView.as_view(), name='logout'),
    path('accounts/password/change/', BBPasswordChangeView.as_view(), name='password_change'),
    path('accounts/profile/', profile, name='profile'),
    path('accounts/login/', BBLoginView.as_view(), name='login'),
    path('<str:page>/', other_page, name='other'),
    path('', index, name='index'),
]

