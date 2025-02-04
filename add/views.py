from django.shortcuts import render, redirect
from .forms import MagicForm

def add_magic(request):
    if request.method == 'POST':
        form = MagicForm(request.POST)
        if form.is_valid():
            form.save()  # フォームのデータを保存
            return redirect('magic_search')  # 成功したら検索ページにリダイレクト
    else:
        form = MagicForm()  # 空のフォームを表示

    return render(request, 'add/add_magic.html', {'form': form})