from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

USER_TYPE = (
    ('S', "Student"),
    ('T', "Teacher"),
)


class Account(AbstractUser):
    username = models.CharField(verbose_name='Username', max_length=150,unique=True)
    email = models.EmailField(verbose_name='Email address',unique=True,null=False,blank=False)
    user_type = models.CharField(blank=False, null=False,
                              choices=USER_TYPE, max_length=1,default = 'S')

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['username',]
    
    def save(self, *args, **kwargs):
        if not self.username:
            username = self.email.split('@')[0] + '_' + self.email.split('@')[1].split('.')[0]
            self.username = username
        super().save(*args, **kwargs)