#pie chart
import matplotlib.pyplot as plt
semesters=[1,2,3,4,5,6,7,8]
cgpa=[7.8,8.2,8,7.6,8,7.9,7.6,8]
plt.figure(figsize=(8, 5))
plt.pie(cgpa,labels=semesters, autopct='%1.1f%%')
plt.title("variation of cgpa with semesters")
plt.legend(["cgpa"], loc="upper right")

import matplotlib.pyplot as plt

# Dataset
game_number = list(range(1, 21))
points_scored = [3, 1, 2, 3, 1, 3, 2, 3, 1, 2, 3, 1, 3, 2, 3, 1, 2, 3, 1, 2]
goals_scored = [2, 0, 2, 3, 1, 2, 1, 2, 0, 1, 3, 1, 2, 1, 2, 0, 1, 3, 1, 2]
opponent_goals = [1, 2, 2, 1, 1, 0, 2, 1, 1, 2, 2, 1, 0, 1, 2, 1, 2, 1, 1, 2]

# Line Chart
plt.figure(figsize=(8, 5))
plt.plot(game_number, points_scored, label='Points Scored', marker='o', linestyle='-')
plt.xlabel('Game Number')
plt.ylabel('Points Scored')
plt.title("Team's Points Over the Season")
plt.legend()
plt.grid(True)
plt.show()

# Scatter Plot
plt.figure(figsize=(8, 5))
plt.scatter(goals_scored, opponent_goals, label='Game Data', color='b', marker='o')
plt.xlabel('Goals Scored')
plt.ylabel('Opponent Goals')
plt.title("Team's Goals vs. Opponent Goals")
plt.legend()
plt.grid(True)
plt.show()

# Bar Chart
months = ['Month 1', 'Month 2', 'Month 3']
monthly_goals = [sum(goals_scored[:7]), sum(goals_scored[7:14]), sum(goals_scored[14:])]
plt.figure(figsize=(8, 5))
plt.bar(months, monthly_goals, color='g')
plt.xlabel('Month')
plt.ylabel('Total Goals Scored')
plt.title("Team's Monthly Goal Comparison")
plt.grid(axis='y')
plt.show()
