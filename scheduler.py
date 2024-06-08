from task import Task

class Scheduler:
    TICK = 100
    SCH_MAX_TASKS = 40
    SCH_tasks_G = []
    current_index_task = 0

    def __int__(self):
        return

    def SCH_Init(self):
        self.current_index_task = 0

    def SCH_Add_Task(self, pFunction, DELAY, PERIOD):
        if self.current_index_task < self.SCH_MAX_TASKS:
            aTask = Task(pFunction, DELAY / self.TICK, PERIOD / self.TICK)
            aTask.TaskID = self.current_index_task
            self.SCH_tasks_G.append(aTask)
            self.current_index_task += 1
        else:
            print("PrivateTasks are full!!!")

    def SCH_Update(self):
        for i in range(0, len(self.SCH_tasks_G)):
            if self.SCH_tasks_G[i].Delay > 0:
                self.SCH_tasks_G[i].Delay -= 1
            else:
                self.SCH_tasks_G[i].Delay = self.SCH_tasks_G[i].Period
                self.SCH_tasks_G[i].RunMe += 1

    def SCH_Dispatch_Tasks(self):
        for i in range(0, len(self.SCH_tasks_G)):
            if self.SCH_tasks_G[i].RunMe > 0:
                self.SCH_tasks_G[i].RunMe -= 1
                self.SCH_tasks_G[i].pTask()

    def SCH_Delete(self, aTask):
        return

    def SCH_GenerateID(self):
        return -1
    
# for testing
import time
import PrivateTasks.private_task_1
import PrivateTasks.private_task_2

queue = Scheduler()
queue.SCH_Init()
task1 = PrivateTasks.private_task_1.Task1()
task2 = PrivateTasks.private_task_2.Task2()
queue.SCH_Add_Task(task1.Task1_Run, 100,200)
queue.SCH_Add_Task(task2.Task2_Run, 100,400)

cnt = 0
print(queue)
while True:
    print("--------------------")
    print("#", cnt)
    queue.SCH_Update()
    queue.SCH_Dispatch_Tasks()
    time.sleep(0.1)
    cnt += 1
    if cnt == 10:
        queue.SCH_Delete(task1)