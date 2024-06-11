from django.urls import path

from .views import home_page_view, HomePageView, HomePageGenericView, blog_detail_view, BlogDetailGenericView

urlpatterns = [
    # path('', home_page_view, name='home'),
    # path('blogs/<int:pk>/', blog_detail_view, name='detail'),

    # path('', HomePageView.as_view(), name='home'),

    path('', HomePageGenericView.as_view(), name='home'),
    path('blogs/<int:pk>/', BlogDetailGenericView.as_view(), name='detail'),
]
