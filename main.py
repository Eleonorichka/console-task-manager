from TaskManager import TaskManager
def main():
    manager = TaskManager()
    manager.load_from_file()
    while True:
        print("\n1 - Add_task")
        print("2 - Remove_task")
        print("3 - Mark_done")
        print("4 - Mark_not_done")
        print("5 - Get_all_tasks")
        print("6 - Get_completed_task")
        print("7 - Get_active_tasks")
        print("0 - Exit")
        
        choice = input("Choose: ")
        
        if choice == "1":
            title = input("Title: ")
            description = input("Description: ")
            manager.add_task(title,description)
            
        elif choice == "2":
            task_id = int(input("Task ID: "))
            manager.remove_task(task_id)
            
        elif choice == "3":
            task_id = int(input("Task ID: "))
            manager.mark_done(task_id)
        
        elif choice == "4":
            task_id = int(input("Task ID: "))
            manager.mark_not_done(task_id)
        
        elif choice == "5":
            for task in manager.get_all_tasks():
                print(task.id_task, task.title, task.is_done)
            
        elif choice == "6":
            for task in manager.get_completed_task():
                print(task.id_task, task.title)
            
        elif choice == "7":
            for task in manager.get_active_tasks():
                print(task.id_task, task.title)
            
        elif choice == "0":
            manager.save_to_file()
            break
        else:
            print("Wrong choice")

if __name__ == "__main__":
    main()