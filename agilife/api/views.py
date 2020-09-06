from rest_framework import viewsets
from rest_framework import mixins
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import authentication_classes, permission_classes

from api.serializers import (
    UserModelSerializer,
    PartnerModelSerializer,
    HomeworkModelSerializer,
    UserHomeworkModelSerializer,
    HomeworkVoucherTypeModelSerializer,
    HomeworkVoucherModelSerializer,
    UserHomeworkVoucherModelSerializer,
    ForumTypeModelSerializer,
    ForumModelSerializer,
    ForumCommentModelSerializer,
    UserForumFavoriteModelSerializer,
    ContentTypeModelSerializer,
    ContentModelSerializer,
    UserContentModelSerializer,
    PaymentModelSerializer
)

from api.models import (
    Partner,
    User,
    Homework,
    UserHomework,
    HomeworkVoucherType,
    HomeworkVoucher,
    UserHomeworkVoucher,
    ForumType,
    Forum,
    ForumComment,
    UserForumFavorite,
    ContentType,
    Content,
    UserContent,
    Payment
)


@authentication_classes([])
@permission_classes([])
class UserApiViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer


class PartnerApiViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Partner.objects.all()
    serializer_class = PartnerModelSerializer


class HomeworkApiViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Homework.objects.all()
    serializer_class = HomeworkModelSerializer


class UserHomeworkApiViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = UserHomework.objects.all()
    serializer_class = UserHomeworkModelSerializer


class HomeworkVoucherTypeListOnlyAPIView(mixins.ListModelMixin, generics.GenericAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = HomeworkVoucherType.objects.all()
    serializer_class = HomeworkVoucherTypeModelSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class HomeworkVoucherListOnlyAPIView(mixins.ListModelMixin, generics.GenericAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = HomeworkVoucher.objects.all()
    serializer_class = HomeworkVoucherModelSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class UserHomeworkVoucherApiViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = UserHomeworkVoucher.objects.all()
    serializer_class = UserHomeworkVoucherModelSerializer


class ForumTypeListOnlyAPIView(mixins.ListModelMixin, generics.GenericAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = ForumType.objects.all()
    serializer_class = ForumTypeModelSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class ForumApiViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Forum.objects.all()
    serializer_class = ForumModelSerializer


class ForumCommentApiViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = ForumComment.objects.all()
    serializer_class = ForumCommentModelSerializer


class UserForumFavoriteApiViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = UserForumFavorite.objects.all()
    serializer_class = UserForumFavoriteModelSerializer


class ContentTypeListOnlyAPIView(mixins.ListModelMixin, generics.GenericAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = ContentType.objects.all()
    serializer_class = ContentTypeModelSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
        

class ContentListOnlyAPIView(mixins.ListModelMixin, generics.GenericAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Content.objects.all()
    serializer_class = ContentModelSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class UserContentApiViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = UserContent.objects.all()
    serializer_class = UserContentModelSerializer


class PaymentApiViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Payment.objects.all()
    serializer_class = PaymentModelSerializer
