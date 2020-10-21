
## interactive_story_1
* restaurant_search{"cuisine": "chinese", "location": "Bangalore", "price": "high"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Bangalore"}
    - slot{"price": "high"}
    - action_chklocation
    - action_search_restaurants
    - slot{"emailbody": "Showing you top rated restaurants:Yauatcha in Level 5, 1 MG Lido Mall, MG Road, Bangalore has been rated 4.7\n And the average price for two people is: 2000\nThe Fatty Bao - Asian Gastro Bar in 610, 3rd Floor, 12th Main, Off 80 Feet Road, Indiranagar, Bangalore has been rated 4.6\n And the average price for two people is: 1200\nHae Kum Gang in 20, Pauls Castle, Castle Street, Ashok Nagar, Brigade Road, Bangalore has been rated 4.6\n And the average price for two people is: 1100\nHigh Ultra Lounge in 26/1, 31st Floor, Dr. Rajkumar Road, World Trade Centre, Brigade Gateway Campus, Malleshwaram, Bangalore has been rated 4.4\n And the average price for two people is: 2600\nChina Pearl in 53/1, 5th Cross, Koramangala 6th Block, Bangalore has been rated 4.4\n And the average price for two people is: 1100\nMamagoto in 949, 12th Main, Ground Floor, Off 100 Feet Road, Indiranagar, Bangalore has been rated 4.3\n And the average price for two people is: 2000\nSriracha in 204, 2nd Level, 4th Floor, Comet Block, UB City, Vittal Mallya Road, Lavelle Road, Bangalore has been rated 4.3\n And the average price for two people is: 1500\nThe Lantern Restaurant & Bar - The Ritz-Carlton, Bangalore in The Ritz-Carlton, 99, Residency Road, Bangalore has been rated 4.3\n And the average price for two people is: 3500\nBangalore Mandarin in 196, 3rd Floor, Double Road, Indiranagar, Bangalore has been rated 4.3\n And the average price for two people is: 1100\nKitchen On Table in Gate 9, P.A.E. Canteen, Bellary Road, Palace Ground, Sadashiv Nagar, Bangalore has been rated 4.2\n And the average price for two people is: 1500\n"}
    - utter_email_conf

## interactive_story_2
* restaurant_search{"cuisine": "chinese", "location": "Denver", "price": "high"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Denver"}
    - slot{"price": "high"}
    - action_chklocation

## interactive_story_1
* restaurant_search{"location": "bangalore", "cuisine": "chinese", "price": "high"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "bangalore"}
    - slot{"price": "high"}
    - action_search_restaurants
    - utter_email_conf

## interactive_story_2
* restaurant_search{"location": "bangalore", "cuisine": "chinese", "price": "high"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "bangalore"}
    - slot{"price": "high"}
    - action_chklocation
    - action_search_restaurants

## interactive_story_1
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_chklocation
* restaurant_search{"location": "Bangalore"}
    - slot{"location": "Bangalore"}
    - action_chklocation
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - utter_ask_budget
* greet
    - action_search_restaurants
    - slot{"emailbody": "Sorry, No results found for your criteria. Would you like to search for some other restaurants?"}
* restaurant_search{"location": "Delhi", "cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Delhi"}
    - utter_ask_budget
* greet
    - action_search_restaurants
    - slot{"emailbody": "Sorry, No results found for your criteria. Would you like to search for some other restaurants?"}
* restaurant_search{"location": "delhi", "price": "high"}
    - slot{"location": "delhi"}
    - slot{"price": "high"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - action_search_restaurants
* restaurant_search{"cuisine": "american", "location": "delhi", "price": "high"}
    - slot{"cuisine": "american"}
    - slot{"location": "delhi"}
    - slot{"price": "high"}
    - action_chklocation
    - action_search_restaurants
    - utter_email_conf
* affirm
    - utter_email_id_ask
* restaurant_search{"email": "urspraveenb@gmail.com"}
    - slot{"email": "urspraveenb@gmail.com"}
    - action_sendemail
    - utter_email_sent
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_chklocation
