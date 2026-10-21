from connection import *
from register import *
async def create_task(title, descp, due_date):
    try:
        conn = await connection_db()
        await conn.execute("""
            INSERT INTO task(title, description, due_date) VALUES
            ($1, $2, $3)
        """, title, descp, due_date)

        print("Created task successful")
    except Exception as Error:
        print(f"Create task Error: {Error}")
    finally:
        await conn.close()


async def get_task():
    try:
        conn = await connection_db()
        tasks = await conn.fetch("""
            select * from task
        """)

        for task in tasks:
            print(f"""

Task Id: {task["task_id"]}
Title: {task["title"]}
User_id {task["user_id"]}
Description: {task["description"]}
Duration date: {task["due_date"]}
Status: {task["status"]}
Created at: {task["created_at"]}

            """)

        return tasks
    except Exception as Error:
        print(f"Get task Error: {Error}")
    finally:
        await conn.close()
        
        
async def update_task(task_id,title,description,due_date):
    try:
        conn = await connection_db()
        await conn.execute(
            """
            UPDATE task
            SET title = $1,
            description = $2,
            due_date = $3
            WHERE task_id = $4
            """,
            title, description, due_date, task_id
            )
        print("Task updated succesfully!")

    except Exception as error:
        print(f"Update task error: {error}")
    finally:
            await conn.close()
            
            
            
async def delete_task(task_id):
    try:
        conn = await connection_db()
        await conn.execute("""
            DELETE FROM task
            WHERE task_id = $1
        """, task_id)
        print("Task deleted successfully!")

    except Exception as error:
        print(f"Delete task error: {error}")

    finally:
            await conn.close()