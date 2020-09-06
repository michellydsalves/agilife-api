from django.contrib import admin

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

admin.site.register(Partner)
admin.site.register(User)
admin.site.register(Homework)
admin.site.register(UserHomework)
admin.site.register(HomeworkVoucherType)
admin.site.register(HomeworkVoucher)
admin.site.register(UserHomeworkVoucher)
admin.site.register(ForumType)
admin.site.register(Forum)
admin.site.register(ForumComment)
admin.site.register(UserForumFavorite)
admin.site.register(ContentType)
admin.site.register(Content)
admin.site.register(UserContent)
admin.site.register(Payment)
