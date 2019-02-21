
# coding: utf-8

# In[56]:

import matplotlib.pyplot as plt
import pandas as pd
matches=pd.read_csv('matches.csv')


# In[57]:

print(matches.head(5))


# In[58]:

print (matches.shape)
print (matches.columns)
print(matches.dtypes)


# In[59]:

print(matches.isnull().sum())


# In[60]:

matches.drop(['id','umpire3'],axis=1,inplace=True)


# In[61]:

matches.replace('Rising Pune Supergiant','Rising Pune Supergiants', inplace=True)


# In[62]:

print(matches.columns)


# In[63]:

import numpy as np
all_teams = np.unique(matches['team1'])
print (all_teams)


# In[64]:

all_city = matches['city'].unique()
all_city = all_city[:-1]
print (all_city)


# In[65]:

all_stadium = np.unique(matches['venue'])
print (all_stadium)


# In[66]:

all_umpires = set(matches['umpire1']).union(set(matches['umpire2']))
all_umpires = list(all_umpires)
all_umpires = all_umpires[1:]
print (all_umpires)


# In[67]:

print ("Total matches played : ",(matches.shape[0]))
print ("Number of different cities : ",(len(all_city)))
print ("Number of different venues : ",(len(all_stadium)))
print ("Total umpires : ",(len(all_umpires)))


# In[68]:

matches = matches[matches['result'] != 'no result']
print(matches.shape)


# In[74]:


df_umpires = pd.concat([matches['umpire1'], matches['umpire2']]) 
df_umpires.value_counts().head(10).plot.bar(colormap='Accent')

plt.xticks(fontsize=12)
plt.xlabel('Umpire',fontsize=14)
plt.ylabel('Number of matches',fontsize=16)
plt.title('Top 10 umpires',fontsize=18)
plt.show()


# In[72]:

df_stadium = matches['venue'].value_counts()
print ("Number of matches played at different stadiums : ",(df_stadium))

df_stadium.sort_values(ascending=True).plot.barh(figsize=(10,12), colormap='summer')

plt.yticks(fontsize=12)
plt.xlabel('Number of matches played',fontsize=14)
plt.ylabel('Stadiums',fontsize=16)
plt.title('Number of matches played at different stadiums',fontsize=18)
plt.show()


# In[80]:

df_toss_decision = 100 * (matches['toss_decision'].value_counts()) / matches.shape[0]
print ("Toss decisions in terms of % :\n{}\n".format(df_toss_decision))


# In[84]:

import seaborn as sns
sns.set(rc={'figure.figsize':(10,6)})
plt.xticks(fontsize=14)
sns.countplot(x='season', hue='toss_decision', data=matches)
plt.show()


# In[87]:

df_team_matches = (matches.team1.value_counts() + matches.team2.value_counts()).sort_values(ascending=False)
print ("Number of matches played by each team :\n\n{}\n".format(df_team_matches))

df_team_matches.plot(kind='bar',figsize=(10,6))

plt.xticks(fontsize=12)
plt.xlabel('Teams',fontsize=14)
plt.ylabel('Number of matches played',fontsize=16)
plt.title('Number of matches played by each team',fontsize=18)
plt.show()


# In[89]:

df_winner = matches['winner'].value_counts().sort_values(ascending=False)
df_winner_per = 100 * df_winner[all_teams]/ df_team_matches[all_teams]

print ("Number of matches won by each team :\n\n{}\n".format(df_winner))
print ("Percentage of matches won by each team :\n\n{}\n".format(df_winner_per))

df_winner_per.sort_values(ascending=False).plot(kind='bar',figsize=(10,6), colormap='summer')

plt.xticks(fontsize=12)
plt.ylim(0,100)
plt.xlabel('Teams',fontsize=14)
plt.ylabel('% of matches won',fontsize=16)
plt.title('Percentage of matches won by each team',fontsize=18)
plt.show()


# In[90]:

df_toss = matches.toss_winner.value_counts()
df_toss_num = df_toss[all_teams].sort_values(ascending=False)
df_toss_per = 100 * df_toss[all_teams]/df_team_matches[all_teams].values

print ("Number of times a team has won the toss : \n")
print (df_toss_num)

print ("\nPercentage a team has won the toss : \n")
print (df_toss_per)

df_toss_per.sort_values(ascending=False).plot(kind='bar',figsize=(10,6))

plt.xticks(fontsize=12)
plt.xlabel('Teams',fontsize=16)
plt.ylim(0,100)
plt.ylabel('%',fontsize=14)
plt.title('Percetange a team has won the toss',fontsize=18)
plt.show()


# In[93]:

