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

        a = (request.GET['t5'])
        if a == '1':
            ser_req = bool(True)
        elif a == '0' :
            ser_req = bool(False)
 
        dist = float(request.GET['t6'])
        base_station = request.GET['t7']
        image = request.GET['t8']
        accept = request.GET['t9']
        
        e = air_data.objects.create(name=name,no_of_flights=no_of_flights,last_service_date=last_ser,service_required=ser_req,distance_travelled=dist,base_station=base_station,image=image,accept=accept)
        msg = "Record Saved"
        return render(request,'result.html',{'msg':msg})
    elif button == "Select":
        id = int(request.GET['t1'])
        msg = air_data.objects.get(pk=id)

        msg1 = msg.id
        msg2 = msg.name
        msg3 = msg.no_of_flights
        msg4 = msg.last_service_date
        if msg.service_required == 0:
            msg5 = "No"
        elif msg.service_required == 1:
            msg5 ="Yes"
        msg6 = msg.distance_travelled
        msg7 = msg.base_station 
        msg8 = msg.image
        msg9 = msg.accept
        return render(request,'show.html',{'msg1':msg1,'msg2':msg2,'msg3':msg3,'msg4':msg4,'msg5':msg5,'msg6':msg6,'msg7':msg7,'msg8':msg8,'msg9':msg9})
    elif button == "Update":
        id = int(request.GET['t1'])
        name = request.GET['t2']
        no_of_flights = int(request.GET['t3'])
        last_ser = (request.GET['t4'])
        ser_req = bool(request.GET['t5'])
        dist = float(request.GET['t6'])
        base_station = request.GET['t7']
        image = request.GET['t8']
        accept = request.GET['t9']
        obj = air_data.objects.get(pk=id)
        obj.name = name
        obj.no_of_flights = no_of_flights
        obj.last_service_date = last_ser
        obj.service_required = ser_req
        obj.distance_travelled = dist
        obj.base_station = base_station
        obj.image = image
        obj.accept= accept
        obj.save()
        msg="Record Updated"
        return render(request,'result.html',{'msg':msg})
    elif button == "Delete":
        id = int(request.GET['t1'])
        obj = air_data.objects.get(pk=id)
        obj.delete()
        msg="Record Deleted"
        return render(request,'result.html',{'msg':msg})