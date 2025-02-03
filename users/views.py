from rest_framework.generics import GenericAPIView, CreateAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenRefreshView

from .serializers import LoginSerializer, RegisterSerializer, RefreshTokenSerializer

User = get_user_model()

# 🔹 ユーザー登録API
class RegisterUserView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

# 🔹 ログインAPI
class LoginView(GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data, status=status.HTTP_200_OK)

# 🔹 JWT認証が必要な保護されたエンドポイント
class ProtectedView(APIView):
    permission_classes = [IsAuthenticated]  

    def get(self, request):
        return Response({"message": f"Hello, {request.user.username}! This is a protected API."})

# 🔹 リフレッシュトークンを使用して新しいアクセストークンを発行
class RefreshTokenView(TokenRefreshView):
    serializer_class = RefreshTokenSerializer

from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import CreateAPIView
from .models import Photo
from .serializers import PhotoSerializer

class PhotoUploadView(CreateAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)  # 認証されたユーザーを自動で紐づける

from rest_framework.generics import ListAPIView
from .models import Photo
from .serializers import PhotoSerializer

class PhotoListView(ListAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer

from rest_framework.generics import DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Photo

#写真削除機能
class PhotoDeleteView(DestroyAPIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):
        try:
            photo = Photo.objects.get(pk=pk, user=request.user)
            photo.delete()
            return Response({"message": "Photo deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
        except Photo.DoesNotExist:
            return Response({"error": "Photo not found or you don't have permission to delete it."}, status=status.HTTP_404_NOT_FOUND)
