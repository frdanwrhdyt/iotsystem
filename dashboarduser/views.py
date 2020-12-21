from django.shortcuts import redirect, render
import base64

# Create your views here.

# def image_view(text_data):
#     context = text_data


def dashboard_view(request):
    context = {
        'link': 'logout'
    }
    if request.user.is_authenticated:
        return render(request, 'monitor/dashboard.html', context=context)

    if not request.user.is_authenticated:
        return render(request, 'modal/popup.html')
