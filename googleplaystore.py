import pandas as pd
import numpy as np

df = pd.read_csv('googleplaystore_a.csv')
print(df.describe)

##Basic questions:
#1. How many different titles are there for this year?
df = df.drop_duplicates(subset ="App")
print("There are 9604 different Apps in the google playstore this year.")
#2. What is the overall rating for all these apps?
overall_rating = df['Rating'].mean()
print('There overall rating for all the apps combined is: ' + str(overall_rating))
#3. What is the genre breakdown for all these apps?
grp_genre = df.groupby('Genres')
print(grp_genre.count())
print("Unexpected difficulty. There are over 118 different genres.")
print("Some of these genres are subgenres of the others.")
print("For example, There's a 'Strategy' genre, and a 'Strategy;Action & Adventure' genre.")
print("Replacing similar genres into more broad ones...")
#Creating a lambda function to replace similar Genres
def simpler_Genre(current_Genre):
    if(";" in current_Genre):
        return current_Genre[:current_Genre.find(';')]
    return current_Genre
df['Genres'] = df['Genres'].apply(simpler_Genre)
print(df.groupby('Genres').count().sort_values(by=['App'], ascending=False))
    # print("A total of 48 different broarder genres.")
    # print("Top 3 Genres are Tools: 820, Entertainment: 589, Education: 576")
    # print("Bottom 3 Genres are Word: 23, Music: 22, Music & Audio: 1")
#4. What is the content breakdown for all these apps?
print("Content rating breakdown as follows:")
print(df.groupby('Content Rating').count())
#5. Which app was installed the most?
print("Most installed app(s):")
max_downloads = df['Installs'].max()
print(df.loc[df['Installs']==max_downloads].sort_values(by=['App'])['App'])
#6. Which app received the highest overall ratings?
print("Highest overall ratings (rating*reviews/Installs):")
#First change installs column to a float value.
#Creating a lambda function to remove '+' and ',' from Installs values
def installs_to_float(current_installs):
    if("+" in current_installs):
        new_installs = current_installs[:current_installs.find('+')]
        final_installs = new_installs.replace(",","")
        return float(final_installs)
    return current_installs
df['Installs(float)'] = df['Installs'].apply(installs_to_float)
df['rating*reviews'] = df['Rating'].multiply(df['Reviews'], axis="index")
#Fill in 0 installs with 1.
df['Installs(float)'] = df['Installs(float)'].replace({0:1})
df['Installs(float)'] = df['Installs(float)'].fillna(1)
print(df.select_dtypes(include=['float64']))
#df['Overall Ratings'] = df['rating*reviews'].divide(df['Installs(float)'],axis="index")
#print(df['Overall Ratings'])

##Deeper questions:
#1. Assuming that higher ratings determines a successful app, what qualities
    #are associated with higher rating apps?
#print(df.corr())
#2. The app market is dominated by free apps, what could make the paid apps
    #gain more downloads?
#3. What are the highest rated (3) apps in each of the genres?
#4. What qualities correlate to more downloads in an app?
