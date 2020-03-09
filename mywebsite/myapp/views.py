from django.shortcuts import render

from.models import Base,TutorailDjango





def index(request):
    return render(request,'index.html')




def addcard(request):
    products = TutorailDjango.objects.filter(available=True )
    context = {"products":products}
    return render(request,'display.html',context)




def learnpython(request):
    products = TutorailDjango.objects.filter(available=True )
    context = {"products":products}
    return render(request,'learnpython.html',context)



def article(request):
    return render(request,"article.html")