from django.db import models
from django.db import connection
import json
class TaskManager(models.Manager):

    def tasksbyref(self,refId):
        cursor = connection.cursor()
        cursor.execute("""select task.id, price, task, refsAllowed
            from tasksbyref join task on tasksbyref.task_id = task.id;""")

        info = {"reparaciones":[]}
        for row in cursor.fetchall():
            allowed = json.loads(row[3])
            if allowed["allow"] == 'ALL' or refId in allowed["allow"]:
                info["reparaciones"].append({"taskId":row[0],"price":row[1],"task":row[2],})
        return info
