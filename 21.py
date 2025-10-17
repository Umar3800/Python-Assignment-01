#   21.	Write a program to find the average marks of 5 subjects and print total and percentage.

s1 = float(input("Enter marks of subject 1 :"))
s2 = float(input("Enter marks of subject 2 :"))
s3 = float(input("Enter marks of subject 3 :"))
s4 = float(input("Enter marks of subject 4 :"))
s5 = float(input("Enter marks of subject 5 :"))

print("Total Marks :",(s1+s2+s3+s4+s5),"Average Marks :",(s1+s2+s3+s4+s5/5),"Percentage :",(s1+s2+s3+s4+s5/500)*100,sep='\n')
