#!/usr/bin/env python
# coding: utf-8

# In[3]:


# Import required libraries
# hardik pandya
import numpy as np
import pandas as pd
URL = "https://stats.espncricinfo.com/ci/engine/player/625371.html?class=3;template=results;type=batting;view=innings"
all_tables = pd.read_html(URL)
all_tables = all_tables[3]
all_tables.to_excel('Hardik.xlsx', index=False)

# virat kohli
URL = "https://stats.espncricinfo.com/ci/engine/player/253802.html?class=3;template=results;type=batting;view=innings"
all_tables = pd.read_html(URL)
all_tables = all_tables[3]
all_tables.to_excel('Kohli.xlsx', index=False)

#rohit sharma
URL = "https://stats.espncricinfo.com/ci/engine/player/34102.html?class=3;template=results;type=batting;view=innings"
all_tables = pd.read_html(URL)
all_tables = all_tables[3]
all_tables.to_excel('Rohit.xlsx', index=False)

#surya
URL = "https://stats.espncricinfo.com/ci/engine/player/446507.html?class=3;template=results;type=batting;view=innings"
all_tables = pd.read_html(URL)
all_tables = all_tables[3]
all_tables.to_excel('SKY.xlsx', index=False)

#shubhman gill
URL = "https://stats.espncricinfo.com/ci/engine/player/1070173.html?class=3;template=results;type=batting;view=innings"
all_tables = pd.read_html(URL)
all_tables = all_tables[3]
all_tables.to_excel('Gill.xlsx', index=False)

#ravindra jadeja
URL = "https://stats.espncricinfo.com/ci/engine/player/234675.html?class=3;template=results;type=batting;view=innings"
all_tables = pd.read_html(URL)
all_tables = all_tables[3]
all_tables.to_excel('Ravindra.xlsx', index=False)

#Shikhar dhawan
URL = "https://stats.espncricinfo.com/ci/engine/player/28235.html?class=3;template=results;type=batting;view=innings"
all_tables = pd.read_html(URL)
all_tables = all_tables[3]
all_tables.to_excel('Dhawan.xlsx', index=False)

# Kl rahul
URL = "https://stats.espncricinfo.com/ci/engine/player/422108.html?class=3;template=results;type=batting;view=innings"
all_tables = pd.read_html(URL)
all_tables = all_tables[3]
all_tables.to_excel('Rahul.xlsx', index=False)


# In[1]:


# Clean the data
def clean_data(df):
    df = df[~df['Runs'].str.contains('\DNB')]
    df.loc[df['Runs'].str.contains('\*'), 'Runs'] = df['Runs'].str.replace('\*', '')
    df = df.drop(['Unnamed: 9', 'Mins','Unnamed: 13','BF'], axis=1)
    df['Runs'] = df['Runs'].astype(int)
    return df

# Calculate player vs oppositon statistics

def Opposition_stats(df):
    Opposition = df.groupby(["Opposition"])["Runs"].agg([("Innings","count"), ("average","mean"), "max", "min",("Runs", "sum")]).reset_index()
    Opposition_stats.columns = ["Ground", "Innings", "average", "max", "min", "Runs"]
    Opposition.rename(columns={"mean": "average", "count": "Innings"}, inplace=True)
    Opposition["average"] = Opposition["average"].round(1)
    return Opposition

# Calculate player at ground statistics
def Ground_stats(df):
    Ground_stats = df.groupby(["Ground"])["Runs"].agg([("Innings","count"), ("average", "mean"), "max", "min",("Runs", "sum")]).reset_index()
    Ground_stats.columns = ["Ground", "Innings", "average", "max", "min", "Runs"]
    Ground_stats.rename(columns={"mean": "average", "count": "Innings"}, inplace=True)
    Ground_stats["average"] = Ground_stats["average"].round(1)
    return Ground_stats


# In[2]:


# Read player data from Excel files
kohli_df = pd.read_excel("Kohli.xlsx")
rohit_df = pd.read_excel("Rohit.xlsx")
rahul_df = pd.read_excel("Rahul.xlsx")
hardik_df = pd.read_excel("Hardik.xlsx")
dhawan_df = pd.read_excel("Dhawan.xlsx")
sky_df = pd.read_excel("SKY.xlsx")
gill_df = pd.read_excel("Gill.xlsx")
jaddu_df = pd.read_excel("Ravindra.xlsx")


# In[5]:


kohli_df = clean_data(kohli_df)
rohit_df = clean_data(rohit_df)
rahul_df = clean_data(rahul_df)
hardik_df = clean_data(hardik_df)
dhawan_df = clean_data(dhawan_df)
sky_df = clean_data(sky_df)
gill_df = clean_data(gill_df)
jaddu_df = clean_data(jaddu_df)


# In[6]:


