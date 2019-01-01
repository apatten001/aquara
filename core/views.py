from django.shortcuts import render, redirect, reverse, HttpResponseRedirect, render_to_response
from django.contrib.auth.hashers import make_password
from django.views.generic import FormView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate
from django.contrib.auth import login, logout
from questanswers.models import Question, Answers, GroupQuestions
from .models import User


from .forms import RegisterForm, LoginForm


# Create your views here.


class DashboardView(FormView):

    def get(self, request):

        content = {}
        if request.user.is_authenticated:
            user = request.user
            user.backend = 'django.contrib.core.backends.ModelBackend'
            quest_obj = Question.objects.filter(user=user)
            answer_obj = Answers.objects.filter(question=quest_obj[0])
            content['userdetail'] = user
            content['questions'] = quest_obj
            content['answers'] = answer_obj
            return render(request, 'dashboard.html', content)
        else:
            return redirect(reverse('login-view'))


class RegisterView(FormView):

    def get(self, request):
        content = {}
        content['form'] = RegisterForm
        return render(request, 'register.html', content)

    def post(self, request, *args, **kwargs):
        content = {}
        form = RegisterForm(request.POST or None)
        if form.is_valid():
            save_it = form.save(commit=False)
            save_it.password = make_password(form.cleaned_data['password'])
            save_it.save()
            login(request, save_it)
            return redirect(reverse('dashboard-view'))
        content['form'] = form
        template = 'register.html'
        return render(request, template, content)


class LoginView(FormView):

    content = {}
    content['form'] = LoginForm

    @ method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(LoginView, self).dispatch(self, request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        content = {}
        if request.user.is_authenticated:
            return redirect(reverse('dashboard-view'))
        else:
            return render(request, 'login.html', content)


    def post(self, request):

        content = {}
        email = request.POST['email']
        password = request.POST['password']

        try:
            users = User.objects.filter(email=email)
            user = authenticate(request, username=users.firsts().username, password=password)
            login(request, user)
            return redirect(reverse('dashboard-view'))
        except Exception as e:
            content = {}
            content['form'] = LoginForm
            content['error'] = 'Unable to login with provided credentials' + e
            return render_to_response( 'login.html', content)


class LogoutView(FormView):

    def get(self, request):
        logout(request)
        HttpResponseRedirect('/')

