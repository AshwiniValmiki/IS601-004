from datetime import datetime
import json
import os

tasks = []
# constant, don't edit, use .copy()
TASK_TEMPLATE = {
    "name":"",
    "due": None, # datetime
    "lastActivity": None, # datetime
    "description": "",
    "done": False # False if not done, datetime otherise
}

# don't edit, intentionaly left an unhandled exception possibility
def str_to_datetime(datetime_str):
    """ attempts to convert a string in one of two formats to a datetime
    Valid formats (visual representation): mm/dd/yy hh:mm:ss or yyyy-mm-dd hh:mm:ss """
    try:
        return datetime.strptime(datetime_str, '%m/%d/%y %H:%M:%S')
    except:
        return datetime.strptime(datetime_str, '%Y-%m-%d %H:%M:%S')

def save():
    """ writes the tasks list to a json file to persist changes """
    f = open("tracker.json", "w")
    f.write(json.dumps(tasks, indent=4, default=str))
    f.close()

def load():
    """ loads the task list from a json file """
    if not os.path.isfile("tracker.json"):
        return
    f = open("tracker.json", "r")
    
    data = json.load(f)
    # Note about global keyword: https://stackoverflow.com/a/11867510
    global tasks
    tasks = data
    f.close()
    print(f"data {data}")    

def list_tasks(_tasks):
    """ List a summary view of all tasks """
    i = 0
    for t in _tasks:
        print(f"{i+1}) [{'x' if t['done'] else ' '}] Task: {t['name']} (Due: {t['due']})")
        i += 1
    if len(_tasks) == 0:
        print("No tasks to show")

# edits should happen below this line

def add_task(name: str, description: str, due: str):
    """ Copies the TASK_TEMPLATE and fills in the passed in data then adds the task to the tasks list """
    task = TASK_TEMPLATE.copy() # don't delete this
    # update lastActivity with the current datetime value
    # set the name, description, and due date (all must be provided)
    # due date must match one of the formats mentioned in str_to_datetime()
    # add the new task to the tasks list
    # output a message confirming the new task was added or if the addition was rejected due to missing data
    # make sure save() is still called last in this function
    # include your ucid and date as a comment of when you implemented this, briefly summarize the solution
    if(name =="" or description =="" or due =="" ):
        if(name ==""):
            print(f"addition was rejected due missing : name")
        if(description ==""):
            print(f"addition was rejected due missing : description")
        if(due ==""):
            print(f"addition was rejected due missing : duedate")
    else:
        task["name"]= name
        task["description"]= description
        task["due"]=str_to_datetime(due)
        task["lastActivity"]=datetime.now()
        tasks.append(task)
        print(f"Congrats. The new task was added!")
    #Ucid: av659 
    #date: 2/18/23
    #Summary: Firstly, Here the checking of tasks was done . Task will be  rejected if eitehr of the data is missing. 
    # When all the data of name, description and duedate is given, then the task was sucessfully added.
    save()

def process_update(index):
    """ extracted the user input prompts to get task data then passes it to update_task() """
    # get the task by index
    # consider index out of bounds scenarios and include appropriate message(s) for invalid index
    # show the existing value of each property where the TODOs are marked in the text of the inputs (replace the TODO related text)
    # include your ucid and date as a comment of when you implemented this, briefly summarize the solution
    if index in range(0,len(tasks)):
        name = input(f"What's the name of this task? "+tasks[index]["name"]+" \n").strip()
        desc = input(f"What's a brief descriptions of this task?"+tasks[index]["description"] +"\n").strip()
        due = input(f"When is this task due (format: m/d/y H:M:S)"+ str(tasks[index]["due"])+" \n").strip()
        update_task(index, name=name, description=desc, due=due)
    else:
        print(f"Index value invalid. Out of bounds. Index doesn't exist in the  taskList")

    #Ucid: av659 
    #date: 2/18/23
    #Summary: Here, checked if the index value is correctly given, or else the index is out of bounds 

   

