from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Category, Manufacturer, Tool, ToolCopy
from django.contrib.auth.decorators import login_required, permission_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import SignUpForm
from django.contrib.auth import login
from datetime import date, timedelta

def home(request):
    return render(request, 'home.html')


def manufacturers(request):
    manufacturers = Manufacturer.objects.all()
    context = {
        'manufacturers': manufacturers,
    }
    return render(request, 'manufacturers.html', context=context)


def categories(request):
    categories = Category.objects.all()
    context = {
        'categories': categories,
    }
    return render(request, 'categories.html', context=context)


def manufacturer(request, manufacturer_id):
    single_manufacturer = get_object_or_404(Manufacturer, pk=manufacturer_id)
    return render(request, 'manufacturer.html', {'manufacturer': single_manufacturer})


def tools(request):
    tools = Tool.objects.all()
    context = {
        'tools': tools,
    }
    return render(request, 'tools.html', context=context)


def tool(request, tool_id):
    single_tool = get_object_or_404(Tool, pk=tool_id)
    return render(request, 'tool.html', {'tool': single_tool})


@login_required()
def mytools(request):
    toolcopies = ToolCopy.objects.filter(customer=request.user.id)
    toolcopies_all = ToolCopy.objects.all()
    context = {
        'toolcopies': toolcopies,
        'toolcopies_all': toolcopies_all,
    }
    return render(request, 'user_tools.html', context=context)


def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse('home'))
    else:
        form = SignUpForm()
    return render(request, 'registration/sign_up.html', context={'form': form})


@login_required
def user_profile(request):
    return render(request, 'registration/user_profile.html')


class ToolCopyCreateView(LoginRequiredMixin, CreateView):
    model = ToolCopy
    fields = ['tool', 'price', 'due_back', 'customer', 'status']
    success_url = "/tools"
    template_name = 'toolcopy_create_form.html'

    def form_valid(self, form):
        # form.instance.reader = self.request.user
        return super().form_valid(form)


class ToolCopyUpdateView(LoginRequiredMixin, UpdateView):
    model = ToolCopy
    fields = ['tool', 'price', 'due_back', 'customer', 'status']
    success_url = "/mytools"
    template_name = 'toolcopy_update.html'

    def test_func(self):
        book = self.get_object()
        return self.request.user == book.reader


class ToolCopyUpdateView_reserve(LoginRequiredMixin, UpdateView):
    model = ToolCopy
    fields = ['tool']
    success_url = "/tools/"
    template_name = 'toolcopy_update_reserve_form.html'

    def form_valid(self, form):
        form.instance.customer = self.request.user
        form.instance.status = 'r'
        form.instance.due_back = date.today() + timedelta(days=10)
        return super().form_valid(form)

    def test_func(self):
        toolcopy = self.get_object()
        return self.request.user == toolcopy.customer


class ToolCopyUpdateView_cancel_reserve(LoginRequiredMixin, UpdateView):
    model = ToolCopy
    fields = ['tool']
    success_url = "/tools/"
    template_name = 'toolcopy_update_cancel_reserve_form.html'

    def form_valid(self, form):
        form.instance.customer = None
        form.instance.status = 'a'
        form.instance.due_back = date.today() + timedelta(days=30)
        return super().form_valid(form)

    def test_func(self):
        toolcopy = self.get_object()
        return self.request.user == toolcopy.customer