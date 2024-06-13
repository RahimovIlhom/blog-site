from django.urls import path

from .views import home_page_view, HomePageView, HomePageGenericView, blog_detail_view, BlogDetailGenericView, \
    contact_view, about_view, BlogCreateGenericView, BlogUpdateGenericView, BlogDeleteGenericView

urlpatterns = [
    # path('', home_page_view, name='home'),
    # path('blogs/<int:pk>/', blog_detail_view, name='detail'),
    path('contact/', contact_view, name='contact'),
    path('about/', about_view, name='about'),

    # path('', HomePageView.as_view(), name='home'),

    path('', HomePageGenericView.as_view(), name='home'),
    path('blogs/<int:pk>/', BlogDetailGenericView.as_view(), name='detail'),
    path('blogs/<int:pk>/edit/', BlogUpdateGenericView.as_view(), name='edit'),
    path('blogs/<int:pk>/delete/', BlogDeleteGenericView.as_view(), name='delete'),
    path('blog/create/', BlogCreateGenericView.as_view(), name='create'),
]
