from django.shortcuts import render


def home(request):
    templateFile = 'index.html'  # in the BASE_DIR/templates
    return render(request, templateFile)
