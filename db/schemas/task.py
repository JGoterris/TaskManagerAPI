def task_schema(task) -> dict:
    return {"id": str(task["_id"]), "name": task["name"], "description": task["description"], "status": task["status"], "createdAt": task["createdAt"], "updatedAt": task["updatedAt"]}

def tasks_schema(tasks) -> list:
    return [task_schema(task) for task in tasks]