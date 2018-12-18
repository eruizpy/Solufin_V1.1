from django.shortcuts import render, redirect
from apps.propuesta.forms import Propuesta_Form, ChequeFormSet


def Registrar_Propuesta(request):
    Template_Name = "propuesta/propuesta.html"
    form = Propuesta_Form()
    form_cheque = ChequeFormSet(prefix='cheque')
    if request.method == 'POST':
        form = Propuesta_Form(request.POST)
        form_cheque = ChequeFormSet(request.POST, prefix='cheque')
        if (
            form.is_valid() and
            form_cheque.is_valid()
        ):
            print(form)
            print(form_cheque)
            return redirect('registrar_propuesta')
        else:
            print(form.errors)
            print(form_cheque.errors)
    return render(
        request,
        Template_Name,
        {
            'propuesta': form,
            'cheque': form_cheque,
        },
    )
