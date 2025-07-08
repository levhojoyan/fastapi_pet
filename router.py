from typing import Annotated
from fastapi import APIRouter, Depends
from schemas import STask, STaskAdd, STaskId
from repository import TaskRepository

tasks = []

router = APIRouter(prefix="/tasks", tags=["tasks"])


@router.post("")
async def add_task(task: Annotated[STaskAdd, Depends()]) -> STaskId:

    task_id = await TaskRepository.add_one(task)

    return {"ok": True, "task_id": task_id}


@router.get("")
async def get_tasks() -> list[STask]:
    tasks = await TaskRepository.find_all()
    print("kek", tasks)

    return tasks
