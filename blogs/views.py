from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from blogs.forms import CommentCreateForm, BlogCreateForm
from blogs.models import Blog, Contact


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


def contact_view(request):
    if request.method == 'GET':
        return render(request, 'contact.html')
    elif request.method == 'POST':
        data = request.POST
        name = data.get('name')
        email = data.get('email')
        subject = data.get('subject')
        message = data.get('message')
        try:
            msg = Contact.objects.create(name=name, email=email, subject=subject, message=message)
            msg.save()
            messages.success(request, "Xabaringiz yuborildi!")
            messages.add_message(request, messages.INFO, "Hushyor bo'lavering")
        except Exception as err:
            messages.error(request, err)
        return render(request, 'contact.html')


def about_view(request):
    if request.method == 'GET':
        return render(request, 'about.html')

# -----------------------------------------------------------------------


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

# ============================================================================


# generic views: CreateView, UpdateView, DetailView, DeleteView, ListView
class HomePageGenericView(ListView):
    model = Blog
    template_name = 'home.html'
    context_object_name = 'blogs'


class BlogDetailGenericView(DetailView):
    model = Blog
    template_name = 'detail.html'
    context_object_name = 'blog'

    # def get_object(self, queryset=None):
    #     slug = self.request.GET.get('slug')
    #     if slug:
    #         try:
    #             blog = Blog.objects.get(slug=slug)
    #         except Blog.DoesNotExist:
    #             return HttpResponse("Bunday sahifa mavjud emas!")
    #     else:
    #         return HttpResponse("Bunday sahifa mavjud emas!")
    #     return blog

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'comment_form': CommentCreateForm()
        })
        return context

    def post(self, request, *args, **kwargs):
        blog = self.get_object()
        author = request.user
        if not author.is_authenticated:
            return redirect('login')
        data = request.POST
        form = CommentCreateForm(data)
        if form.is_valid():
            form.instance.blog = blog
            form.instance.author = author
            form.save()
            return redirect(request.META.get('HTTP_REFERER'))


class BlogCreateGenericView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    form_class = BlogCreateForm
    template_name = 'create.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        user = self.request.user
        if user.is_superuser:
            return True
        return False


class BlogUpdateGenericView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Blog
    template_name = 'update.html'
    fields = ['title', 'body', 'photo', 'video']

    def test_func(self):
        user = self.request.user
        return self.get_object().author == user


class BlogDeleteGenericView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Blog
    template_name = 'delete.html'
    success_url = reverse_lazy('home')

    def test_func(self):
        return self.get_object().author == self.request.user


class SearchView(View):
    def get(self, request):
        query = request.GET.get('query')
        if query:
            blogs = Blog.objects.filter(
                Q(body__icontains=query) | Q(title__icontains=query)
            )
            print(blogs)
        else:
            blogs = []
        context = {'blogs': blogs}
        return render(request, 'search.html', context)
