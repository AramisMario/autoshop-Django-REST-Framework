from django.db import models
from django.db import connection
import json
class TasksManager(models.Manager):

    def tasksbyref(self,refId):
        cursor = connection.cursor()
        cursor.execute("""select tasks.id, price, task, refsAllowed
            from tasksbyref join tasks on tasksbyref.tasks_id = tasks.id;""")

        info = {"reparaciones":[]}
        for row in cursor.fetchall():
            allowed = json.loads(row[3])
            if allowed["allow"] == 'ALL' or refId in allowed["allow"]:
                info["reparaciones"].append({"taskId":row[0],"price":row[1],"task":row[2]})
        return info
