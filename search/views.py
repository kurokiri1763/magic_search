from django.shortcuts import render,  get_object_or_404
from django.db.models import Q
from .models import Magic

def magic_list(request):
    # 既存の一覧表示
    magics = Magic.objects.all()
    return render(request, 'search/magic_list.html', {'magics': magics})

def magic_detail(request, magic_id):
    # 既存の詳細表示
    magic = get_object_or_404(Magic, id=magic_id)
    return render(request, 'search/magic_detail.html', {'magic': magic})

def magic_search(request):
    """
    魔法の検索ビュー
    """
    query = request.GET.get('q', '')
    magic_type = request.GET.get('magic_type', '')
    order_by = request.GET.get('order_by', 'rank')

    # 基本のクエリセット
    magic_queryset = Magic.objects.all()

    # 検索キーワードによるフィルタリング
    if query:
        magic_queryset = magic_queryset.filter(
            Q(name__icontains=query) |
            Q(summary__icontains=query) |
            Q(effect__icontains=query) |
            Q(extended_effect1__icontains=query) |
            Q(extended_effect2__icontains=query)
        )

    # 魔法の系統によるフィルタリング
    if magic_type:
        magic_queryset = magic_queryset.filter(magic_type=magic_type)

    # ソート
    magic_queryset = magic_queryset.order_by(order_by)

    return render(request, 'search/magic_search.html', {
        'magics': magic_queryset,
        'query': query,
        'magic_type': magic_type,
        'order_by': order_by,
    })
