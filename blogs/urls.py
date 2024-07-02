from django.urls import path

from .views import home_page_view, HomePageView, HomePageGenericView, blog_detail_view, BlogDetailGenericView, \
    contact_view, about_view, BlogCreateGenericView, BlogUpdateGenericView, BlogDeleteGenericView, SearchView

urlpatterns = [
    # path('', home_page_view, name='home'),
    # path('blogs/<int:pk>/', blog_detail_view, name='detail'),
    path('contact/', contact_view, name='contact'),
    path('about/', about_view, name='about'),

    # path('', HomePageView.as_view(), name='home'),

    path('', HomePageGenericView.as_view(), name='home'),
    path('blogs/<slug:slug>/', BlogDetailGenericView.as_view(), name='detail'),
    path('blogs/<slug:slug>/edit/', BlogUpdateGenericView.as_view(), name='edit'),
    path('blogs/<slug:slug>/delete/', BlogDeleteGenericView.as_view(), name='delete'),
    path('blog/create/', BlogCreateGenericView.as_view(), name='create'),
    path('search/list/', SearchView.as_view(), name='search'),
]
