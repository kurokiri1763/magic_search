from django.shortcuts import render, redirect,get_object_or_404
from .forms import MagicForm
from search.models import Magic

def edit_magic(request, magic_id):

    magic = get_object_or_404(Magic, id=magic_id)

    if request.method == 'POST':
        form = MagicForm(request.POST, instance=magic)
        if form.is_valid():
            form.save() 
            return redirect('magic_detail', magic.id) 
    else:
        form = MagicForm(instance=magic)

    return render(request, 'edit/edit_magic.html', {'form': form, 'magic': magic})
