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
