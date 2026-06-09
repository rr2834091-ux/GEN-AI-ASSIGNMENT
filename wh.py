print("GRADE OF STUDENTS USING WHILE LOOP")
print("----------------------------------")

subjects = ["Tamil", "English", "Maths", "Science", "Social Science"]
i = 0
while i < len(subjects):
    mark = int(input(f"Enter the {subjects[i]} mark: "))
    if 91<= mark <=100:
        print(mark, "S grade")
    elif 81<= mark <=90:
        print(mark, "A grade")
    elif 71<= mark <=80:
        print(mark, "B grade")
    elif 61<= mark <=70:
        print(mark, "C grade")
    elif 51<= mark <=60:
        print(mark, "D grade")
    elif mark == 50:
        print(mark, "E grade")
    elif 0<= mark <50:
        print(mark, "Fail")
    else:
        print("Invalid mark")

    i += 1
