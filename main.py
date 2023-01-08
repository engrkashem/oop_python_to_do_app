from datetime import datetime
from uuid import uuid1


class Task():
    all_task_list = []

    def __init__(self) -> None:
        self.task_name = ''
        self.created_time = None
        self.updated_time = 'NA'
        self.completed_time = 'NA'
        self.task_done = False
        self.id = None

    def __repr__(self) -> str:
        return f'name: {self.task_name}, id:{self.id} ctime: {self.created_time}, comtime: {self.completed_time}\n'

    @staticmethod
    def get_instant_date_time():
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        return dt_string

    @staticmethod
    def get_id():
        id = uuid1()
        return id

    def add_a_task(self, name):
        self.task_name = name
        self.created_time = self.get_instant_date_time()
        self.id = self.get_id()
        self.all_task_list.append(self)

    def update_task(self, task_no, task_name):
        for i, task in enumerate(self.all_task_list):
            if (i == task_no):
                task.task_name = task_name
                instant_date_time = self.get_instant_date_time()
                task.updated_time = instant_date_time
        print(f'\nYour Task is Updated Successfully.\n')

    def complete_task(self, task_no):
        for i, task in enumerate(self.all_task_list):
            if (i == task_no):
                instant_date_time = self.get_instant_date_time()
                task.completed_time = instant_date_time
                task.task_done = True
        print(f'\nYour Task has been Completed Successfully.\n')

    @staticmethod
    def print(task):
        print(f'ID: {task.id}\nTask: {task.task_name}')
        print(f'Created Time: {task.created_time}')
        print(f'Updated Time: {task.updated_time}')
        print(f'Completed Time: {task.completed_time}')
        print(f'Task Completed: {task.task_done}\n')

    def show_all_task(self):
        print('\n*****************************************')
        for task in self.all_task_list:
            self.print(task)
        print('*****************************************')

    def show_incomplete_task(self):
        print()
        is_completed = True
        for task in self.all_task_list:
            if task.task_done == False:
                is_completed = False
                self.print(task)

        if is_completed:
            print('WOW!! All Tasks are Completed right now, Have a Relax.\n')

    def show_complete_task(self):
        print()
        is_completed = False
        for task in self.all_task_list:
            if task.task_done == True:
                is_completed = True
                self.print(task)

        if is_completed == False:
            print('Oops!! No Completed Task, All tasks are pending right now.\n')

    def update_a_task(self):
        print('\nSelect a Task to Update')
        for i, task in enumerate(self.all_task_list):
            if task.task_done == False:
                print(f'Task No- {i+1}')
                self.print(task)
        task_no = int(input('Enter task No. '))
        task_no -= 1
        task_name = input('Enter Task Name: ')
        self.update_task(task_no, task_name)

    def complete_a_task(self):
        print('\nSelect a Task to Complete')
        for i, task in enumerate(self.all_task_list):
            if task.task_done == False:
                print(f'Task No- {i+1}')
                self.print(task)
        task_no = int(input('Enter task No. '))
        task_no -= 1
        self.complete_task(task_no)


while True:
    print('1. Add New task')
    print('2. Show All Tasks')
    print('3. Show Incomplete Tasks')
    print('4. Show Complete Tasks')
    print('5. Update Tasks')
    print('6. Merk a Task Complete')
    inp = int(input('Enter Option: '))
    task = Task()
    if inp == 1:
        task_name = input('Enter Your Task: ')
        task.add_a_task(task_name)
    elif inp == 2:
        task.show_all_task()
    elif inp == 3:
        task.show_incomplete_task()
    elif inp == 4:
        task.show_complete_task()
    elif inp == 5:
        task.update_a_task()
    elif inp == 6:
        task.complete_a_task()
    else:
        print('\nInvalid Option.\n')
