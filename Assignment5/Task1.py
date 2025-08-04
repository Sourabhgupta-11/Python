dic={"Saurabh":95,"Alice":85,"Sujata":77}

name=str(input("Enter the student's name:"))
getMarks=dic.get(name,"Student not found")
print(f"{name}'s marks: {getMarks}" if dic.get(name) else getMarks )