def update_task(index: int, name: str, description:str, due: str):
    """ Updates the name, description , due date of a task found by index if an update to the property was provided """
    # find the task by index
    # consider index out of bounds scenarios and include appropriate message(s) for invalid index
    # update incoming task data if it's provided (if it's not provided use the original task property value)
    # update lastActivity with the current datetime value
    # output that the task was updated if any items were changed, otherwise mention task was not updated
    # make sure save() is still called last in this function
    # include your ucid and date as a comment of when you implemented this, briefly summarize the solution
    if index in range(0,len(tasks)):
        flag = 0
        if(name !=""):
            flag = 1
            tasks[index]["name"] = name
        if(description !="" ):
            flag = 1
            tasks[index]["description"] = description
        if(due != ""):
            flag = 1
            tasks[index]["due"]=str_to_datetime(due)
        if(flag == 0):
            print(f"Sorry. The task was not updated")
        else:
            print(f"Congrats. The task was updated!")
        tasks[index]["lastActivity"]=datetime.now()
    else:
        print(f"Index value invalid. Out of bounds. Index does not exist in the TaskList")
    save()
     #Ucid: av659 
    #date: 2/19/23
    #Summary: Here, checked if the index value is correctly given, or else the index is out of bounds . 
    #And through the index I have updated the task.


def mark_done(index):
    """ Updates a single task, via index, to a done datetime"""
    # find task from list by index
    # consider index out of bounds scenarios and include appropriate message(s) for invalid index
    # if it's not done, record the current datetime as the value
    # if it is done, print a message saying it's already completed
    # make sure save() is still called last in this function
    # include your ucid and date as a comment of when you implemented this, briefly summarize the solution
    if index in range(0,len(tasks)):
        if(not tasks[index]["done"]):
            tasks[index]["done"]=datetime.now()
            print(f"Task is being marked as complete")
        else:
            print(f"It has already completed")
    else:
        print(f"Index value invalid. Out of bounds. Index does not exist in the TaskList")

    save()
    #Ucid: av659 
    #date: 2/19/23
    #Summary: Here, checked if the index value is correctly given, or else the index is out of bounds . 
    #And when index is correctly given the task is being marked as complete else it has already completed .



def view_task(index):
    """ View more info about a specific task fetch by index """
    # find task from list by index
    # consider index out of bounds scenarios and include appropriate message(s) for invalid index
    # utilize the given print statement when a task is found
    # include your ucid and date as a comment of when you implemented this, briefly summarize the solution
    task = {}
    if index in range(0,len(tasks)):
        task= tasks[index]
        print(f"""[{'x' if task['done'] else ' '}] Task: {task['name']}\n Description: {task['description']} \n 
        Last Activity: {task['lastActivity']} \n
        Due: {task['due']}\n
        Completed: {task['done'] if task['done'] else '-'} \n
        """.replace('  ', ' '))
    else:
        print(f"Index value invalid. Out of bounds. Index does not exist in the TaskList")
    #Ucid: av659 
    #date: 2/19/23
    #Summary: Here, checked if the index value is correctly given, or else the index is out of bounds . 
    #And when index is correctly given the task can be viewed with their respective parameters like name, desc, and due.


def delete_task(index):
    """ deletes a task from the tasks list by index """
    # delete/remove task from list by index
    # message should show if it was successful or not
    # consider index out of bounds scenarios and include appropriate message(s) for invalid index
    # make sure save() is still called last in this function
    # include your ucid and date as a comment of when you implemented this, briefly summarize the solution
    if index in range(0,len(tasks)):
        tasks.remove(tasks[index])
        print(f"The Task was succesfully deleted.")
    else:
        print(f" Index value invalid. Out of bounds. Index does not exist in the TaskList Deletion was not successful.")
    save()
    #Ucid: av659 
    #date: 2/20/23
    #Summary: Here, checked if the index value is correctly given, or else the index is out of bounds . 
    #And when index is correctly given the respective task can be deleted.


def get_incomplete_tasks():
    """ prints a list of tasks that are not done """
    # generate a list of tasks where the task is not done
    # pass that list into list_tasks()
    # include your ucid and date as a comment of when you implemented this, briefly summarize the solution
    _tasks = []
    flag=0
    for t in tasks:
        if not t["done"]:
            flag=1
            _tasks.append(t)
    if(flag==0):
        print(f"There are no incomplete tasks available")
    list_tasks(_tasks)
    #Ucid: av659 
    #date: 2/20/23
    #Summary: Here, a for loop has been initiated to check the list of tasks that are not done. 
    #else it is being showed that the there are mno incomplete tasks. Then finaaly passing them into __tasks.

def get_overdue_tasks():
    """ prints a list of tasks that are over due completion (not done and expired) """
    # generate a list of tasks where the due date is older than now and that are not complete
    # pass that list into list_tasks()
    # include your ucid and date as a comment of when you implemented this, briefly summarize the solution
    _tasks = []
    for t in tasks:
        if datetime.strptime(str(t["due"]),'%Y-%m-%d %H:%M:%S')<datetime.now() and not t["done"]:
            _tasks.append(t)
    list_tasks(_tasks)
    #Ucid: av659 
    #date: 2/20/23
    #Summary: Here, a for loop has been initiated to check the list of tasks that are not done infact Overdue .
    #Then finally passing them into __tasks.

