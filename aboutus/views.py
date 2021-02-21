from django.shortcuts import render


# Create your views here.
def aboutus(request):
    """ A view to display about page """
    return render(request, 'aboutus/aboutus.html')