
from connection import *
from service import *
from register import *
import asyncio


async def main():
    await create_table()

    while True:
        n = int(input("\n1)Registration\n2)Login\n0)Exit\nChoose one: "))

        match n:
            case 1:
                username = input("Enter username: ")
                password = input("Enter password: ")
                await register_user(username, password)
            case 2:
                username = input("Enter username: ")
                password = input("Enter password: ")
                user_id = await login_user(username, password)
                if user_id:
                    print(f"\nWelcome, {username}!")
                    while True:
                        n = int(input("1)Create task\n2)Get task\n3)Update task\n4)Delete task\n5)log out\n0) Exit\nChoose one: "))
                        match n:
                            case 1:
                                await create_task(input("Title: "), input("Description: "), input("Duration date: "))
                            case 2:
                                await get_task()
                            case 3:
                                task_id = int(input("Enter task ID: "))
                                title = input("Enter new title: ")
                                description = input("Enter new description: ")
                                due_date = input("Enter New duration date: ")
                                await update_task(task_id, title, description, due_date)
                                
                            case 4:
                                task_id = int(input("Enter task ID to delete: "))
                                await delete_task(task_id)
                            case 5:
                                print("Logged out successfully!")
                                break
                            case 0:
                                print("Goodbye!")
                                break
                            case _:
                                print("Invalid Input")

                else:
                    print("Login failed")

            case 0:
                print("Goodbye!")
                break

            case _:
                print("Invalid Input")


if __name__ == "__main__":
    asyncio.run(main())