from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .forms import ColorsForm

from .models import Colors
# Create your views here.
def colors_list(request):
    colors = Colors.objects.all()
    return render(request, 'style/colors_list.html', {'colors': colors})

def colors_detail(request, pk):
    colors = get_object_or_404(Colors, pk=pk)
    return render(request, 'style/color_detail.html', {'colors': colors})

def colors_new(request):
    if request.method == "POST":
        form = ColorsForm(request.POST)
        if form.is_valid():
            colors = form.save(commit=False)
            #colors.author = request.user lets add the user who created the style later
            colors.save()
            return redirect('colors_detail', pk=colors.pk)
    else:
        form = ColorsForm()
    return render(request, 'style/colors_edit.html', {'form': form})

def colors_edit(request, pk):
    colors = get_object_or_404(Colors, pk=pk)
    if request.method == "POST":
        form = ColorsForm(request.POST, instance=colors)
        if form.is_valid():
            colors = form.save(commit=False)
            colors.author = request.user
            colors.published_date = timezone.now()
            colors.save()
            return redirect('colors_detail', pk=colors.pk)
    else:
        form = ColorsForm(instance=colors)
    return render(request, 'style/colors_edit.html', {'form': form})