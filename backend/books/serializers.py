from rest_framework import serializers as s
from .models import Book, BookCategory
from apps.helpers.unexpected_keys import unexpected_key_names

class BooksCategorySerializer (s.ModelSerializer):
    created_by = s.HiddenField(default=s.CurrentUserDefault())
    
    class Meta:
        model = BookCategory
        fields = ['id', 'name', 'created_by']
        
    def to_internal_value(self, data):
        unexpected_key_names(allowed=self.fields.keys(), incoming=data.keys())
        return super().to_internal_value(data)


class BooksSerializer (s.ModelSerializer):
    category_id = s.UUIDField(write_only= True)
    category = BooksCategorySerializer (read_only=True)
    created_by = s.HiddenField(default=s.CurrentUserDefault())
    updated_by = s.HiddenField(default = s.CurrentUserDefault())
    
    class Meta:
        model = Book
        fields = ['id', 'name', 'author','category_id', 'category', 'created_by', 'updated_by']
        
    def to_internal_value(self, data):
        unexpected_key_names(allowed=self.fields.keys(), incoming=data.keys())
        return super().to_internal_value(data)