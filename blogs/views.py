from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView

from blogs.models import Blog


# functional view
def home_page_view(request):
    blogs = Blog.objects.all()
    context = {
        'blogs': blogs
    }
    return render(request, 'home.html', context)


def blog_detail_view(request, pk):
    try:
        blog = Blog.objects.get(pk=pk)
        context = {
            'blog': blog
        }
        return render(request, 'detail.html', context)
    except Blog.DoesNotExist:
        return HttpResponse("Bunday sahifa mavjud emas!")


# class based view
class HomePageView(View):
    def get(self, request):
        blogs = Blog.objects.all()
        context = {
            'blogs': blogs
        }
        return render(request, 'home.html', context)

    def post(self, request):
        pass


class BlogDetailView(View):
    def get(self, request, pk):
        try:
            blog = Blog.objects.get(pk=pk)
            context = {
                'blog': blog
            }
            return render(request, 'detail.html', context)
        except Blog.DoesNotExist:
            return HttpResponse("Bunday sahifa mavjud emas!")


# generic views: CreateView, UpdateView, DetailView, DeleteView, ListView
class HomePageGenericView(ListView):
    model = Blog
    template_name = 'home.html'
    context_object_name = 'blogs'


class BlogDetailGenericView(DetailView):
    model = Blog
    template_name = 'detail.html'
    context_object_name = 'blog'
