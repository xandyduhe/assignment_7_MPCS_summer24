# problem 4 
# week 7 


import sys
import requests
import json
import datetime

# Sign up for a free API at https://newsapi.org/register
API_KEY = "ecc30ff3374d4c9bbde729f361d6018e"


def top_headlines():

    """Display top headlines from user selected category from news api """

    # dictionary of categories from news api 
    categories = {'1': 'business', 
                '2': 'entertainment',   
                '3': 'general',
                '4': 'health', 
                '5': 'science', 
                '6': 'sports',
                '7': 'technology'}

    # take user selection 
    category_selection = input('''Select which category would you like to headlines for: 
    [1] business   
    [2] entertainment
    [3] general   
    [4] health   
    [5] science   
    [6] sports   
    [7] technology \n\n>> ''')

    # format selection into http
    try:
        url = f"https://newsapi.org/v2/top-headlines?country=us&category={categories[category_selection]}&pageSize=10&apiKey={API_KEY}"
        return url
    except:
        print(f'Invalid category selection: {category_selection}')
        return False


def search():
    """Use user search term to search newsapi"""

    # take user search term 
    search_term = input('Enter your search term: \n>> ')

    # format serch term inot search http address 
    try: 
        # Search headlines with a query (q)
        url = f"https://newsapi.org/v2/everything?q={search_term}&sortBy=publishedAt&pageSize=10&apiKey={API_KEY}"
        return url 
    
    except:
        print(f'Could not use your search term {search_term}. Try again.\n')
        return False 


def user_choice():
    """Take user choice on searching or selecteing fromn top categrories"""

    # take user choice for search or top headlines 
    choice = input("Please make a choice: [1] Top headlines [2] Search\n>> ")

    # execute definitions based on user choice 
    try: 
        if choice == '1': # top headlines 
            url = top_headlines()

            while url is False:
                url = top_headlines()
            
        if choice == '2': # search 
            url = search()

            while url is False:
                url = search()
        
        return url

    except:
        print(f'Entry invalid. Choice {choice} does not exist. Try again.\n')
        return False
 

def main():

    print('Welcome to Command Line News! \n')

    url = user_choice()

    while url is False: # invalid entry from user 
        url = user_choice()

    # Request URL Data
    r = requests.get(url)

    # Convert into JSON
    json_data = r.json()

    # # Newapi query information
    status = json_data["status"]
    total_results = json_data["totalResults"]
    articles = json_data["articles"]


    # # # Note the `pageSize` argument in the API can be used to limit the result that
    # # # are returned
    for article in articles:

        # reformat date 
        date = datetime.datetime.strptime(article['publishedAt'], '%Y-%m-%dT%H:%M:%SZ')
        published_at = date.strftime('%b %d, %Y')

        # print
        print("*",article['title'], f'({published_at})')
        print("\t",article['description'])
        print("-----------------------------------------------\n")

if __name__ == '__main__':
    main()



