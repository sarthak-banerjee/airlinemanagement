from .models import air_data
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def crud(request):
    button=request.GET['b1']
    print(button)
    if button=="Insert":
        name=request.GET['t2']
        addr=request.GET['t3']
        age=int(request.GET['t4'])
        e=air_data.objects.create(name=name,address=addr,age=age)
        msg="Record Saved"
        return render(request,'result.html',{'msg':msg})
    elif button=="Select":
        id=int(request.GET['t1'])
        msg=air_data.objects.get(pk=id)
        #obj=air_data.object.get(pk=id)
        print(msg.id)
        msg1=msg.id
        print(msg.name)
        msg2=msg.name
        print(msg.address)
        msg3=msg.address
        print(msg.age)
        msg4=msg.age
        return render(request,'show.html',{'msg1':msg1,'msg2':msg2,'msg3':msg3,'msg4':msg4})
    elif button=="Update":
        id=int(request.GET['t1'])
        name=request.GET['t2']
        addr=request.GET['t3']
        age=int(request.GET['t4'])
        obj=air_data.objects.get(pk=id)
        obj.name=name
        obj.address=addr
        obj.age=age
        obj.save()
        msg="Record Updated"
        return render(request,'result.html',{'msg':msg})
    elif button=="Delete":
        id=int(request.GET['t1'])
        obj=air_data.objects.get(pk=id)
        obj.delete()
        msg="Record Deleted"
        return render(request,'result.html',{'msg':msg})