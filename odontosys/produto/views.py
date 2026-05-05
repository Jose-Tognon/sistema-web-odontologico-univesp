from django.shortcuts import render,redirect,get_object_or_404
from .models import Produto
from .forms import ProdutoForm
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.decorators import login_required,user_passes_test
from datetime import date, timedelta

# Create your views here.
def is_admin(user):
    return user.is_staff

@login_required
@user_passes_test(is_admin, login_url='login')
def produto_list(request):
    template_name = 'produto_list.html'
    objects = Produto.objects.all()

    hoje = date.today()

    for produto in objects:
        if produto.validade < hoje:
            produto.status_validade = 'expirado'
        elif produto.validade <= hoje + timedelta(days=7):
            produto.status_validade = 'perto'
        else:
            produto.status_validade = 'ok'

    context = {'object_list': objects}
    return render(request, template_name, context)

def produto_details(request,pk):
    template_name = 'produto_details.html'
    obj = Produto.objects.get(pk=pk)
    context = {'object':obj}
    return render(request,template_name,context)

class ProdutoCreate(CreateView):
    model = Produto
    template_name = 'produto_form.html'
    form_class = ProdutoForm


class ProdutoUpdate(UpdateView):
    model = Produto
    template_name = 'produto_form.html'
    form_class = ProdutoForm

def alterar_estoque(request, pk):
    objeto = get_object_or_404(Produto, pk=pk)

    if request.method == 'POST':
        acao = request.POST.get('acao')

        if acao == 'aumentar':
            objeto.estoque += 1

        elif acao == 'diminuir':
            if objeto.estoque > 0:  # evita negativo
                objeto.estoque -= 1

        objeto.save()

    return redirect('produto:produto_list')

def produto_delete(request, pk):
    produto = get_object_or_404(Produto, pk=pk)

    if request.method == "POST":
        produto.delete()
        return redirect('produto:produto_list')