kohli_ground = Ground_stats(kohli_df)
print(kohli_ground)

kohli_opposition = Opposition_stats(kohli_df)
print(kohli_opposition)
import matplotlib.pyplot as plt

# Create pie chart (opposition)
plt.pie(kohli_opposition["Runs"] , labels=kohli_opposition["Opposition"], autopct='%3.1f%%')
plt.title('RunsvsOpp')
plt.show()


# bar chart for ground stats
Y = kohli_ground["Runs"]
X = kohli_ground["Ground"]
plt.figure(figsize=(60,8))
plt.bar(X,Y)



# In[7]:


# Calculate the moving average of the runs scored in each innings over a window of 3 innings
window_size = 6
kohli_df['Moving Average'] = kohli_df['Runs'].rolling(window_size).mean()

# Calculate the overall average of the batsman
overall_average = kohli_df['Runs'].mean()

# Add a column for innings number
kohli_df['Innings_NO'] = range(1, len(kohli_df) + 1)

# Plot the moving average and overall average over time
plt.plot(kohli_df['Innings_NO'], kohli_df['Moving Average'], label='Moving Average')
plt.axhline(y=overall_average, linestyle='--', color='red', label='Overall Average')
plt.xlabel('Innings')
plt.ylabel('Runs')
plt.title('Kohli Form Analysis')
plt.legend()
plt.show()


# In[8]:


#rohit
rohit_ground = Ground_stats(rohit_df)
print(rohit_ground)

rohit_opposition = Opposition_stats(rohit_df)
print(rohit_opposition)
import matplotlib.pyplot as plt

# Create pie chart (opposition)
plt.pie(rohit_opposition["Runs"] , labels=rohit_opposition["Opposition"], autopct='%3.1f%%')
plt.title('RunsvsOpp')
plt.show()


# bar chart for ground stats
Y = rohit_ground["Runs"]
X = rohit_ground["Ground"]
plt.figure(figsize=(60,8))
plt.bar(X,Y)


# In[9]:


#rahul
rahul_ground = Ground_stats(rahul_df)
print(rahul_ground)

rahul_opposition = Opposition_stats(rahul_df)
print(rahul_opposition)
import matplotlib.pyplot as plt

# Create pie chart (opposition)
plt.pie(rahul_opposition["Runs"] , labels=rahul_opposition["Opposition"], autopct='%3.1f%%')
plt.title('RunsvsOpp')
plt.show()


# bar chart for ground stats
Y = rahul_ground["Runs"]
X = rahul_ground["Ground"]
plt.figure(figsize=(60,8))
plt.bar(X,Y)


# In[10]:


#sky
sky_ground = Ground_stats(sky_df)
print(sky_ground)

sky_opposition = Opposition_stats(sky_df)
print(sky_opposition)
import matplotlib.pyplot as plt

# Create pie chart (opposition)
plt.pie(sky_opposition["Runs"] , labels=sky_opposition["Opposition"], autopct='%3.1f%%')
plt.title('RunsvsOpp')
plt.show()


# bar chart for ground stats
Y = sky_ground["Runs"]
X = sky_ground["Ground"]
plt.figure(figsize=(60,8))
plt.bar(X,Y)


# In[11]:


dhawan_ground = Ground_stats(dhawan_df)
print(dhawan_ground)

dhawan_opposition = Opposition_stats(dhawan_df)
print(dhawan_opposition)
import matplotlib.pyplot as plt

# Create pie chart (opposition)
plt.pie(dhawan_opposition["Runs"] , labels=dhawan_opposition["Opposition"], autopct='%3.1f%%')
plt.title('RunsvsOpp')
plt.show()


# bar chart for ground stats
Y = dhawan_ground["Runs"]
X = dhawan_ground["Ground"]
plt.figure(figsize=(60,8))
plt.bar(X,Y)


# In[12]:


hardik_ground = Ground_stats(hardik_df)
print(hardik_ground)

hardik_opposition = Opposition_stats(hardik_df)
print(hardik_opposition)
import matplotlib.pyplot as plt

# Create pie chart (opposition)
plt.pie(hardik_opposition["Runs"] , labels=hardik_opposition["Opposition"], autopct='%3.1f%%')
plt.title('RunsvsOpp')
plt.show()


# bar chart for ground stats
Y = hardik_ground["Runs"]
X = hardik_ground["Ground"]
plt.figure(figsize=(60,8))
plt.bar(X,Y)


# In[13]:


# Calculate ground stats for Gill
gill_ground = Ground_stats(gill_df)
print(gill_ground)

# Calculate opposition stats for Gill
gill_opposition = Opposition_stats(gill_df)
print(gill_opposition)

# Create pie chart for opposition stats
plt.pie(gill_opposition["Runs"], labels=gill_opposition["Opposition"], autopct='%3.1f%%')
plt.title('Runs vs Opposition')
plt.show()

