from django.shortcuts import render, redirect
from apps.propuesta.forms import Propuesta_Form, ChequeFormSet


def Registrar_Propuesta(request):
    Template_Name = "propuesta/propuesta.html"
    form = Propuesta_Form()
    form_cheque = ChequeFormSet(prefix='cheque')
    if request.method == 'POST':
        form = Propuesta_Form(request.POST)
        if form.is_valid():
            print(form)
            return redirect('registrar_propuesta')
        else:
            print(form.errors)
    return render(
        request,
        Template_Name,
        {
            'propuesta': form,
            'cheque': form_cheque,
        },
    )
