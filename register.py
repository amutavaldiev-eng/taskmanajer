from connection import *

async def register_user(username, password):
    conn = await connection_db()
    try:
        await conn.execute("""
            CREATE TABLE IF NOT EXISTS users (
                user_id serial primary key,
                username varchar(100) unique not null,
                password varchar(100) not null
            )""")
        users = await conn.fetch(
            "select username FROM users"
        )
        for user in users:
            if user["username"] == username:
                print("Username already exists!")
                await conn.close()
        await conn.execute("""
            INSERT INTO users (username, password) VALUES 
                ($1, $2)""",
                username, password)

        print("Registration successful!")
    except Exception as error:
        print(f"Error: {error}")
    finally:
        await conn.close()



async def login_user(username, password):
    conn = await connection_db()

    try:
        users = await conn.fetch(
            "select * FROM users"
        )
        for user in users:
            if user["username"] == username and user["password"] == password:
                print("Login successful!")
                return user["user_id"]
        print("Username or password is incorrect!")
        

    except Exception as error:
        print(f"Error: {error}")

    finally:
        await conn.close()