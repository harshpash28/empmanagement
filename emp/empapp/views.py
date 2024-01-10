from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from empapp.models import Emp

# Create your views here.

def index(request):
    # return HttpResponse("Hello World!!!")
    return render(request,'index.html')

def allemp(request):
    e = Emp.objects.all()
    t = len(e)
    context = {}
    context['data'] = e
    context['total'] = t
    return render(request,'allemp.html',context)

def remove(request, eid):
    e = Emp.objects.filter(id = eid)
    e.delete()
    return redirect('/allemp')

def addnemp(request):
    if request.method == 'GET':
        return render(request,'addemp.html')
    else:
        f = request.POST['first_name']
        l = request.POST['last_name']
        e = request.POST['email']
        m = request.POST['mobile']
        a = request.POST['address']
        r = request.POST['role']
        s = request.POST['salary']
        e = Emp.objects.create(first_name=f, last_name=l, email=e, mobile=m, address=a, role=r, salary=s)
        e.save()
        return redirect('/allemp')
        # return render(request,'allemp.html',context)
        # return HttpResponse("Data Fetched Successfully")

def editemp(request,eid):
    if request.method == 'GET':
        e = get_object_or_404(Emp, id=eid)
        context = {}
        context['data'] = e
        return render(request,'editemp.html',context)
    else:
        f = request.POST['first_name']
        l = request.POST['last_name']
        e = request.POST['email']
        m = request.POST['mobile']
        a = request.POST['address']
        r = request.POST['role']
        s = request.POST['salary']
        h = Emp.objects.filter(id=eid).update(first_name=f, last_name=l, email=e, mobile=m, address=a, role=r, salary=s)
        # h.save()
        return redirect('/allemp')
    return render(request,'editemp.html')

def search(request):
    query = request.GET['query']
    all = Emp.objects.filter(first_name__icontains = query)
    context = {}
    context['data'] = all
    return render(request,'search.html',context)
    # return HttpResponse("Hello. This is Search Bar")

def sort(request,sv):
    if sv == '0':
        col = 'first_name'
    else:
        col = '-first_name'
    s = Emp.objects.all().order_by(col)
    context = {}
    context['data'] = s
    return render(request,'allemp.html',context)
