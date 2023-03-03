from django.urls import path
from main.views import (BBLoginView, BBLogoutView, BBPasswordChangeView,
                        BBPasswordResetCompleteView,
                        BBPasswordResetConfirmView, BBPasswordResetDoneView,
                        BBPasswordResetView, ChangeUserInfoView,
                        DeleteUserView, RegisterDoneView, RegisterUserView,
                        index, other_page, profile, user_activate)

app_name = 'main'

urlpatterns = [
    path(
        'accounts/password/confirm/<uidb64>/<token>/',
        BBPasswordResetConfirmView.as_view(), name='password_reset_confirm'
    ),
    path(
        'accounts/password/confirm/complete/',
        BBPasswordResetCompleteView.as_view(), name='password_reset_complete'
    ),
    path(
        'accounts/password/reset/done/', BBPasswordResetDoneView.as_view(),
        name='password_reset_done'
    ),
    path(
        'accounts/register/activate/<str:sign>/', user_activate,
        name='register_activate'
    ),
    path(
        'accounts/password/reset/', BBPasswordResetView.as_view(),
        name='password_reset'
    ),
    path(
        'accounts/password/change/', BBPasswordChangeView.as_view(),
        name='password_change'
    ),
    path(
        'accounts/profile/delete/', DeleteUserView.as_view(),
        name='profile_delete'
    ),
    path(
        'accounts/profile/change/', ChangeUserInfoView.as_view(),
        name='profile_change'
    ),
    path(
        'accounts/register/done/', RegisterDoneView.as_view(),
        name='register_done'
    ),
    path('accounts/profile/', profile, name='profile'),
    path('accounts/logout/', BBLogoutView.as_view(), name='logout'),
    path('accounts/login/', BBLoginView.as_view(), name='login'),
    path('accounts/register/', RegisterUserView.as_view(), name='register'),
    path('<str:page>/', other_page, name='other'),
    path('', index, name='index'),
]
