from django.contrib.auth.models import BaseUserManager
from django.utils.translation import gettext_lazy as _

# Create your managers here.
class UserManager(BaseUserManager):
    
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError(_("The Email must be set"))
        
        email = self.normalize_email(email)
        user = self.model(email = email, **extra_fields)
        user.set_password(password)
        user.save()
        
        return user
        
    
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("is_staff", True)
        
        # Check Errors
        if extra_fields.get("is_superuser"):
            raise ValueError(_("Superuser must have is_superuser=True."))
        if extra_fields.get("is_staff"):
            raise ValueError(_("Superuser must have is_staff=True."))
        
        superuser = self.create_user(email, password, **extra_fields)
        
        return superuser
    