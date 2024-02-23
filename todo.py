task = []
print ("TO DO LIST APPLICATION")
print ("1. Add task\n2. Remove task\n3. View tasks\n4. Save and exit")
while True:
    choice= int (input ("Enter your choice: "))
    if choice == 1:
       n = int(input("ENTER THE NUMBER OF TASKS TO ADD: "))

       for _ in range(n):
           todo = input("ENTER THE TASK: ")
           found = False
    
          # Check if the task or its variation is already in the list
       for existing_todo in task:
            if existing_todo.lower() == todo.lower() or existing_todo.lower() in todo.lower() or todo.lower() in existing_todo.lower():
                found = True
                break

       if found:
        print("ALREADY ADDED")
       else:
        task.append(todo)

    elif choice == 2:
        a=input ("Enter the task to be removed from tasks: ")
        if a in task:
            task.remove (a)
            print ("Task marked as complete!! ")
        else:
            print ("Task not found in the list!")
    elif choice == 3:
        print ("Task list: ")
        for item in task:
            print (item)
    elif choice == 4:
        with open('tasks.txt', 'w') as file:
            for t in task:
                file.write(t + "\n")
            print("To do list saved")
    else:
        print ("Please give a valid input")
        break
