from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.contrib.auth import get_user_model

# MANAGERS FOR THE MODELS

class ActiveManager(models.Manager):
    def active(self):
        return self.filter(active = True)


class UserManager(BaseUserManager):
    # This user manager is necessary to change the application from username based login to email based login
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('The email must be set')
        email = self.normalize_email(email)
        user = self.model(email = email, **extra_fields)
        user.set_password(password)
        user.save(using= self._db)

    def create_user(self, email, password = None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Super user must have is_staff=True.")

        return self._create_user(email, password, **extra_fields)

class User(AbstractUser):
    username = None
    email = models.EmailField("email address", unique = True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

class BlogPostCategory(models.Model):
    name = models.CharField(max_length = 30)
    slug = models.CharField(max_length = 40)

    def __str__(self):
        return self.name
    

class BlogPost(models.Model):
    title = models.CharField(max_length = 90)
    slug = models.SlugField(max_length = 100)
    description = models.CharField(max_length = 112)
    content = models.TextField()
    date_updated = models.DateTimeField(auto_now = True)
    active = models.BooleanField(default = True)
    user = models.ForeignKey(User, on_delete = models.RESTRICT)
    category = models.ForeignKey(BlogPostCategory, on_delete = models.RESTRICT)

    objects = ActiveManager()

    def __str__(self):
        return self.title



class BlogPostTag(models.Model):
    name = models.CharField(max_length = 30)
    slug = models.CharField(max_length = 40)
    blogpost = models.ManyToManyField(BlogPost, blank = True)

    def __str__(self):
        return self.name


class Comment(models.Model):
    message = models.TextField(max_length = 500)
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    blogpost = models.ForeignKey(BlogPost, on_delete = models.CASCADE)

class BlogPostImage(models.Model):
    blogpost = models.OneToOneField(BlogPost, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='upload_images')
    thumbnail = models.ImageField(upload_to='upload_thumbnails', null = True)
