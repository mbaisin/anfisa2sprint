from django.shortcuts import render

from ice_cream.models import IceCream

from django.db.models import Q

def index(request):
    template_name = 'homepage/index.html'
    ice_cream_list = IceCream.objects.values(
        'id', 'title', 'description'
        ).filter(
            Q(Q(is_on_main=True) & Q(is_published=True)) | Q(Q(title__contains='пломбир') & Q(is_published=True))
        )
    context = {
        'ice_cream_list': ice_cream_list,
    }
    return render(request, template_name, context)
