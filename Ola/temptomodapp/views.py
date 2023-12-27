from django.shortcuts import render

# Create your views here.
from temptomodapp.forms import empfrom

def empview(request):
    if request.method == 'POST':
        form = empfrom(request.POST or None, request.FILES)
        if form.is_valid():
            form.full_clean()
            form.save()
        else:
            return render(request, 'temptomod.html', {'form': form})

    form = empfrom()
    return render(request, 'temptomod.html', {'form': form})