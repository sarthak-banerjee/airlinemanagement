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
        no_of_flights = int(request.GET['t3'])
        last_ser = (request.GET['t4'])
        ser_req = bool(request.GET['t5'])
        dist = float(request.GET['t6'])
        base_station = request.GET['t7']
        veg = request.GET['t8']
        non_veg = request.GET['t9']
        jain = request.GET['t10']
        continental = request.GET['t11']
        e = air_data.objects.create(name=name,no_of_flights=no_of_flights,last_service_date=last_ser,service_required=ser_req,distance_travelled=dist,base_station=base_station,veg=veg,non_veg=non_veg,jain=jain,continental=continental)
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
        #print(msg.no_of_flights)
        msg3 = msg.no_of_flights
        #print(msg.last_service_date)
        msg4 = msg.last_service_date
        #print(msg.service_required)
        msg5 = msg.service_required
        #print(msg.distance_travelled)
        msg6 = msg.distance_travelled
        #print(msg.base_station)
        msg7 = msg.base_station
        #print(msg.veg)
        msg8 = msg.veg
        #print(msg.non_veg)
        msg9 = msg.non_veg
        #print(msg.jain)
        msg10 = msg.jain
        #print(msg.continental)
        msg11 = msg.continental
        return render(request,'show.html',{'msg1':msg1,'msg2':msg2,'msg3':msg3,'msg4':msg4,'msg5':msg5,'msg6':msg6,'msg7':msg7,'msg8':msg8,'msg9':msg9,'msg10':msg10,'msg11':msg11})
    elif button == "Update":
        id = int(request.GET['t1'])
        name = request.GET['t2']
        no_of_flights = int(request.GET['t3'])
        last_ser = (request.GET['t4'])
        ser_req = bool(request.GET['t5'])
        dist = float(request.GET['t6'])
        base_station = request.GET['t7']
        veg = request.GET['t8']
        non_veg = request.GET['t9']
        jain = request.GET['t10']
        continental = request.GET['t11']
        obj = air_data.objects.get(pk=id)
        obj.name = name
        obj.no_of_flights = no_of_flights
        obj.last_service_date = last_ser
        obj.service_required = ser_req
        obj.distance_travelled = dist
        obj.base_station = base_station
        obj.veg = veg
        obj.non_veg = non_veg
        obj.jain = jain
        obj.continental = continental
        obj.save()
        msg="Record Updated"
        return render(request,'result.html',{'msg':msg})
    elif button == "Delete":
        id = int(request.GET['t1'])
        obj = air_data.objects.get(pk=id)
        obj.delete()
        msg="Record Deleted"
        return render(request,'result.html',{'msg':msg})