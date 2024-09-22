task = input("Enter the task description: ")
priority = input("Enter the task's priority (high, medium, low): ")
time_bound = input("Is the task time-bound (yes or no): ")

match priority:
    case "high":
        reminder = "Urgent task: " + task
        if time_bound == "yes":
            reminder += " that requires immediate attention today!"
    case "medium":
        reminder = "Important task: " + task
        if time_bound == "yes":
            reminder += " should be addressed soon."
    case "low":
        reminder = "Task: " + task
        if time_bound == "yes":
            reminder += " can be completed at your convenience."
    case _:
        reminder = "Invalid priority."

print(reminder)