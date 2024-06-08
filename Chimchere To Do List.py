import tkinter as tk
from datetime import datetime, timedelta

class Task:
    def __init__(self, name, start_time, end_time, status="Pending", remarks=""):
        self.name = name
        self.start_time = start_time
        self.end_time = end_time
        self.status = status
        self.remarks = remarks

    def duration(self):
        return self.end_time - self.start_time

class ToDoApp:
    def __init__(self, master):
        self.master = master
        self.tasks = []
        
        # Create labels and entry boxes for input
        self.name_label = tk.Label(master, text="Task Name:")
        self.name_label.grid(row=0, column=0)
        self.name_entry = tk.Entry(master)
        self.name_entry.grid(row=0, column=1)

        self.start_time_label = tk.Label(master, text="Start Time (YYYY-MM-DD HH:MM:SS):")
        self.start_time_label.grid(row=1, column=0)
        self.start_time_entry = tk.Entry(master)
        self.start_time_entry.grid(row=1, column=1)

        self.end_time_label = tk.Label(master, text="End Time (YYYY-MM-DD HH:MM:SS):")
        self.end_time_label.grid(row=2, column=0)
        self.end_time_entry = tk.Entry(master)
        self.end_time_entry.grid(row=2, column=1)

        self.add_button = tk.Button(master, text="Add Task", command=self.add_task_gui,bg="blue")
        self.add_button.grid(row=3, column=0, columnspan=2)

        self.serial_number_label = tk.Label(master, text="Serial Number:", bg="aquamarine")
        self.serial_number_label.grid(row=4, column=0)
        self.serial_number_entry = tk.Entry(master)
        self.serial_number_entry.grid(row=4, column=1)

        self.update_button = tk.Button(master, text="Update Task", command=self.update_task_gui,bg="brown")
        self.update_button.grid(row=5, column=0, columnspan=2)

        self.delete_button = tk.Button(master, text="Delete Task", command=self.delete_task_gui,bg="red")
        self.delete_button.grid(row=6, column=0, columnspan=2)

        self.message_label = tk.Label(master, text="")
        self.message_label.grid(row=7, column=0, columnspan=2)

        # Create a Listbox to display tasks
        self.task_list = tk.Listbox(master)
        self.task_list.grid(row=8, column=0, columnspan=2, sticky="nsew")
        
        # Make the listbox expandable
        master.grid_rowconfigure(8, weight=1)
        master.grid_columnconfigure(1, weight=1)

        self.update_task_colors()  # Start the task color update loop

    def add_task_gui(self):
        try:
            name = self.name_entry.get()
            start_time = datetime.strptime(self.start_time_entry.get(), "%Y-%m-%d %H:%M:%S")
            end_time = datetime.strptime(self.end_time_entry.get(), "%Y-%m-%d %H:%M:%S")
            self.add_task(name, start_time, end_time)
            self.name_entry.delete(0, tk.END)
            self.start_time_entry.delete(0, tk.END)
            self.end_time_entry.delete(0, tk.END)
        except ValueError:
            self.show_message("Invalid date format. Please use YYYY-MM-DD HH:MM:SS")

    def add_task(self, name, start_time, end_time):
        task = Task(name, start_time, end_time)
        self.tasks.append(task)
        self.update_task_list()

    def update_task_gui(self):
        try:
            serial_number = int(self.serial_number_entry.get()) - 1
            name = self.name_entry.get()
            start_time = datetime.strptime(self.start_time_entry.get(), "%Y-%m-%d %H:%M:%S")
            end_time = datetime.strptime(self.end_time_entry.get(), "%Y-%m-%d %H:%M:%S")
            self.update_task(serial_number, name, start_time, end_time)
            self.serial_number_entry.delete(0, tk.END)
            self.name_entry.delete(0, tk.END)
            self.start_time_entry.delete(0, tk.END)
            self.end_time_entry.delete(0, tk.END)
        except ValueError:
            self.show_message("Invalid input. Please enter valid data.")

    def update_task(self, serial_number, new_name, new_start_time, new_end_time):
        if 0 <= serial_number < len(self.tasks):
            now = datetime.now()
            task = self.tasks[serial_number]
            if now < task.end_time:
                task.name = new_name
                task.start_time = new_start_time
                task.end_time = new_end_time
                self.update_task_list()
            else:
                self.show_message("End time has passed. Cannot update task.")
        else:
            self.show_message("Task with serial number {} not found.".format(serial_number + 1))

    def delete_task_gui(self):
        try:
            serial_number = int(self.serial_number_entry.get()) - 1
            self.delete_task(serial_number)
            self.serial_number_entry.delete(0, tk.END)
        except ValueError:
            self.show_message("Invalid input. Please enter a valid serial number.")

    def delete_task(self, serial_number):
        if 0 <= serial_number < len(self.tasks):
            del self.tasks[serial_number]
            self.update_task_list()
        else:
            self.show_message("Task with serial number {} not found.".format(serial_number + 1))

    def update_task_list(self):
        self.task_list.delete(0, tk.END)
        for i, task in enumerate(self.tasks):
            self.task_list.insert(tk.END, "{}. {} ({} - {})".format(i + 1, task.name, task.start_time, task.end_time))
        self.update_task_colors()

    def show_message(self, message):
        self.message_label.config(text=message)
        self.master.after(5000, lambda: self.message_label.config(text=""))  # Clear message after 5 seconds

    def update_task_colors(self):
        now = datetime.now()
        for i, task in enumerate(self.tasks):
            time_remaining = task.start_time - now
            if task.status == "Pending":
                if time_remaining <= timedelta(minutes=10):
                    self.task_list.itemconfig(i, {'bg':'orange'})
                elif time_remaining <= timedelta(0):
                    self.task_list.itemconfig(i, {'bg':'red'})
                else:
                    self.task_list.itemconfig(i, {'bg':'gray'})
            elif task.status == "Completed":
                self.task_list.itemconfig(i, {'bg':'green'})
            elif task.status == "Postponed":
                self.task_list.itemconfig(i, {'bg':'yellow'})
            else:
                self.task_list.itemconfig(i, {'bg':'brown'})

        self.master.after(60000, self.update_task_colors)  # Call again after 1 minute (60000 milliseconds)

def main():
    root = tk.Tk()
    root.title("Chimchere To Do List")
    app = ToDoApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
