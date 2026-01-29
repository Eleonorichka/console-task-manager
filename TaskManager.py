import json
from task import Task

class TaskManager:
    def __init__(self):
        self.task_list: list[Task] = []
        self.next_id = 1
    

    def load_from_file(self):
        try:
            with open('tasks.json', 'r') as f:
                data = json.load(f)
                for item in data:
                    task = Task(
                        id_task=item['id'],
                        title=item['title'],
                        description=item['description'],
                        is_done=item['is_done']
                    )
                    self.task_list.append(task)
                    if task.id_task >= self.next_id:
                        self.next_id = task.id_task + 1
        except FileNotFoundError:
            self.task_list = []

    def save_to_file(self):
        data = []
        for task in self.task_list:
            task_data = {
                "id": task.id_task,
                "title": task.title,
                "description": task.description,
                "is_done": task.is_done
            }
            data.append(task_data)
        with open('tasks.json', 'w') as f:
            json.dump(data, f, indent=4)

    def add_task(self, title, description):
        id_task = self.next_id
        task = Task(id_task, title, description)
        self.task_list.append(task)
        self.next_id += 1
    
    def remove_task(self, task_id):
        for task in self.task_list:
            if task.id_task == task_id:
                self.task_list.remove(task)
                break
    
    def mark_done(self, task_id):
        for task in self.task_list:
            if task.id_task == task_id:
                task.done()
                break
    
    def mark_not_done(self, task_id):
        for task in self.task_list:
            if task.id_task == task_id:
                task.mark_active()
                break
    
    def get_all_tasks(self):
        return self.task_list
    
    def get_completed_task(self):
        return [task for task in self.task_list if task.is_done]
    
    def get_active_tasks(self):
        return [task for task in self.task_list if not task.is_done]