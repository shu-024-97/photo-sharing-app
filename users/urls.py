from django.urls import path
from .views import (
    RegisterUserView, LoginView, ProtectedView, 
    RefreshTokenView, PhotoUploadView,PhotoListView,PhotoDeleteView,
)

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('protected/', ProtectedView.as_view(), name='protected'),  # 認証が必要なエンドポイント
    path('refresh/', RefreshTokenView.as_view(), name='token_refresh'),
    path('upload/', PhotoUploadView.as_view(), name='photo-upload'),  # 画像アップロードAPI
    path('photos/', PhotoListView.as_view(), name='photo-list'),
     path('photos/<int:pk>/delete/', PhotoDeleteView.as_view(), name='photo-delete'),
]
