#   50.	Write a program to convert total seconds into hours, minutes, and seconds using // and %.

total_seconds = int(input("Enter total seconds: "))

hours = total_seconds // 3600
remaining_seconds = total_seconds % 3600

minutes = remaining_seconds // 60
seconds = remaining_seconds % 60

print(f"{total_seconds} seconds = {hours} hours, {minutes} minutes, {seconds} seconds")
