from django.shortcuts import render
from django.views.generic import FormView
from equations_system.forms import EquationForm
from functions import solve_equations



def index(request):
    return render(request, 'index.html')


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def help(request):
    return render(request, 'help.html')


class MyFormView(FormView):

    form_class = EquationForm
    template_name = "solve.html"
    success_url = "/equations_system/"

    def get(self, request, *args, **kwargs):
        # print(request.GET)
        return super().get(request, *args, **kwargs)


    def post(self, request, *args, **kwargs):
        form = EquationForm(request.POST)
        # response = request.POST
        if form.is_valid():
            eq = []
            eq.append(form.cleaned_data['equation'])
            result = solve_equations(eq)
            args = {'form':form, 'text': result}
            return render(request, self.template_name, args)

        return super().get(request, *args, **kwargs)