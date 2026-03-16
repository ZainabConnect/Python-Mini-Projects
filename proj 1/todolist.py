def display():
    print("1. Add task")
    print("2. remove task")
    print("3. view task")
    print("4. exit")
    
def addtask(tasks):
    task=input("enter task ")
    tasks.append(task)
    print(f"task '{task}' added successfully!")

def viewtask(tasks):
    if not tasks:
        print("sorry no tasks to display")
    
    else:
        print("\n --Your Tasks-- ")
        for i in range(len(tasks)):
            print(f"{i+1}. {tasks[i]}")
        print()


    
def deletetask(tasks):
    if not tasks:
        print("sorry no tasks to delete")
        return
    
    viewtask(tasks)
    try:
        num=int(input("enter the task number to be deleted: "))
        if num<1 or num>len(tasks):
            print("invalid number entered!")
        else:
            index=num-1
            deleted=tasks.pop(index)
            print(f"task '{deleted}' deleted successfully!")
    
    except ValueError:
        print("enter a valid number!")

def savetask(tasks):
    try:
        with open('task.txt','w') as file:
            for task in tasks:
                file.write(task + '/n')
        print("file saved succeffully!")
    except Exception as e:
        print(f"error saving task: {e}")

def loadtask():
    try:
        with open('task.txt','r') as file:
            tasks = []
            for line in file:
                tasks.append(line.strip())
        return tasks
    except FileNotFoundError:
        print("no tasks found")
        return []
    except Exception as e:
        print(f"error loading tasks: {e}")
        return []
    
def main():
    tasks=loadtask()
    while True:
        display()
        n=input("enter your choice: ")
        if n =='1':
            addtask(tasks)
        elif n =='2':
            deletetask(tasks)
        elif n =='3':
            viewtask(tasks)
        elif n == '4':
            savetask(tasks)
            print("Goodbye!")
            break 
        else:
            print("invalid choice!")
        
if __name__ == "__main__":
    main()  

    