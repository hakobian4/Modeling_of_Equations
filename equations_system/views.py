from django.shortcuts import render
from django.views.generic import FormView
from equations_system.forms import EquationForm
from functions import solve_equations



def index(request):
    return render(request, 'index.html')


def home(request):
    return render(request, 'home.html')


def page(request):
    return render(request, 'page.html')


class MyFormView(FormView):

    form_class = EquationForm
    template_name = "form_page.html"
    success_url = "/equations_system/"

    def get(self, request, *args, **kwargs):
        # print(request.GET)
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        response = request.POST
        eq = []
        eq.append(response["equation"])
        solve_equations(eq)
        return super().post(request, *args, **kwargs)
