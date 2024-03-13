from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from . models import Memeber
from django.db.models import Q

# Create your views here.
def names(request):
    mynames= Memeber.objects.all().values()
    template = loader.get_template("all_members.html")
    context = {
        'mynames': mynames
    }
    return HttpResponse(template.render(context,request))

def details(request, id):
    myname = Memeber.objects.get(id=id)
    template = loader.get_template("details.html")
    context={
        'myname': myname,
    
    }
    return HttpResponse(template.render(context,request))


def main(response):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())


def index(response):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def kwame(response):
    return HttpResponse("<h1> He's a boy who likes walking</h1>")


def testing(request):
  template = loader.get_template('template.html')
  context = {
    'fruits': ['Apple', 'Banana', 'Cherry', 'Oranges', 'Kiwi'],
  }
  return HttpResponse(template.render(context, request))

def test(request):
  mydata = Memeber.objects.values().all()
#   Order the result alphabetically by firstname:
#   mydata = Memeber.objects.all().order_by('firstname').values()
  
# Order the result firstname descending:
#   mydata = Memeber.objects.all().order_by('-firstname').values()
  
  mydata = Memeber.objects.all().order_by('lastname', '-id').values()


  template = loader.get_template('test.html')
  context = {
    'mymembers': mydata,
  }
  return HttpResponse(template.render(context, request))



# The filter() method takes the arguments as **kwargs (keyword arguments),
# so you can filter on more than one field by separating them by a comma.
# AND
# def test(request):
#   mydata = Memeber.objects.filter(lastname='Refsnes', id=2).values()
#   template = loader.get_template('test.html')
#   context = {
#     'mymembers': mydata,
#   }
#   return HttpResponse(template.render(context, request))


# Return the records where firstname starts with the letter 'K':
# def test(request):
#   mydata = Memeber.objects.filter(firstname__startswith='k').values()
#   template = loader.get_template('test.html')
#   context = {
#     'mymembers': mydata,
#   }
#   return HttpResponse(template.render(context, request))

# Get all records that have the value "bias" in the firstname column:
# The contains lookup is used to get records that contains a specified value.
# def test(request):
#   mydata = Memeber.objects.filter(firstname__contains='bias').values()
#   template = loader.get_template('test.html')
#   context = {
#     'mymembers': mydata,
#   }
#   return HttpResponse(template.render(context, request))




# The icontains lookup is used to get records that contains a specified value.
# The icontains lookup is case insensitive.
# def test(request):
#   mydata = Memeber.objects.filter(lastname__icontains='ref').values()
#   template = loader.get_template('test.html')
#   context = {
#     'mymembers': mydata,
#   }
#   return HttpResponse(template.render(context, request))



# Get all records where firstname ends with the letter "s":
# mydata = Member.objects.filter(firstname__endswith='s').values()



# Return records where firstname is either "Emil" or Tobias":
# def test(request):
#   mydata = Memeber.objects.filter(Q(firstname='Kwame') | Q(firstname='Johan')).values()
#   template = loader.get_template('test.html')
#   context = {
#     'mymembers': mydata,
#   }
#   return HttpResponse(template.render(context, request))


# mydata = Member.objects.filter(firstname='Emil').values() | Member.objects.filter(firstname='Tobias').values()

# def test(request):
#   mydata = Memeber.objects.values_list('firstname' )
#   template = loader.get_template('test.html')
#   context = {
#     'mymembers': mydata,
#   }
#   return HttpResponse(template.render(context, request))


# def test(request):
#   mydata = Memeber.objects.filter(firstname='Kwame').values()
#   template = loader.get_template('test.html')
#   context = {
#     'mymembers': mydata,
#   }
#   return HttpResponse(template.render(context, request))