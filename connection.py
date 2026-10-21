from dotenv import load_dotenv
import asyncpg
import os


load_dotenv()

pasw = os.getenv("PASWORD_DB")


async def connection_db():
    try:
        conn = await asyncpg.connect(
            port=5432,
            host="localhost",
            user="postgres",
            database="task_d",
            password=pasw
        )
        print("Connection successful")
        return conn
    except Exception as Error:
        print(f"Connection Error: {Error}")


async def create_table():
    try:
        conn = await connection_db()
        await conn.execute("""
            Create table if not exists task(
                task_id serial primary key,
                user_id int references users(user_id),
                title varchar(200),
                description text,
                due_date varchar(50),
                status boolean default false,
                created_at timestamp default now(),
                is_active boolean default true
            )
        """)

        print("Created table successful")
        return conn
    except Exception as Error:
        print(f"Create table Error: {Error}")
    finally:
        await conn.close()