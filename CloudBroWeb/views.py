from django.shortcuts import render
from blog.views import render_widget


def home(request):
    return render(request, 'index.html', {'blogwidget': render_widget(5)})
