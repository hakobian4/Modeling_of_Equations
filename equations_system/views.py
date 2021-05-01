from django.shortcuts import render, redirect
from django.views.generic import FormView, TemplateView
from equations_system.forms import EquationForm
from django.forms import formset_factory
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from functions import solve_equations
from django.contrib.staticfiles import finders
from django.conf import settings
import os



def index(request):
    return render(request, 'index.html')


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def help(request):
    return render(request, 'help.html')


def show_products(request):
    return render(request, "html_to_pdf.html")
# dow = 0
# globals()['dow'] = 0

def render_pdf_view(request):
    # print("dow2", dow)

    # MyFormView.extra_context['text']

    if len(MyFormView.extra_context['text']) > 0:
        equations = []
        for form in MyFormView.extra_context['form']:
            if len(form.cleaned_data) == 0:
                continue
            else:
                equations.append(form.cleaned_data['equation'])

        # print("dddd",equations)
        template_path = 'html_to_pdf.html'
        context = {'equations': equations, 'answers' : MyFormView.extra_context['text']}
        # Create a Django response object, and specify content_type as pdf
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="report.pdf"'
        # find the template and render it.
        template = get_template(template_path)
        html = template.render(context)

        # create a pdf
        pisa_status = pisa.CreatePDF(
           html, dest=response)
        if pisa_status.err:
           return HttpResponse('We had some errors <pre>' + html + '</pre>')
        return response

    return redirect("solve")



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
            for form in range(len(formset)):
                print(formset[form].cleaned_data)
                if len(formset[form].cleaned_data) == 0:
                    # del formset[form]
                    # formset.remove(formset[form])
                    continue
                else:
                    eq.append(formset[form].cleaned_data['equation'])

            if len(eq) == 0:
                self.extra_context['form'] = formset_factory(EquationForm, extra=len(formset))
                self.extra_context['text'] = []
                # return redirect('solve')
            else:
                self.extra_context['text'] = solve_equations(eq)

                # print("text", self.extra_context['text'])
                # Add the formset to context dictionary
                self.extra_context['form'] = formset
                # dow = self.extra_context['form'].cleaned_data
                # print("dow1", dow)

                # render_pdf_view(self.extra_context['text'])


            return render(request, self.template_name, self.extra_context)

        return super().post(request, *args, **kwargs)

    # def render_pdf_view(self, request, *args, **kwargs):
    #
    #         # MyFormView.extra_context['text']
    #     download_data = self.extra_context['form']
    #     print("dddd", download_data)
    #     template_path = 'html_to_pdf.html'
    #     context = {'download_data': download_data}
    #         # Create a Django response object, and specify content_type as pdf
    #     response = HttpResponse(content_type='application/pdf')
    #     response['Content-Disposition'] = 'filename="report.pdf"'
    #         # find the template and render it.
    #     template = get_template(template_path)
    #     html = template.render(context)
    #
    #         # create a pdf
    #     pisa_status = pisa.CreatePDF(
    #         html, dest=response)
    #     if pisa_status.err:
    #         return HttpResponse('We had some errors <pre>' + html + '</pre>')
    #     return response

        # return super().post(request, *args, **kwargs)

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