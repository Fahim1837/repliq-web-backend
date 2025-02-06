from uuid import uuid4
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import UserManager



# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField (primary_key= True, default= uuid4, editable= False)
    is_active_user = models.BooleanField(default= True)
    is_admin = models.BooleanField(default= False)
    email = models.EmailField (unique= True, null= False, blank= False)
    first_name = models.CharField (max_length= 255, null= False, blank= False)
    last_name = models.CharField (max_length= 255, null= False, blank=False)
    created_at = models.DateTimeField (auto_now_add= True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name','password']
    
    # Custom Manager
    objects = UserManager()

    def __str__(self):
        return self.email
    
    class Meta:
        db_table = 'repliq_user'
        default_manager_name = 'objects'