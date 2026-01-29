class Task:
    def __init__(self, id_task: int, title: str, description: str):
        self.id_task = id_task
        self.title = title
        self.description = description
        self.is_done = False

    def done(self):
        self.is_done = True

    def mark_active(self):
        self.is_done = False