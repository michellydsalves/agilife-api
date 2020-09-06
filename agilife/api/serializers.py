from rest_framework import serializers

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


class PartnerModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partner
        fields = ['id', 'score_homework']


class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'password', 'female', 'image_link', 'score_content', 'premium', 'expiration_premium', 'partner']


class HomeworkModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Homework
        fields = ['id', 'title', 'description', 'start_date', 'end_date', 'days_week', 'time', 'alert', 'partner']


class UserHomeworkModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserHomework
        fields = ['id', 'status', 'date', 'user', 'homework']


class HomeworkVoucherTypeModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeworkVoucherType
        fields = ['id', 'name']


class HomeworkVoucherModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeworkVoucher
        fields = ['id', 'title', 'description', 'voucher', 'establishment', 'score', 'expiration_date', 'homework_voucher_type']


class UserHomeworkVoucherModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserHomeworkVoucher
        fields = ['id', 'views', 'date', 'user', 'homework_voucher']


class ForumTypeModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ForumType
        fields = ['id', 'name']


class ForumModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Forum
        fields = ['id', 'description', 'date', 'user', 'forum_type']


class ForumCommentModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ForumComment
        fields = ['id', 'comment', 'date', 'user', 'forum']


class UserForumFavoriteModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserForumFavorite
        fields = ['id', 'date', 'user', 'forum']


class ContentTypeModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentType
        fields = ['id', 'name']


class ContentModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = ['id', 'title', 'description', 'url', 'score', 'date', 'location', 'content_type']


class UserContentModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserContent
        fields = ['id', 'favorite', 'runtime', 'date', 'user', 'content']


class PaymentModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['id', 'number', 'name', 'expiration_date', 'user']