# Create bar chart for ground stats
Y = gill_ground["Runs"]
X = gill_ground["Ground"]
plt.figure(figsize=(60,8))
plt.bar(X,Y)
plt.title('Runs vs Ground')
plt.show()




# Calculate ground stats for jaddu
jaddu_ground = Ground_stats(jaddu_df)
print(jaddu_ground)

# Calculate opposition stats for Jaddu
jaddu_opposition = Opposition_stats(jaddu_df)
print(jaddu_opposition)

# Create pie chart for opposition stats
plt.pie(jaddu_opposition["Runs"], labels=jaddu_opposition["Opposition"], autopct='%3.1f%%')
plt.title('Runs vs Opposition')
plt.show()

# Create bar chart for ground stats
Y = jaddu_ground["Runs"]
X = jaddu_ground["Ground"]
plt.figure(figsize=(60,8))
plt.bar(X,Y)
plt.title('Runs vs Ground')
plt.show()


# In[4]:


import pandas as pd
import matplotlib.pyplot as plt

# Define a function to calculate opposition stats
def Opposition_stats(df):
    # Group the data by opposition team and calculate the total runs scored against each team
    opposition_stats_df = df.groupby('Opposition')['Runs'].sum().reset_index()
    # Sort the data by runs scored in descending order
    opposition_stats_df = opposition_stats_df.sort_values(by=['Runs'], ascending=False)
    # Return the opposition stats dataframe
    return opposition_stats_df

# Define a function to calculate ground stats
def Ground_stats(df):
    # Group the data by ground and calculate the total runs scored at each ground
    ground_stats_df = df.groupby('Ground')['Runs'].sum().reset_index()
    # Sort the data by runs scored in descending order
    ground_stats_df = ground_stats_df.sort_values(by=['Runs'], ascending=False)
    # Return the ground stats dataframe
    return ground_stats_df

# Define the available players and their dataframes
players = {'Kohli': kohli_df, 'Rohit': rohit_df, 'Rahul': rahul_df, 'Hardik': hardik_df, 'Dhawan': dhawan_df, 'Sky': sky_df, 'Gill': gill_df, 'Jaddu': jaddu_df}

def update_stats(player):
    # Get the player's dataframes
    player_df = players[players]
    player_ground = Ground_stats(player_df)
    player_opposition = Opposition_stats(player_df)  # Add this line

    # Clear the existing plots
    plt.clf()
    

player_df = players[players]       
player_opposition = Opposition_stats(player_df) 
player_ground = Ground_stats(player_df)
    
   # Plot the opposition stats as a pie chart
plt.subplot(1, 2, 1)
plt.figure(figsize=(10, 5))
plt.pie(player_opposition["Runs"], labels=player_opposition["Opposition"], autopct='%10.1f%%')
plt.title(f"{player} - Opposition Stats")
plt.show()
    
    
   # Plot the ground stats as a bar chart
plt.subplot(1, 2, 2)
plt.figure(figsize=(10, 5))
Y = player_ground["Runs"]
X = player_ground["Ground"]
plt.bar(X, Y)
plt.title(f"{player} - Ground Stats")
plt.xlabel('Ground')
plt.ylabel('Runs')
plt.show()

# Create subplots with 1 row and 2 columns
fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))

# Plot the opposition stats as a pie chart
ax1.pie(player_opposition["Runs"], labels=player_opposition["Opposition"], autopct='%10.1f%%')
ax1.set_title(f"{player} - Opposition Stats")

# Plot the ground stats as a bar chart
Y = player_ground["Runs"]
X = player_ground["Ground"]
ax2.bar(X, Y)
ax2.set_title(f"{player} - Ground Stats")
ax2.set_xlabel('Ground')
ax2.set_ylabel('Runs')

# Display the runs table next to the charts
table_data = player_opposition[["Opposition", "count", "mean", "max", "min"]].copy()
table_data.columns = ["Opposition", "Innings", "Average", "High Score", "Low Score"]
table_data.set_index("Opposition", inplace=True)
table = ax2.table(cellText=table_data.values, colLabels=table_data.columns, loc='right')
table.auto_set_font_size(False)
table.set_fontsize(8)
table.scale(1, 1.5)

# Show the plots
plt.show()



    
    

# Create the GUI window
root = tk.Tk()
root.title("Player Stats")

# Create a dropdown menu for player selection
var = tk.StringVar(root)
var.set(list(players.keys())[0])  # Default player is the first one
player_menu = tk.OptionMenu(root, var, *players.keys())
player_menu.pack()

# Create a button to update the player stats
update_button = tk.Button(root, text="Update Stats", command=lambda: update_stats(var.get()))
update_button.pack()

# Run the GUI main loop
root.mainloop()


