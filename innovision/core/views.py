from django.shortcuts import render, redirect
from .models import StartupIdea
from .forms import StartupIdeaForm

def home(request):
    if request.method == 'POST':
        form = StartupIdeaForm(request.POST)
        if form.is_valid():
            form.save()  # Save the idea
            return redirect('home')  # Redirect to homepage

    form = StartupIdeaForm()
    ideas = StartupIdea.objects.all()  # Fetch all submitted ideas
    return render(request, 'core/home.html', {'form': form, 'ideas': ideas})
