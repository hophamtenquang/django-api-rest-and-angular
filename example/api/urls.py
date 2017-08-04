from django.conf.urls import url, include

from .api import UserList, UserDetail
from .api import PostList, PostDetail, UserPostList
from .api import PhotoList, PhotoDetail, PostPhotoList
from .api import ArticleList, ArticleDetail, ArticleImageList
from .api import PersonList, PersonDetail, PersonAricleList
from .api import ImageList, ImageDetail

user_urls = [
    url(r'^/(?P<username>[0-9a-zA-Z_-]+)/posts$', UserPostList.as_view(), name='userpost-list'),
    url(r'^/(?P<username>[0-9a-zA-Z_-]+)$', UserDetail.as_view(), name='user-detail'),
    url(r'^$', UserList.as_view(), name='user-list')
]

post_urls = [
    url(r'^/(?P<pk>\d+)/photos$', PostPhotoList.as_view(), name='postphoto-list'),
    url(r'^/(?P<pk>\d+)$', PostDetail.as_view(), name='post-detail'),
    url(r'^$', PostList.as_view(), name='post-list')
]

photo_urls = [
    url(r'^/(?P<pk>\d+)$', PhotoDetail.as_view(), name='photo-detail'),
    url(r'^$', PhotoList.as_view(), name='photo-list')
]

person_urls = [
    url(r'^$', PersonList.as_view(), name='person-list'),
    url(r'^/(?P<pk>\d+)$', PersonDetail.as_view(), name='person-detail'),
    url(r'^/(?P<pk>\d+)/articles$', PersonAricleList.as_view(), name='personarticle-list')
]

article_urls = [
    url(r'^$', ArticleList.as_view(), name='article-list'),
    url(r'^/(?P<pk>\d+)$', ArticleDetail.as_view(), name='article-detail'),
    url(r'^/(?P<pk>\d+)/images$', ArticleImageList.as_view(), name='articleimage-list')
]

image_urls = [
    url(r'^$', ImageList.as_view(), name='image-list'),
    url(r'^/(?P<pk>\d+)$', ImageDetail.as_view(), name='image-detail')
]

urlpatterns = [
    url(r'^users', include(user_urls)),
    url(r'^posts', include(post_urls)),
    url(r'^photos', include(photo_urls)),
    url(r'^people', include(person_urls)),
    url(r'^articles', include(article_urls)),
    url(r'^images', include(image_urls))
]