# In[ ]:


import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

# Define function to display player stats against opposition
def show_opposition_stats():
    table.delete("1.0", "end")
    stats = df.groupby(["Opposition"])["Runs"].agg(["count", "mean", "max", "min"]).reset_index()
    table.insert("end", stats.to_string(index=False))

# Define function to display player stats at a venue
def show_venue_stats():
    table.delete("1.0", "end")
    stats = df.groupby(["Ground"])["Runs"].agg(["count", "mean", "max", "min"]).reset_index()
    table.insert("end", stats.to_string(index=False))
    
def go_back():
    player_select.pack(side="left")
    opposition_button.pack_forget()
    venue_button.pack_forget()
    back_button.pack_forget()
    table.delete("1.0", "end")
    table.insert("end", "show_opposition_stats():")

# Define the available players and their dataframes
players = {'Kohli': kohli_df, 'Rohit': rohit_df, 'Rahul': rahul_df, 'Hardik': hardik_df, 'Dhawan': dhawan_df, 'Sky': sky_df, 'Gill': gill_df, 'Jaddu': jaddu_df}

# Define a function to update the player stats and graphs based on the selected player
def update_stats(player):
    # Get the player's dataframes
    player_df = players[player]
    player_ground = Ground_stats(player_df)
    player_opposition = Opposition_stats(player_df)
    
    # Clear the existing plots
    plt.clf()
    
    # Plot the opposition stats as a pie chart
    plt.subplot(1, 2, 1)
    plt.pie(player_opposition["Runs"], labels=player_opposition["Opposition"], autopct='%10.1f%%')
    plt.title(f"{player} - Opposition Stats")
    plt.show()
    # Display opposition stats in table
    table.delete("1.0", "end")
    table.insert("end", player_opposition.to_string(index=False))
    
    # Plot the ground stats as a bar chart
    plt.subplot(1, 2, 2)
    Y = player_ground["Runs"]
    X = player_ground["Ground"]
    plt.bar(X, Y)
    plt.title(f"{player} - Ground Stats")
    plt.xlabel('Ground')
    plt.ylabel('Runs')
    plt.show()
    # Display ground stats in table
    table.delete("1.0", "end")
    table.insert("end", player_ground.to_string(index=False))
    
    # Convert the Matplotlib figure to a Tkinter canvas
    fig = plt.gcf()
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()

    # Update the Tkinter canvas widget in the GUI
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

# Create the GUI window
root = tk.Tk()
root.title("Player Stats")

# Create a dropdown menu for player selection
var = tk.StringVar(root)
var.set(list(players.keys())[0])  # Default player is the first one
player_menu = tk.OptionMenu(root, var, *players.keys())
player_menu.pack()

# Create a button to update the player stats
update_button = tk.Button(root, text="Update Stats", command=lambda: update_stats(var.get()))
update_button.pack()

# Create buttons to show player stats against opposition and at venues
opposition_button = tk.Button(root, text="Show Opposition Stats", command=show_opposition_stats)
venue_button = tk.Button(root, text="Show Venue Stats", command=show_venue_stats)

#Create a button to go back to the main screen
back_button = tk.Button(root, text="Back", command=go_back)

table = tk.Text(root, height=10)
table.pack()

#Run the GUI main loop
root.mainloop()


# In[15]:


hardik_df


# In[ ]:


kohli_opposition.to_excel('Kohliopp.xlsx', index=False)
kohli_ground.to_excel('Kohligrd.xlsx', index=False)


# In[2]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data into a Pandas DataFrame
kohli_df = pd.read_excel("Kohli.xlsx")




 #Calculate mean, median, and standard deviation of runs scored, number of 4s, and number of 6s by batting position
stats = kohli_df.groupby('Pos')[['Runs']].agg(['mean', 'median', 'std'])

# Calculate total runs, 4s, and 6s by batting position
totals = kohli_df.groupby('Pos')[['Runs']].sum()

# Print the statistics and totals for each batting position
print(stats)
print(totals)


# In[ ]:



# Create histograms of runs scored, number of 4s, and number of 6s by batting position
for col in ['Runs', '4s', '6s']:
    sns.histplot(data=kohli_df, x=col, hue='Pos', kde=True, stat='density')

# Use correlation analysis to examine the relationship between runs scored, number of 4s, and number of 6s
corr = kohli_df[['Runs', '4s', '6s']].corr()
sns.heatmap(corr, annot=True, cmap='coolwarm')

# Use regression analysis to model the relationship between batting position, runs scored, number of 4s, and number of 6s
import statsmodels.api as sm
X = kohli_df[['Pos', '4s', '6s']]
y = kohli_df['Runs']
X = sm.add_constant(X)
model = sm.OLS(y, X).fit()
print(model.summary())


# In[ ]:




