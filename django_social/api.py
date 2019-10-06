from rest_framework.viewsets import ModelViewSet
from rest_framework import routers

from .models import Image, User

from .serializers import ImageSerializer, UserSerializer


class ImageViewSet(ModelViewSet):
    serializer_class = ImageSerializer
    queryset = Image.objects.all()


class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()


router = routers.SimpleRouter()
router.register(r'images', ImageViewSet)
router.register(r'users', UserViewSet)
api_urls = router.urls
