from database import TaskOrm
from schemas import STask, STaskAdd

from database import new_session

from sqlalchemy import select


class TaskRepository:
    @classmethod
    async def add_one(cls, data: STaskAdd) -> int:
        async with new_session() as session:
            task_dict = data.model_dump()

            task = TaskOrm(**task_dict)
            session.add(task)

            await session.flush()
            await session.commit()

            return task.id

    @classmethod
    async def find_all(cls) -> list[TaskOrm]:
        async with new_session() as session:
            query = select(TaskOrm)
            result = await session.execute(query)
            task_models = result.scalars().all()

            task_schemas = [
                STask.model_validate(task_model) for task_model in task_models
            ]
            print(task_schemas)
            return task_schemas
