"""
Views for thr books APIs
"""
from rest_framework import (
    viewsets,mixins,status
)
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from core.models import Book
from book import serializers
# Create your views here.


class BookViewSets(viewsets.ModelViewSet):
    """View for manage book APIs"""
    serializer_class=serializers.BookDetailSerializer
    queryset=Book.objects.all()
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]

    def get_queryset(self):
        """Retrieve books for authenticated user"""
        return self.queryset.filter(user=self.request.user).order_by('-id')
     

    def get_serializer_class(self):
        """Return the serailizer class for request"""
        if self.action == 'list':
            return serializers.BookSerializer
        
        return self.serializer_class 
    
    def perform_create(self, serializer):
        """Create a anew recipe"""
        serializer.save(user=self.request.user)


# class BaseRecipeAttrViewSet(mixins.DestroyModelMixin,
#                             mixins.UpdateModelMixin,
#                             mixins.ListModelMixin,
#                             viewsets.GenericViewSet):
#     """Base viewset for recipe attributes"""
#     authentication_classes=[TokenAuthentication]
#     permission_classes=[IsAuthenticated]

#     def get_queryset(self):
#         """Filter queryset to authenticated user"""
#         return self.queryset.filter(user=self.request.user).order_by('-name')


