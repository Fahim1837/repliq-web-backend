from django.db import models
from authentication.models import User

# Create your models here.
class BookCategory(models.Model):
    name = models.CharField(max_length= 50, blank= False, null= True)
    created_by = models.ForeignKey(User, on_delete= models.CASCADE, related_name="book_category")
    created_at = models.DateTimeField(auto_now_add= True)


class Book (models.Model):
    name = models.CharField(max_length= 255, blank= False, null= False)
    author = models.CharField(max_length=255, blank=True, null= True)
    category = models.ForeignKey (BookCategory, on_delete= models.CASCADE, related_name="book")
    created_by = models.ForeignKey(User, on_delete= models.CASCADE, related_name="book_created")
    created_at = models.DateTimeField(auto_now_add= True)
    updated_by = models.ForeignKey(User, on_delete= models.CASCADE, related_name="book_updated")
    updated_at = models.DateTimeField(auto_now= True)
    
    class Meta:
        db_table = "book"