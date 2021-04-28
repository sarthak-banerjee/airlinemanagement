from .models import air_data
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def crud(request):
    button=request.GET['b1']
    print(button)
    if button == "Insert":
        name = request.GET['t2']
        age = int(request.GET['t3'])
        last_ser = (request.GET['t4'])
        ser_req = bool(request.GET['t5'])
        dist = float(request.GET['t6'])
        e = air_data.objects.create(name=name,age=age,last_service_date=last_ser,service_required=ser_req,distance_travelled=dist)
        msg = "Record Saved"
        return render(request,'result.html',{'msg':msg})
    elif button == "Select":
        id = int(request.GET['t1'])
        msg = air_data.objects.get(pk=id)
        #obj=air_data.object.get(pk=id)
        #print(msg.id)
        msg1 = msg.id
        #print(msg.name)
        msg2 = msg.name
        #print(msg.age)
        msg3 = msg.age
        #print(msg.last_service_date)
        msg4 = msg.last_service_date
        #print(msg.service_required)
        msg5 = msg.service_required
        #print(msg.distance_travelled)
        msg6 = msg.distance_travelled
        return render(request,'show.html',{'msg1':msg1,'msg2':msg2,'msg3':msg3,'msg4':msg4,'msg5':msg5,'msg6':msg6})
    elif button == "Update":
        id = int(request.GET['t1'])
        name = request.GET['t2']
        age = int(request.GET['t3'])
        last_ser = (request.GET['t4'])
        ser_req = bool(request.GET['t5'])
        dist = float(request.GET['t6'])
        obj = air_data.objects.get(pk=id)
        obj.name = name
        obj.age = age
        obj.last_service_date = last_ser
        obj.service_required = ser_req
        obj.distance_travelled = dist
        obj.save()
        msg="Record Updated"
        return render(request,'result.html',{'msg':msg})
    elif button == "Delete":
        id = int(request.GET['t1'])
        obj = air_data.objects.get(pk=id)
        obj.delete()
        msg="Record Deleted"
        return render(request,'result.html',{'msg':msg})