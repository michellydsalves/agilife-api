from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.core.validators import MinLengthValidator, EmailValidator

import datetime

min_validator = MinLengthValidator(8, 'A senha deve conter pelo menos 8 caracteres.')

DAYS_WEEK_CHOICES = [
    ('Seg', 'Segunda-feira'),
    ('Ter', 'Terça-feira'),
    ('Qua', 'Quarta-feira'),
    ('Qui', 'Quinta-feira'),
    ('Sex', 'Sexta-feira'),
    ('Sab', 'Sábado'),
    ('Dom', 'Domingo')
]


class UserManager(BaseUserManager):
    def create_user(self, email, name, password, female, is_staff=False, is_superuser=False):
        user = self.model(email=email, name=name, password=password, female=female, is_staff=is_staff, is_superuser=is_superuser, is_active=True)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password):
        self.create_user(email, 'admin', password, False, True, True)


class Partner(models.Model):
    score_homework = models.IntegerField(default=0)


class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=50, blank=True)
    email = models.EmailField(validators=[EmailValidator], unique=True, blank=True)
    password = models.CharField(max_length=50, validators=[min_validator], blank=True)
    female = models.BooleanField(blank=True)
    image_link = models.TextField(max_length=500, default="")
    score_content = models.IntegerField(default=0)
    premium = models.BooleanField(default=0)
    expiration_premium = models.DateField(auto_now_add=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    partner = models.ForeignKey(Partner, on_delete=models.SET_NULL, blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['password']

    objects = UserManager()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Homework(models.Model):
    title = models.CharField(max_length=50, blank=True)
    description = models.TextField(max_length=500, default="")
    start_date = models.DateField(blank=True)
    end_date = models.DateField(blank=True)
    days_week = models.CharField(max_length=3, choices=DAYS_WEEK_CHOICES)
    time = models.TimeField(blank=True)
    alert = models.TimeField(default=None)
    partner = models.ForeignKey(Partner, on_delete=models.PROTECT, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']


class UserHomework(models.Model):
    status = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT, blank=True)
    homework = models.ForeignKey(Homework, on_delete=models.PROTECT, blank=True)

    def __str__(self):
        return self.homeworks.title

    class Meta:
        ordering = ['date']


class HomeworkVoucherType(models.Model):
    name = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class HomeworkVoucher(models.Model):
    title = models.CharField(max_length=50, blank=True)
    description = models.TextField(max_length=500, default="")
    voucher = models.CharField(max_length=50, blank=True)
    establishment = models.CharField(max_length=50, blank=True)
    score = models.IntegerField(default=0)
    expiration_date = models.DateField(blank=True)
    homework_voucher_type = models.ForeignKey(HomeworkVoucherType, on_delete=models.PROTECT, blank=True)

    def __str__(self):
        return self.title
        
    class Meta:
        ordering = ['title']


class UserHomeworkVoucher(models.Model):
    views = models.IntegerField(default=1)
    date = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT, blank=True)
    homework_voucher = models.ForeignKey(HomeworkVoucher, on_delete=models.PROTECT, blank=True)

    def __str__(self):
        return self.homeworks.views

    class Meta:
        ordering = ['date']


class ForumType(models.Model):
    name = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Forum(models.Model):
    description = models.TextField(max_length=500, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT, blank=True)
    forum_type = models.ForeignKey(ForumType, on_delete=models.PROTECT, blank=True)

    def __str__(self):
        return self.description

    class Meta:
        ordering = ['description']


class ForumComment(models.Model):
    comment = models.TextField(max_length=500, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT, blank=True)
    forum = models.ForeignKey(Forum, on_delete=models.PROTECT, blank=True)

    def __str__(self):
        return self.comment

    class Meta:
        ordering = ['date']


class UserForumFavorite(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT, blank=True)
    forum = models.ForeignKey(Forum, on_delete=models.PROTECT, blank=True)

    class Meta:
        ordering = ['date']


class ContentType(models.Model):
    name = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Content(models.Model):
    title = models.CharField(max_length=50, blank=True)
    description = models.TextField(max_length=500, blank=True)
    url = models.TextField(max_length=500, blank=True)
    score = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True)
    location = models.TextField(max_length=500, blank=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.PROTECT,  blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']


class UserContent(models.Model):
    favorite = models.BooleanField(default=False)
    runtime = models.TimeField(default=datetime.time(0,0,0))
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT, blank=True)
    content = models.ForeignKey(Content, on_delete=models.PROTECT,  blank=True)

    class Meta:
        ordering = ['date']


class Payment(models.Model):
    number = models.IntegerField(blank=True)
    name = models.CharField(max_length=50, blank=True)
    expiration_date = models.DateField(blank=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT, blank=True)

    class Meta:
        ordering = ['number']