def get_time_remaining(index):
    """ outputs the number of days, hours, minutes, seconds a task has before it's overdue otherwise shows similar info for how far past due it is """
    # get the task by index
    # consider index out of bounds scenarios and include appropriate message(s) for invalid index
    # get the days, hours, minutes, seconds between the due date and now
    # display the remaining time via print in a clear format showing days, hours, minutes, seconds
    # if the due date is in the past print out how many days, hours, minutes, seconds the task is over due (clearly note that it's over due, values should be positive)
    # include your ucid and date as a comment of when you implemented this, briefly summarize the solution
    task = {}
    if index in range(0,len(tasks)):
        if not tasks[index]["done"]:
            if datetime.strptime(tasks[index]["due"],'%Y-%m-%d %H:%M:%S')>datetime.now():
                remaining_time = datetime.strptime(tasks[index]["due"],'%Y-%m-%d %H:%M:%S')-datetime.now()
                days,hours,minutes,seconds= remaining_time.days,remaining_time.seconds//3600, (remaining_time.seconds//60)%60,remaining_time.seconds%60
                print(f"The time remaining to complete this task is ",days,"days ",hours,"Hours ",minutes,"Minutes ",seconds,"seconds ")
            else:
                overdue_time= datetime.now()-datetime.strptime(tasks[index]["due"],'%Y-%m-%d %H:%M:%S')
                o_days,o_hours,o_minutes,o_seconds= overdue_time.days,overdue_time.seconds//3600, (overdue_time.seconds//60)%60,overdue_time.seconds%60
                print(f"The due date is Overdue by ",o_days,"days ",o_hours,"Hours ",o_minutes,"Minutes ",o_seconds,"seconds ")
        else:
            print(f"Whoo.The task was already completed")
    else:
        print(f"Index value invalid. Out of bounds. Index does not exist in the TaskList")
    #Ucid: av659 
    #date: 2/20/23
    #Summaruy : Firstly checked the index. If true then the time remaining for the task to be complete has been printed else,
    #The due date is overdue by is printed. 

# no changes needed below this line

command_list = ["add", "view", "update", "list", "incomplete", "overdue", "delete", "remaining", "help", "quit", "exit", "done"]
def print_options():
    """ prints a readable list of commands that can be typed when prompted """
    print("Choices")
    print("add - Creates a task")
    print("update - updates a specific task")
    print("view - see more info about a task by number")
    print("list - lists tasks")
    print("incomplete - lists incomplete tasks")
    print("overdue - lists overdue tasks")
    print("delete - deletes a task by number")
    print("remaining - gets the remaining time of a task by number")
    print("done - marks a task complete by number")
    print("quit or exit - terminates the program")
    print("help - shows this list again")

def run():
    """ runs the program until terminated or a quit/exit command is used """
    print("Welcome to Task Tracker!")
    load()
    print_options()
    while(True):
        opt = input("What would you like to do?\n").strip() # strip removes whitespace from beginning/end
        if opt not in command_list:
            print("That's not a valid option")
        elif opt == "add":
            name = input("What's the name of this task?\n").strip()
            desc = input("What's a brief descriptions of this task?\n").strip()
            due = input("When is this task due (visual format: mm/dd/yy hh:mm:ss)\n").strip()
            add_task(name, desc, due)
        elif opt == "view":
            num = int(input("Which task do you want to view? (hint: number from 'list') ").strip())
            index = num-1
            view_task(index)
        elif opt == "update":
            num = int(input("Which task do you want to update? (hint: number from 'list') ").strip())
            index = num-1
            process_update(index)
        elif opt == "done":
            num = int(input("Which task do you want to complete? (hint: number from 'list') ").strip())
            index = num-1
            mark_done(index)
        elif opt == "list":
            list_tasks(tasks)
        elif opt == "incomplete":
            get_incomplete_tasks()
        elif opt == "overdue":
            get_overdue_tasks()
        elif opt == "delete":
            num = int(input("Which task do you want to delete? (hint: number from 'list') ").strip())
            index = num-1
            delete_task(index)
        elif opt == "remaining":
            num = int(input("Which task do you like to get the duration for? (hint: number from 'list') ").strip())
            index = num-1
            get_time_remaining(index)
        elif opt in ["quit", "exit"]:
            print("Good bye.")
            quit()
        elif opt == "help":
            print_options()
        
if __name__ == "__main__":
    run()