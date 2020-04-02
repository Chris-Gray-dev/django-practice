from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request,*args, **kwargs):
    print(request.user)
    print(args,kwargs)
    return render(request,"home.html",{})



def contacts_view(request,*args, **kwargs):
    myContext={
        "my_text"   : "zContact text ",
        "my_number" : 123,
        "true_val" : True,
        "cat_types" : ["smol","reg","chonk"],
        "my_html": "<h1> this is my html</h1>"
    }
    return render(request,"contact.html",myContext)