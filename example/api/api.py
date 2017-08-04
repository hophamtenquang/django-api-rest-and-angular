from rest_framework import generics, permissions


from .serializers import UserSerializer, PostSerializer, PhotoSerializer
from .serializers import PersonSerializer, ArticleSerializer, ImageSerializer
from .models import User, Post, Photo, Person, Article, Image
from .permissions import PostAuthorCanEditPermission


class UserMixin(object):
    model = User
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserList(UserMixin, generics.ListAPIView):
    permission_classes = [
        permissions.AllowAny
    ]


class UserDetail(UserMixin, generics.RetrieveAPIView):
    lookup_field = 'username'


class PostMixin(object):
    model = Post
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [
        PostAuthorCanEditPermission
    ]

    def perform_create(self, serializer):
        """Force author to the current user on save"""
        serializer.save(author=self.request.user)


class PostList(PostMixin, generics.ListCreateAPIView):
    pass


class PostDetail(PostMixin, generics.ListCreateAPIView):
    pass


class UserPostList(generics.ListAPIView):
    model = Post
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_queryset(self):
        queryset = super(UserPostList, self).get_queryset()
        return queryset.filter(author__username=self.kwargs.get('username'))


class PhotoMixin(object):
    model = Photo
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer


class PhotoList(PhotoMixin, generics.ListCreateAPIView):
    permission_classes = [
        permissions.AllowAny
    ]


class PhotoDetail(PhotoMixin, generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [
        permissions.AllowAny
    ]


class PostPhotoList(generics.ListAPIView):
    model = Photo
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer

    def get_queryset(self):
        queryset = super(PostPhotoList, self).get_queryset()
        return queryset.filter(post__pk=self.kwargs.get('pk'))


class PersonMixin(object):
    model = Person
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class PersonList(PersonMixin, generics.ListAPIView):
    pass


class PersonDetail(PersonMixin, generics.RetrieveUpdateDestroyAPIView):
    pass


class ArticleMixin(object):
    model = Article
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleList(ArticleMixin, generics.ListAPIView):
    pass


class ArticleDetail(ArticleMixin, generics.RetrieveUpdateDestroyAPIView):
    pass


class PersonAricleList(generics.ListAPIView):
    model = Article
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def get_queryset(self):
        queryset = super(PersonAricleList, self).get_queryset()
        return queryset.filter(author__pk=self.kwargs.get('pk'))


class ImageMixin(object):
    model = Image
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
