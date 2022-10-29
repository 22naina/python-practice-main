#Stock average of marks:
num_subjects=int(input("enter numbers of subjects:"))
math_marks=float(input("enter marks obtained:"))
chem_marks=float(input("enter marks obrained:"))
IT_marks=float(input("enter marks obtained:"))

#Sum of makrs in all subjects:
total=(math_marks+chem_marks+IT_marks)

#Average of sum of marks:
average=(total/num_subjects)

print(average)