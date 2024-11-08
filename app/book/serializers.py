"""
Serializers for book APIs
"""

from rest_framework import serializers

from core.models import Book

class BookSerializer(serializers.ModelSerializer):
    """Serializer for books"""

    
    class Meta:
        model=Book
        fields=['id','book_name','author_name','genre']
        read_only_fields=['id']


#     def create(self,validated_data):
#         """Create a book"""
#         book=Book.objects.create(**validated_data)
    
#         return book
    
#     def update(self, instance, validated_data):
#         """Update recipe"""
       
#         for attr,value in validated_data.items():
#             setattr(instance,attr,value)

#         instance.save()
#         return instance

class BookDetailSerializer(BookSerializer):
    """Serializer for book detail view"""

    class Meta(BookSerializer.Meta):
        fields=BookSerializer.Meta.fields + ['description']


