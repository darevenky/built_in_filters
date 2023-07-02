from django.shortcuts import render

# Create your views here.

def built_filters(request):
    d={'c':2,'venky':'VenkY Dare FroM AKn PallI','d':0}
    return render(request,'built_filters.html',d)