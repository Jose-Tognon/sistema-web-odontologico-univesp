from django.shortcuts import render,redirect
from .models import Produto
from .forms import ProdutoForm

# Create your views here.
def produto_list(request):
    template_name = 'produto_list.html'
    objects = Produto.objects.all()
    context = {'object_list':objects}
    return render(request,template_name,context)

def produto_details(request,pk):
    template_name = 'produto_details.html'
    obj = Produto.objects.get(pk=pk)
    context = {'object':obj}
    return render(request,template_name,context)

def produto_add(request):
    form = ProdutoForm()
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('produto:produto_list')
    context = {'form':form}
    return render(request,'produto_form.html',context) 