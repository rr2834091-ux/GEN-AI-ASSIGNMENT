import pandas as pd
import matplotlib.pyplot as plt
data={'Player Names':['Dhoni','KL Rahul','Sooriyavaibavanshi','Kholi','Rohit'],
      'Scores':[92,67,150,87,99],
      'Strike Rate':[230,121,258,189,165],
      'Ball':[40,55,58,46,60]}
df=pd.DataFrame(data)
print(df)
#Bar plot using pandas
plt.figure(figsize=(6,5))
plt.bar(df['Player Names'],df['Scores'])
plt.title('Player scores')
plt.xlabel('Player Names')
plt.ylabel('Scores')
plt.show()
print('-'*60)
#Line plot using pandas:
plt.figure(figsize=(6,5))
plt.bar(df['Player Names'],df['Strike Rate'])
plt.title('Players Strike Rate')
plt.xlabel('Player Names')
plt.ylabel('Strike Rate')
plt.show()
#Pie chart using pandas:
plt.figure(figsize=(6,6))
plt.pie(df["Scores"], labels=df["Player Names"], autopct="%1.1f%%")
plt.title("Scores Percentage")
plt.show()
#SCATTER GRAPH - Sales vs Profit
plt.figure(figsize=(7,4))
plt.scatter(df["Ball"], df["Strike Rate"])
plt.title("Ball vs Strike Rate")
plt.xlabel("Ball")
plt.ylabel("Strike Rate")
plt.show()

