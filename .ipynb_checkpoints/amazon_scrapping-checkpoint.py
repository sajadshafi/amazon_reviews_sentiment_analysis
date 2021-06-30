import requests
from bs4 import BeautifulSoup

# links and Headers
HEADERS = ({'User-Agent': 
           'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36', 
                           'Accept-Language': 'en-US, en;q=0.5'})

# Link to the amazon product reviews
url = 'https://www.amazon.in/Samsung-Internal-Solid-State-MZ-V7S500BW/product-reviews/B07MFBLN7K/ref=cm_cr_arp_d_paging_btm_next_2?ie=UTF8&reviewerType=all_reviews&pageNumber='

review_list = []

def retrieve_reviews(soup):
    # Get only those divs from the website which have a property data-hook and its value is review
    reviews = soup.find_all("div", {'data-hook': "review"})

    # Retrieving through the raw text inside the reviews
    for item in reviews:
        
        review = {
        # Get the title of the review
        'title': item.find("a", {'data-hook': "review-title"}).text.strip(),

        # Get the rating. It will be like 4.5 out of 5 stars. So we have to remove out of 5 stars from it and only keep float value 4.5, 3.4, etc.
        'rating': item.find("i", {'data-hook': "review-star-rating"}).text.replace("out of 5 stars", "").strip(),

        # Get the actual review text 
        'review_text': item.find("span", {'data-hook': "review-body"}).text.strip()
        }

        review_list.append(review)

# Get the page content from amazon
# as we know we have 43 pages to visit and get content from
for pageNumber in range(1, 51):
    raw_text = requests.get(url=url+(str(pageNumber)), headers = HEADERS)
    soup = BeautifulSoup(raw_text.text, 'lxml')
    retrieve_reviews(soup)

for index in range(len(review_list)):
    # Print out all the reviews inside of a reviews_list
    print(f"{index+1})  {review_list[index]}")
    print("")


# Now we have successfully retrieved almost top 500 reviews from the amazon
# We will now export all of these reviews to a csv file

import csv
import pandas as pd

# Create dataframe out of all the reviews from amazon
reviews_df = pd.DataFrame(review_list)

# Put that dataframe into an excel file
reviews_df.to_excel('samsung_ssd_rating.xlsx', index = False)

'''
By default this code will make an excel file inside the folder to where it will be executed but we can also give it a path where we want to store it
'''

print("Done.")


