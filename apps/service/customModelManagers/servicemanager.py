from django.db import models
from django.db import connection
import json

class ServiceManager(models.Manager):

    def historyByCustomer(self,customerId):

        cursor = connection.cursor()
        cursor.execute("""select v.id, rfv.brand, rfv.model, s.inDate, s.outDate from customers as c
        join vehicles as v on c.id = v.customers_id
        join refvehicle as rfv on v.refvehicle_id = rfv.id
        join services as s on v.id = s.vehicles_id where c.id = %s order by inDate;""",[customerId])

        info = {"history":[]}
        for row in cursor:
            outDate = None
            if row[4] == None:
                outDate = "En espera"
            else:
                outDate = row[4]
            info["history"].append({"vehiId":row[0],"vehiBrand":row[1],"vehiModel":row[2],"inDate":row[3],"outDate":outDate})

        return info


    def invoiceByService(self,serviceId):

        cursor = connection.cursor()
        cursor.execute("""select c.firstName, c.lastName,v.licensePlate,rfv.brand, rfv.model,t.task, tbr.price , s.inDate, s.outDate, r.firstName, r.lastName  from customers as c join vehicles as v on c.id = v.customers_id
        join services as s on s.vehicles_id = v.id
        join receptionist as r on s.receptionist_id = r.id
        join refvehicle as rfv on rfv.id = v.refvehicle_id
        join details as d on s.id = d.services_id
        join tasks as t on d.tasks_id = t.id
        join tasksbyref as tbr on t.id = tbr.tasks_id where s.id = %s;""",[serviceId])
        invoice = {
            "receptionistFN":None,
            "receptionistLN":None,
            "customerFN":None,
            "customerLN":None,
            "licenseplate":None,
            "brand":None,
            "model":None,
            "repairs":[],
            "indate":0,
            "outdate":0,
            "pay":0,
            }

        i = 0
        for row in cursor:
            if i == 0:
                invoice["receptionistFN"] = row[9]
                invoice["receptionistLN"] = row[10]
                invoice["customerFN"] = row[0]
                invoice["customerLN"] = row[1]
                invoice["licenseplate"] = row[2]
                invoice["brand"] = row[3]
                invoice["model"] = row[4]
                invoice["indate"] = row[7]
                invoice["outdate"] = row[8]

            invoice["repairs"].append({"repair":row[5],"price":row[6]})
            invoice["pay"] = invoice["pay"] + row[6]

            i = i + 1

        return invoice
