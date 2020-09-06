from django.urls import include, path
from django.contrib import admin
from rest_framework import routers

from api import views

router = routers.DefaultRouter()
router.register(r'users', views.UserApiViewSet)
router.register(r'partners', views.PartnerApiViewSet)
router.register(r'homeworks', views.HomeworkApiViewSet)
router.register(r'user_homeworks', views.UserHomeworkApiViewSet)
router.register(r'user_homework_vouchers', views.UserHomeworkVoucherApiViewSet)
router.register(r'forums', views.ForumApiViewSet)
router.register(r'forum_comments', views.ForumCommentApiViewSet)
router.register(r'user_forum_favorites', views.UserForumFavoriteApiViewSet)
router.register(r'user_contents', views.UserContentApiViewSet)
router.register(r'payments', views.PaymentApiViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('homework_vouchers_types/', views.HomeworkVoucherTypeListOnlyAPIView.as_view()),
    path('homework_vouchers/', views.HomeworkVoucherListOnlyAPIView.as_view()),
    path('forum_types/', views.ForumTypeListOnlyAPIView.as_view()),
    path('content_types/', views.ContentTypeListOnlyAPIView.as_view()),
    path('contents/', views.ContentListOnlyAPIView.as_view()),
    path('auth/', include('rest_auth.urls'))
]
