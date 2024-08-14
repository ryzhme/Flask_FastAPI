"""
Необходимо создать API для управления списком задач. Каждая задача должна содержать заголовок и описание.
Для каждой задачи должна быть возможность указать статус (выполнена/не выполнена).

API должен содержать следующие конечные точки:
— GET /tasks — возвращает список всех задач.
— GET /tasks/{id} — возвращает задачу с указанным идентификатором.
— POST /tasks — добавляет новую задачу.
— PUT /tasks/{id} — обновляет задачу с указанным идентификатором.
— DELETE /tasks/{id} — удаляет задачу с указанным идентификатором.

Для каждой конечной точки необходимо проводить валидацию данных запроса и ответа.
Для этого использовать библиотеку Pydantic.
"""
import logging
from fastapi import FastAPI, HTTPException
from typing import Optional, Literal
from pydantic import BaseModel

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
app = FastAPI()


class Task(BaseModel):
    id: int
    name: str
    description: str
    state: Literal['выполнена', 'не выполнена']


class TaskAdd(BaseModel):
    name: str
    description: str
    state: Literal['выполнена', 'не выполнена']


class TaskUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    state: Optional[Literal['выполнена', 'не выполнена']] = None


g_seq_id = 0
g_tasks_list = []


def next_seq_id():
    global g_seq_id
    g_seq_id += 1
    return g_seq_id


def add(task: TaskAdd):
    g_tasks_list.append(Task(id=next_seq_id(), name=task.name, description=task.description, state=task.state))
    return


def delete(task_id: int):
    for index in range(len(g_tasks_list)):
        if g_tasks_list[index].id == task_id:
            del g_tasks_list[index]
            return
    raise HTTPException(status_code=404, detail='Task not found')


def get(task_id: int):
    for index in range(len(g_tasks_list)):
        if g_tasks_list[index].id == task_id:
            return g_tasks_list[index]
    raise HTTPException(status_code=404, detail='Task not found')


def update(task_id: int, task_data: TaskUpdate):
    for index in range(len(g_tasks_list)):
        if g_tasks_list[index].id == task_id:
            if task_data.name:
                g_tasks_list[index].name = task_data.name
            if task_data.description:
                g_tasks_list[index].description = task_data.description
            if task_data.state:
                g_tasks_list[index].state = task_data.state
            return
    raise HTTPException(status_code=404, detail='Task not found')


@app.get("/")
async def read_root():
    return {"descr": "API for DZ #5"}


@app.get("/tasks/", response_model=list[Task])
async def read_tasks():
    logger.info(f'Отработал GET запрос.')
    return g_tasks_list


@app.get("/tasks/{id}", response_model=Task)
async def read_task(id: int):
    logger.info(f'Отработал GET запрос для task id = {id}.')
    return get(id)


@app.post("/tasks/")
async def create_task(task: TaskAdd):
    logger.info('Отработал POST запрос.')
    return add(task)


@app.put("/tasks/{id}")
async def update_task(id: int, task: TaskUpdate):
    logger.info(f'Отработал PUT запрос для task id = {id}.')
    return update(id, task)


@app.delete("/tasks/{id}")
async def delete_task(id: int):
    logger.info(f'Отработал DELETE запрос для item id = {id}.')
    return delete(id)