df_toss_winner = matches[matches.toss_winner == matches.winner]['winner']
df_toss_winner_count = df_toss_winner.value_counts()
df_toss_winner_per = 100 * df_toss_winner.value_counts()[all_teams]/df_team_matches[all_teams].values
toss_match_win_per = df_toss_winner.count()/float(matches.shape[0])

print ("Percentage of matches won by teams after winning the toss : {}\n".format(toss_match_win_per))

print ("Number of matches won by teams after winning the toss : \n")
print (df_toss_winner_count)

print ("\nPercentage of matches won by teams after winning the toss : \n")
print (df_toss_winner_per)

df_toss_winner_per.sort_values(ascending=False).plot(kind='bar',figsize=(10,6),colormap='Dark2')

plt.xticks(fontsize=12)
plt.xlabel('Teams',fontsize=16)
plt.ylim(0,100)
plt.ylabel('%',fontsize=14)
plt.title('Percentage of matches won after winning the toss',fontsize=18)
plt.show()


# In[104]:

#Percentage of teams winning the match after winning the toss (field first)

df_toss_winner_field = matches[(matches.toss_winner == matches.winner) & (matches.toss_decision == 'field')]['winner']
df_toss_winner_field_count = df_toss_winner_field.value_counts()
df_toss_winner_field_per = 100 * df_toss_winner_field.value_counts()[all_teams]/df_team_matches[all_teams].values
df_toss_winner_field_total_per = df_toss_winner_field.count()/float(matches.shape[0])

print ("Percentage of matches won by teams after winning the toss and electing to field first : {}\n".format(df_toss_winner_field_total_per))

print ("Number of matches won by teams after winning the toss and electing to field first: \n")
print (df_toss_winner_field_count)

print ("\nPercentage of matches won by teams after winning the toss and electing to field first: \n")
print (df_toss_winner_field_per)

df_toss_winner_field_per.sort_values(ascending=False).plot(kind='bar',figsize=(10,6))

plt.xticks(fontsize=12)
plt.xlabel('Teams',fontsize=16)
plt.ylim(0,100)
plt.ylabel('%',fontsize=14)
plt.title('Percentage of matches won after winning the toss and electing to field first',fontsize=18)
plt.show()


# In[106]:

#Percentage of teams winning the match after winning the toss (bat first)

df_toss_winner_bat = matches[(matches.toss_winner == matches.winner) & (matches.toss_decision == 'bat')]['winner']
df_toss_winner_bat_count = df_toss_winner_bat.value_counts()
df_toss_winner_bat_per = 100 * df_toss_winner_bat.value_counts()[all_teams]/df_team_matches[all_teams].values
df_toss_winner_bat_total_per = df_toss_winner_bat.count()/float(matches.shape[0])

print ("Percentage of matches won by teams after winning the toss and electing to bat first : {}\n".format(df_toss_winner_bat_total_per))

print ("Number of matches won by teams after winning the toss and electing to bat first: \n")
print (df_toss_winner_bat_count)

print ("\nPercentage of matches won by teams after winning the toss and electing to bat first: \n")
print (df_toss_winner_bat_per)

df_toss_winner_bat_per.sort_values(ascending=False).plot(kind='bar',figsize=(10,6),colormap='Set2')

plt.xticks(fontsize=12)
plt.xlabel('Teams',fontsize=16)
plt.ylim(0,100)
plt.ylabel('%',fontsize=14)
plt.title('Percentage of matches won after winning the toss and electing to bat first',fontsize=18)
plt.show()


# In[107]:

#HeatMap

total_teams = len(all_teams)
heatmap_scores = np.zeros((total_teams, total_teams))
for i,team1 in enumerate(all_teams):
    for j,team2 in enumerate(all_teams):
        matches_played = 0
        if team1 != team2:
            df_winner = matches[(matches.team1 == team1) & (matches.team2 == team2)]['winner']
            matches_played = df_winner.shape[0]
            #print team1, team2, matches_played
            heatmap_scores[i,j] += matches_played
            heatmap_scores[j,i] += matches_played
        
fig, ax = plt.subplots(1, 1)
fig.set_figheight(7.5)
fig.set_figwidth(10)

ax1 = sns.heatmap(heatmap_scores, xticklabels = all_teams, yticklabels = all_teams, linewidths = 0.5, annot = True, cmap="OrRd", ax = ax)

ax1.set_title("No. of Matches played TeamA vs TeamB",fontsize=16)

fig.tight_layout()
plt.show()


# In[108]:

#Most number of MoMs

matches['player_of_match'].value_counts().head(10).plot.bar(figsize=(10,6), color='R')

plt.xticks(fontsize=12)
plt.ylim(0,30)
plt.xlabel('Player',fontsize=14)
plt.ylabel('Number of matches',fontsize=16)
plt.title('Top 10 players with most no. of MoMs',fontsize=18)
plt.show()


# In[ ]:



