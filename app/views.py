from  django.shortcuts  import  render
from .models import *
from django.template import loader
from django.contrib.auth.decorators import login_required


def home(request):
    return  render(request=request,template_name= 'home.html',)

@login_required
def floor(request):
    floor = Floor.objects.all().values()
    print(type(floor))
    context = {'floor': floor,}
    return  render(request,'floor.html',context)

@login_required
def seating(request):
    floor = Floor.objects.all().values()
    context = {'floor': floor,}
    return  render(request,'floor.html',context)

@login_required
def addPlan(request):
    context={}
    if 'cubicle' in request.GET:
        cub=[]
        emp=[]
        err=[]
        for i in request.GET.getlist('cubicle'):
            cub.append(i)
        for i in request.GET.getlist('employee'):
            emp.append(i)
        m=0

        for i in range(0,len(cub)):
            c=Seating.objects.filter(cubicle_id=cub[i]).values()
            m=max(m,len(c)+1)
            if len(c)!=0:
                print(emp[i])
                if c[len(c)-1]['employee_id_id']!=None and int(c[len(c)-1]['employee_id_id'])!=int(emp[i]):
                    t=Employee.objects.filter(employee_id=c[len(c)-1]['employee_id_id'])
                    err.append(t[0].employee_name+" already has been assigned cubicle number "+cub[i]+". Reassign cubicle to complete the step.")
        if len(err)==0:
            err.append("Values updated succesfully")
            for i in range(0,len(cub)):
                t=Seating(employee_id=Employee.objects.get(employee_id=emp[i]),cubicle_id=Cubicle.objects.get(cubicle_number=cub[i]))
                t.save()
            c=Cubicle.objects.filter(floor_number_id=1).values()
            print(c)

            for i in c:
                t=Seating.objects.filter(cubicle_id=i['cubicle_number']).values()
                if len(t)!=m:
                    t=Seating(cubicle_id=Cubicle.objects.get(cubicle_number=i['cubicle_number']))
                    t.save()
        print(err)
        print(type(context))
        floor=str(1)
        employee = Employee.objects.all().values()
        cubicle = Cubicle.objects.filter(floor_number=floor).values()
        context['employee']=employee
        context['cubicle']=cubicle
        context['tex']=err

        return render(request,'addPlan.html',context)
    
    floor=str(request.POST['floor'])
    employee = Employee.objects.all().values()
    cubicle = Cubicle.objects.filter(floor_number=floor).values()
    print(cubicle)
    context = {'employee':employee,'cubicle':cubicle, 'floor':floor}
    print(type(context))
    return  render(request,'addPlan.html',context)

@login_required
def change(request):
    #floor=str(request.POST['floor'])
    employee = Employee.objects.all().values()
    cubicle = Cubicle.objects.filter(floor_number=floor).values()
    print(cubicle)
    context = {'employee':employee,'cubicle':cubicle}


