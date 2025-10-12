days = int(input("Enter the number of days: "))
hours = int(input("Enter the number of hours: "))

print("please select a choice:")
print("1. Convert to seconds")
print("2. Convert to minutes")
choice = int(input("Enter your choice (1 or 2): "))
print("--------------------------")
if choice == 1:
    total_seconds = ( days * 24 *3600) + ( hours * 3600)
    print(f"Total seconds: {total_seconds}")

elif choice == 2:
    total_minutes = ( days * 24 * 60) + ( hours * 60)
    print(f"Total minutes: {total_minutes}")