from django.shortcuts import render, redirect
from django.views.generic import FormView, TemplateView
from equations_system.forms import EquationForm
from django.forms import formset_factory
from django.urls import reverse_lazy
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

    form_class = formset_factory(EquationForm, extra=1)
    respon = []
    template_name = "solve_new.html"
    success_url = "/equations_system/solve/"
    extra_context = {'form': form_class, 'text': respon}

    def get(self, request, *args, **kwargs):

        return super().get(request, *args, **kwargs)


    def post(self, request, *args, **kwargs):


        formset = self.form_class(request.POST or None)

        # print formset data if it is valid
        if formset.is_valid():
            eq = []
            for form in formset:
                print(form.cleaned_data)

                eq.append(form.cleaned_data['equation'])
            self.extra_context['text'] = solve_equations(eq)

            # Add the formset to context dictionary
            self.extra_context['form'] = formset

            return render(request, self.template_name, self.extra_context)

        return super().post(request, *args, **kwargs)







        # form = EquationForm(request.POST)
        # print("aaaaaa", len(form['equation']))
        # # response = request.POST
        # if form.is_valid():
        #     eq = []
        #     eq.append(form.cleaned_data['equation'])
        #     result = solve_equations(eq)
        #     args = {'form':form, 'text': result}
        #     return render(request, self.template_name, args)
        # context = {}