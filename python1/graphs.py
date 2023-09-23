#pie chart
import matplotlib.pyplot as plt
semesters=[1,2,3,4,5,6,7,8]
cgpa=[7.8,8.2,8,7.6,8,7.9,7.6,8]
plt.figure(figsize=(8, 5))
plt.pie(cgpa,labels=semesters, autopct='%1.1f%%')
plt.title("variation of cgpa with semesters")
plt.legend(["cgpa"], loc="upper right")
