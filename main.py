from connection import get_connection


def add_task(title, description):
    """Add a new task to the database"""
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "INSERT INTO tasks (task_name, description) VALUES (%s, %s)",
                (title, description)
            )
        conn.commit()
    print("✅ Task added!")


def delete_task(task_name):
    """Delete a task by its name"""
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "DELETE FROM tasks WHERE task_name = %s",
                (task_name,)
            )
        conn.commit()
    print("🗑️ Task deleted!")


def list_tasks():
    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT id, task_name, description, status FROM tasks ORDER BY id")
                rows = cur.fetchall()
                for r in rows:
                    print(r)
    except Exception as e:
        print("❌ Error while listing tasks:", e)


def list_tasks():    
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT id, task_name, description, status FROM tasks ORDER BY id")
            rows = cur.fetchall()
            for r in rows:
                print(f"{r[0]}. {r[1]} | {r[2]} | {r[3]}")


def main():
    """Main program loop"""
    while True:
        print("\n=== TO-DO MANAGER ===")
        print("1. Add task")
        print("2. Delete task")
        print("3. List tasks")
        print("4. Update task status")
        print("5. Exit")

        choice = input("Select an action: ").strip()

        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            add_task(title, description)

        elif choice == "2":
            task_name = input("Enter the name of the task to delete: ")
            delete_task(task_name)

        elif choice == "3":
            list_tasks()
            input("\nPress Enter to return to menu...")

        elif choice == "4":
            task_name = input("Enter task name to update: ")
            status = input("Enter new status (pending/done/in progress): ")
            

        elif choice == "5":
            print("👋 Exiting...")
            break

        else:
            print("❌ Wrong choice, try again.")


if __name__ == "__main__":
    main()
