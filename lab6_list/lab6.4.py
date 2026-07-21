#ITS100 Lecture6 Lists Lab6.4
namelist = ["mimi", "mumu", "mama"]
for i in range(3):
    print("student list:",namelist)
    delete = input("Please enter a student's name that you want to delete (q = exit)")
    if delete == 'q':
        break
    elif delete == "mimi" or delete == "mumu"or delete == "mama":
        confirm = input("you will remove ' %s ' from this class."%delete)
        if confirm == "yes":
            namelist.remove("%s"%delete)
