import pandas as pd
from bs4 import BeautifulSoup
from instagramy import  InstagramUser
import requests
import numpy as np
session_id ="1788a069f20-4afb8e"



def extract(keyword):

    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'}
    url = 'https://www.searchmy.bio/search?q='+ keyword

    r=requests.get(url).text
    soup=BeautifulSoup(r,'lxml')
    divs=soup.find_all('div',class_='search-result')
    for items in divs:
        username=items.find('div',class_='search-result-username').text
        fullname=items.find('div',class_='search-result-fullname').text
        followers=items.find('div',class_='search-result-data-point').text
        profile_link=(items.find('a',class_='search-result-button')['href'])
        biography=items.find('div',class_='search-result-bio').text
        userdetails={
        'username':username,
        'fullname':fullname,
        'followers':followers,
        'profile_link':profile_link,
        'biography':biography

              }
        userdata.append(userdetails)
    divs_more=soup.find_all('read-more',class_='ng-scope ng-isolate-scope')
    for items in divs_more:
        user_name = items.find('div', class_='search-result-username ng-binding').text
        full_name = items.find('div', class_='search-result-fullname ng-binding').text
        total_followers = items.find('div', class_='search-result-data-point ng-binding').text
        profile_link_instagram = (items.find('a', class_='search-result-button')['href'])
        biography_profile = items.find('div', class_='search-result-bio ng-binding').text
        user_details = {
            'username': user_name,
            'fullname': full_name,
            'followers': total_followers,
            'profile_link': profile_link_instagram,
            'biography': biography_profile

        }
        userdata.append(user_details)

    return


userdata=[]

extract("design")


df=pd.DataFrame(userdata)
print(df.head())
df.to_csv('userdata.csv')