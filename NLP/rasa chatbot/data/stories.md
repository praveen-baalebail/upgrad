## complete path with location true 1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_chklocation
    - slot{"loc_avl": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_chkcuisine
    - slot{"cusn_avl": true}
    - utter_ask_budget
* restaurant_search{"price": "medium"}
    - slot{"price": "medium"}
    - action_search_restaurants
	- slot{"emailbody": "Showing you top rated restaurants:Yauatcha in Level 5, 1 MG Lido Mall, MG Road, Bangalore has been rated 4.7\n And the average price for two people is: 2000\nThe Fatty Bao - Asian Gastro Bar in 610, 3rd Floor, 12th Main, Off 80 Feet Road, Indiranagar, Bangalore has been rated 4.6\n And the average price for two people is: 1200\nHae Kum Gang in 20, Pauls Castle, Castle Street, Ashok Nagar, Brigade Road, Bangalore has been rated 4.6\n And the average price for two people is: 1100\nHigh Ultra Lounge in 26/1, 31st Floor, Dr. Rajkumar Road, World Trade Centre, Brigade Gateway Campus, Malleshwaram, Bangalore has been rated 4.4\n And the average price for two people is: 2600\nChina Pearl in 53/1, 5th Cross, Koramangala 6th Block, Bangalore has been rated 4.4\n And the average price for two people is: 1100\nMamagoto in 949, 12th Main, Ground Floor, Off 100 Feet Road, Indiranagar, Bangalore has been rated 4.3\n And the average price for two people is: 2000\nSriracha in 204, 2nd Level, 4th Floor, Comet Block, UB City, Vittal Mallya Road, Lavelle Road, Bangalore has been rated 4.3\n And the average price for two people is: 1500\nThe Lantern Restaurant & Bar - The Ritz-Carlton, Bangalore in The Ritz-Carlton, 99, Residency Road, Bangalore has been rated 4.3\n And the average price for two people is: 3500\nBangalore Mandarin in 196, 3rd Floor, Double Road, Indiranagar, Bangalore has been rated 4.3\n And the average price for two people is: 1100\nKitchen On Table in Gate 9, P.A.E. Canteen, Bellary Road, Palace Ground, Sadashiv Nagar, Bangalore has been rated 4.2\n And the average price for two people is: 1500\n"}
	- slot{"rest_found": true}
    - utter_email_conf
* affirm
    - utter_email_id_ask
* restaurant_search{"email": "abc.def@gmail.com"}
    - slot{"email": "abc.def@gmail.com"}
    - action_sendemail
    - utter_email_sent
    - utter_goodbye
	- action_restart

## complete path with location true 1 and results 0
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_chklocation
    - slot{"loc_avl": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_chkcuisine
    - slot{"cusn_avl": false}
    - action_chkcuisine
    - slot{"cusn_avl": true}
    - utter_ask_budget
* restaurant_search{"price": "medium"}
    - slot{"price": "medium"}
    - action_search_restaurants
	- slot{"emailbody": "Sorry, No results found for your criteria. Would you like to search for some other restaurant criteria?\n"}
    - slot{"rest_found": false}
	- action_restart
	
## complete path with location false 1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_chklocation
    - slot{"loc_avl": false}
	- action_restart

## complete path with location false 2
* greet
    - utter_greet
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_chklocation
    - slot{"loc_avl": false}
	- action_restart

## complete path with location false 3
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_chklocation
    - slot{"loc_avl": false}
	- action_restart
	
## complete path with cuisine first and locatio false
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_chkcuisine
    - slot{"cusn_avl": true}
	- utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_chklocation
    - slot{"loc_avl": false}
	- utter_ask_location
* restaurant_search{"location": "delhi"}
	- slot{"loc_avl": true}
	- action_chklocation
    - utter_ask_budget
* restaurant_search{"price": "medium"}
    - slot{"price": "medium"}
    - action_search_restaurants
    - slot{"emailbody": "Showing you top rated restaurants:Yauatcha in Level 5, 1 MG Lido Mall, MG Road, Bangalore has been rated 4.7\n And the average price for two people is: 2000\nThe Fatty Bao - Asian Gastro Bar in 610, 3rd Floor, 12th Main, Off 80 Feet Road, Indiranagar, Bangalore has been rated 4.6\n And the average price for two people is: 1200\nHae Kum Gang in 20, Pauls Castle, Castle Street, Ashok Nagar, Brigade Road, Bangalore has been rated 4.6\n And the average price for two people is: 1100\nHigh Ultra Lounge in 26/1, 31st Floor, Dr. Rajkumar Road, World Trade Centre, Brigade Gateway Campus, Malleshwaram, Bangalore has been rated 4.4\n And the average price for two people is: 2600\nChina Pearl in 53/1, 5th Cross, Koramangala 6th Block, Bangalore has been rated 4.4\n And the average price for two people is: 1100\nMamagoto in 949, 12th Main, Ground Floor, Off 100 Feet Road, Indiranagar, Bangalore has been rated 4.3\n And the average price for two people is: 2000\nSriracha in 204, 2nd Level, 4th Floor, Comet Block, UB City, Vittal Mallya Road, Lavelle Road, Bangalore has been rated 4.3\n And the average price for two people is: 1500\nThe Lantern Restaurant & Bar - The Ritz-Carlton, Bangalore in The Ritz-Carlton, 99, Residency Road, Bangalore has been rated 4.3\n And the average price for two people is: 3500\nBangalore Mandarin in 196, 3rd Floor, Double Road, Indiranagar, Bangalore has been rated 4.3\n And the average price for two people is: 1100\nKitchen On Table in Gate 9, P.A.E. Canteen, Bellary Road, Palace Ground, Sadashiv Nagar, Bangalore has been rated 4.2\n And the average price for two people is: 1500\n"}
    - slot{"rest_found": true}
	- utter_email_conf
* affirm
    - utter_email_id_ask
* restaurant_search{"email": "abc.def@gmail.com"}
    - slot{"email": "abc.def@gmail.com"}
    - action_sendemail
    - utter_email_sent
    - utter_goodbye
	- action_restart

## complete path with cuisine first and locatio false
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_chkcuisine
    - slot{"cusn_avl": true}
	- utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_chklocation
    - slot{"loc_avl": false}
	- utter_ask_location
* restaurant_search{"location": "delhi"}
	- slot{"loc_avl": true}
	- action_chklocation
    - slot{"loc_avl": true}
    - utter_ask_budget
* restaurant_search{"price": "medium"}
    - slot{"price": "medium"}
    - action_search_restaurants
    - slot{"emailbody": "Sorry, No results found for your criteria. Would you like to search for some other restaurant criteria?\n"}
    - slot{"rest_found": false}
	- action_restart

## complete path with cuisine false and locatio false
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_chkcuisine
    - slot{"cusn_avl": false}
	- utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
	- action_chkcuisine
    - slot{"cusn_avl": true}
	- utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_chklocation
    - slot{"loc_avl": false}
	- utter_ask_location
* restaurant_search{"location": "delhi"}
	- slot{"loc_avl": true}
	- action_chklocation
    - utter_ask_budget
* restaurant_search{"price": "medium"}
    - slot{"price": "medium"}
    - action_search_restaurants
    - slot{"emailbody": "Showing you top rated restaurants:Yauatcha in Level 5, 1 MG Lido Mall, MG Road, Bangalore has been rated 4.7\n And the average price for two people is: 2000\nThe Fatty Bao - Asian Gastro Bar in 610, 3rd Floor, 12th Main, Off 80 Feet Road, Indiranagar, Bangalore has been rated 4.6\n And the average price for two people is: 1200\nHae Kum Gang in 20, Pauls Castle, Castle Street, Ashok Nagar, Brigade Road, Bangalore has been rated 4.6\n And the average price for two people is: 1100\nHigh Ultra Lounge in 26/1, 31st Floor, Dr. Rajkumar Road, World Trade Centre, Brigade Gateway Campus, Malleshwaram, Bangalore has been rated 4.4\n And the average price for two people is: 2600\nChina Pearl in 53/1, 5th Cross, Koramangala 6th Block, Bangalore has been rated 4.4\n And the average price for two people is: 1100\nMamagoto in 949, 12th Main, Ground Floor, Off 100 Feet Road, Indiranagar, Bangalore has been rated 4.3\n And the average price for two people is: 2000\nSriracha in 204, 2nd Level, 4th Floor, Comet Block, UB City, Vittal Mallya Road, Lavelle Road, Bangalore has been rated 4.3\n And the average price for two people is: 1500\nThe Lantern Restaurant & Bar - The Ritz-Carlton, Bangalore in The Ritz-Carlton, 99, Residency Road, Bangalore has been rated 4.3\n And the average price for two people is: 3500\nBangalore Mandarin in 196, 3rd Floor, Double Road, Indiranagar, Bangalore has been rated 4.3\n And the average price for two people is: 1100\nKitchen On Table in Gate 9, P.A.E. Canteen, Bellary Road, Palace Ground, Sadashiv Nagar, Bangalore has been rated 4.2\n And the average price for two people is: 1500\n"}
    - slot{"rest_found": true}
	- utter_email_conf
* affirm
    - utter_email_id_ask
* restaurant_search{"email": "abc.def@gmail.com"}
    - slot{"email": "abc.def@gmail.com"}
    - action_sendemail
    - utter_email_sent
    - utter_goodbye
	- action_restart

## complete path with cuisine false and locatio true
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_chkcuisine
    - slot{"cusn_avl": false}
	- utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
	- action_chkcuisine
    - slot{"cusn_avl": true}
	- utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_chklocation
    - slot{"loc_avl": true}
    - utter_ask_budget
* restaurant_search{"price": "medium"}
    - slot{"price": "medium"}
    - action_search_restaurants
    - slot{"emailbody": "Sorry, No results found for your criteria. Would you like to search for some other restaurant criteria?\n"}
    - slot{"rest_found": false}
	- action_restart
	
## complete path with location true 1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_chklocation
    - slot{"loc_avl": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_chkcuisine
    - slot{"cusn_avl": true}
    - utter_ask_budget
* restaurant_search{"price": "medium"}
    - slot{"price": "medium"}
    - action_search_restaurants
	
## complete path with cuisine first 1
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_chkcuisine
    - slot{"cusn_avl": true}
	- utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_chklocation
    - slot{"loc_avl": true}
    - utter_ask_budget
* restaurant_search{"price": "medium"}
    - slot{"price": "medium"}
    - action_search_restaurants
    - slot{"emailbody": "Showing you top rated restaurants:Yauatcha in Level 5, 1 MG Lido Mall, MG Road, Bangalore has been rated 4.7\n And the average price for two people is: 2000\nThe Fatty Bao - Asian Gastro Bar in 610, 3rd Floor, 12th Main, Off 80 Feet Road, Indiranagar, Bangalore has been rated 4.6\n And the average price for two people is: 1200\nHae Kum Gang in 20, Pauls Castle, Castle Street, Ashok Nagar, Brigade Road, Bangalore has been rated 4.6\n And the average price for two people is: 1100\nHigh Ultra Lounge in 26/1, 31st Floor, Dr. Rajkumar Road, World Trade Centre, Brigade Gateway Campus, Malleshwaram, Bangalore has been rated 4.4\n And the average price for two people is: 2600\nChina Pearl in 53/1, 5th Cross, Koramangala 6th Block, Bangalore has been rated 4.4\n And the average price for two people is: 1100\nMamagoto in 949, 12th Main, Ground Floor, Off 100 Feet Road, Indiranagar, Bangalore has been rated 4.3\n And the average price for two people is: 2000\nSriracha in 204, 2nd Level, 4th Floor, Comet Block, UB City, Vittal Mallya Road, Lavelle Road, Bangalore has been rated 4.3\n And the average price for two people is: 1500\nThe Lantern Restaurant & Bar - The Ritz-Carlton, Bangalore in The Ritz-Carlton, 99, Residency Road, Bangalore has been rated 4.3\n And the average price for two people is: 3500\nBangalore Mandarin in 196, 3rd Floor, Double Road, Indiranagar, Bangalore has been rated 4.3\n And the average price for two people is: 1100\nKitchen On Table in Gate 9, P.A.E. Canteen, Bellary Road, Palace Ground, Sadashiv Nagar, Bangalore has been rated 4.2\n And the average price for two people is: 1500\n"}
    - slot{"rest_found": true}
	- utter_email_conf
* affirm
    - utter_email_id_ask
* restaurant_search{"email": "abc.def@gmail.com"}
    - slot{"email": "abc.def@gmail.com"}
    - action_sendemail
    - utter_email_sent
    - utter_goodbye
	- action_restart

## complete path with budget first
* greet
    - utter_greet
* restaurant_search{"price": "medium"}
    - slot{"price": "medium"}
	- utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_chklocation
    - slot{"loc_avl": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_chkcuisine
    - slot{"cusn_avl": true}
    - action_search_restaurants
    - slot{"emailbody": "Showing you top rated restaurants:Yauatcha in Level 5, 1 MG Lido Mall, MG Road, Bangalore has been rated 4.7\n And the average price for two people is: 2000\nThe Fatty Bao - Asian Gastro Bar in 610, 3rd Floor, 12th Main, Off 80 Feet Road, Indiranagar, Bangalore has been rated 4.6\n And the average price for two people is: 1200\nHae Kum Gang in 20, Pauls Castle, Castle Street, Ashok Nagar, Brigade Road, Bangalore has been rated 4.6\n And the average price for two people is: 1100\nHigh Ultra Lounge in 26/1, 31st Floor, Dr. Rajkumar Road, World Trade Centre, Brigade Gateway Campus, Malleshwaram, Bangalore has been rated 4.4\n And the average price for two people is: 2600\nChina Pearl in 53/1, 5th Cross, Koramangala 6th Block, Bangalore has been rated 4.4\n And the average price for two people is: 1100\nMamagoto in 949, 12th Main, Ground Floor, Off 100 Feet Road, Indiranagar, Bangalore has been rated 4.3\n And the average price for two people is: 2000\nSriracha in 204, 2nd Level, 4th Floor, Comet Block, UB City, Vittal Mallya Road, Lavelle Road, Bangalore has been rated 4.3\n And the average price for two people is: 1500\nThe Lantern Restaurant & Bar - The Ritz-Carlton, Bangalore in The Ritz-Carlton, 99, Residency Road, Bangalore has been rated 4.3\n And the average price for two people is: 3500\nBangalore Mandarin in 196, 3rd Floor, Double Road, Indiranagar, Bangalore has been rated 4.3\n And the average price for two people is: 1100\nKitchen On Table in Gate 9, P.A.E. Canteen, Bellary Road, Palace Ground, Sadashiv Nagar, Bangalore has been rated 4.2\n And the average price for two people is: 1500\n"}
    - slot{"rest_found": true}
	- utter_email_conf
* affirm
    - utter_email_id_ask
* restaurant_search{"email": "abc.def@gmail.com"}
    - slot{"email": "abc.def@gmail.com"}
    - action_sendemail
    - utter_email_sent
    - utter_goodbye
	- action_restart

## complete path with budget first and location false
* greet
    - utter_greet
* restaurant_search{"price": "medium"}
    - slot{"price": "medium"}
	- utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
	- action_chklocation
    - slot{"loc_avl": false}
	- utter_ask_location
* restaurant_search{"location": "delhi"}
	- slot{"location": "delhi"}
	- action_chklocation
    - slot{"loc_avl": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_chkcuisine
    - slot{"cusn_avl": true}
    - action_search_restaurants
    - slot{"emailbody": "Showing you top rated restaurants:Yauatcha in Level 5, 1 MG Lido Mall, MG Road, Bangalore has been rated 4.7\n And the average price for two people is: 2000\nThe Fatty Bao - Asian Gastro Bar in 610, 3rd Floor, 12th Main, Off 80 Feet Road, Indiranagar, Bangalore has been rated 4.6\n And the average price for two people is: 1200\nHae Kum Gang in 20, Pauls Castle, Castle Street, Ashok Nagar, Brigade Road, Bangalore has been rated 4.6\n And the average price for two people is: 1100\nHigh Ultra Lounge in 26/1, 31st Floor, Dr. Rajkumar Road, World Trade Centre, Brigade Gateway Campus, Malleshwaram, Bangalore has been rated 4.4\n And the average price for two people is: 2600\nChina Pearl in 53/1, 5th Cross, Koramangala 6th Block, Bangalore has been rated 4.4\n And the average price for two people is: 1100\nMamagoto in 949, 12th Main, Ground Floor, Off 100 Feet Road, Indiranagar, Bangalore has been rated 4.3\n And the average price for two people is: 2000\nSriracha in 204, 2nd Level, 4th Floor, Comet Block, UB City, Vittal Mallya Road, Lavelle Road, Bangalore has been rated 4.3\n And the average price for two people is: 1500\nThe Lantern Restaurant & Bar - The Ritz-Carlton, Bangalore in The Ritz-Carlton, 99, Residency Road, Bangalore has been rated 4.3\n And the average price for two people is: 3500\nBangalore Mandarin in 196, 3rd Floor, Double Road, Indiranagar, Bangalore has been rated 4.3\n And the average price for two people is: 1100\nKitchen On Table in Gate 9, P.A.E. Canteen, Bellary Road, Palace Ground, Sadashiv Nagar, Bangalore has been rated 4.2\n And the average price for two people is: 1500\n"}
    - slot{"rest_found": true}
	- utter_email_conf
* affirm
    - utter_email_id_ask
* restaurant_search{"email": "abc.def@gmail.com"}
    - slot{"email": "abc.def@gmail.com"}
    - action_sendemail
    - utter_email_sent
    - utter_goodbye
	- action_restart
	
## complete path with 2 entities location and cuisine
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "delhi"}
    - slot{"cuisine": "chinese"}
    - action_chkcuisine
    - slot{"cusn_avl": true}
    - slot{"location": "delhi"}
    - action_chklocation
    - slot{"loc_avl": true}
    - utter_ask_budget
* restaurant_search{"price": "medium"}
    - slot{"price": "medium"}
    - action_search_restaurants
    - slot{"emailbody": "Showing you top rated restaurants:Yauatcha in Level 5, 1 MG Lido Mall, MG Road, Bangalore has been rated 4.7\n And the average price for two people is: 2000\nThe Fatty Bao - Asian Gastro Bar in 610, 3rd Floor, 12th Main, Off 80 Feet Road, Indiranagar, Bangalore has been rated 4.6\n And the average price for two people is: 1200\nHae Kum Gang in 20, Pauls Castle, Castle Street, Ashok Nagar, Brigade Road, Bangalore has been rated 4.6\n And the average price for two people is: 1100\nHigh Ultra Lounge in 26/1, 31st Floor, Dr. Rajkumar Road, World Trade Centre, Brigade Gateway Campus, Malleshwaram, Bangalore has been rated 4.4\n And the average price for two people is: 2600\nChina Pearl in 53/1, 5th Cross, Koramangala 6th Block, Bangalore has been rated 4.4\n And the average price for two people is: 1100\nMamagoto in 949, 12th Main, Ground Floor, Off 100 Feet Road, Indiranagar, Bangalore has been rated 4.3\n And the average price for two people is: 2000\nSriracha in 204, 2nd Level, 4th Floor, Comet Block, UB City, Vittal Mallya Road, Lavelle Road, Bangalore has been rated 4.3\n And the average price for two people is: 1500\nThe Lantern Restaurant & Bar - The Ritz-Carlton, Bangalore in The Ritz-Carlton, 99, Residency Road, Bangalore has been rated 4.3\n And the average price for two people is: 3500\nBangalore Mandarin in 196, 3rd Floor, Double Road, Indiranagar, Bangalore has been rated 4.3\n And the average price for two people is: 1100\nKitchen On Table in Gate 9, P.A.E. Canteen, Bellary Road, Palace Ground, Sadashiv Nagar, Bangalore has been rated 4.2\n And the average price for two people is: 1500\n"}
    - slot{"rest_found": true}
	- utter_email_conf
* affirm
    - utter_email_id_ask
* restaurant_search{"email": "abc.def@gmail.com"}
    - slot{"email": "abc.def@gmail.com"}
    - action_sendemail
    - utter_email_sent
    - utter_goodbye
	- action_restart

## complete path with 2 entities location and cuisine false
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "delhi"}
    - slot{"location": "delhi"}
    - slot{"cuisine": "chinese"}
	- action_chklocation
    - slot{"loc_avl": true}
	- action_chkcuisine
    - slot{"cusn_avl": false}
	- utter_ask_cuisine
* restaurant_search{"cuisine": "chinese", "location": "delhi"}
    - slot{"cuisine": "chinese"}
	- slot{"cusn_avl": true}
    - utter_ask_budget
* restaurant_search{"price": "medium"}
    - slot{"price": "medium"}
    - action_search_restaurants
    - slot{"emailbody": "Showing you top rated restaurants:Yauatcha in Level 5, 1 MG Lido Mall, MG Road, Bangalore has been rated 4.7\n And the average price for two people is: 2000\nThe Fatty Bao - Asian Gastro Bar in 610, 3rd Floor, 12th Main, Off 80 Feet Road, Indiranagar, Bangalore has been rated 4.6\n And the average price for two people is: 1200\nHae Kum Gang in 20, Pauls Castle, Castle Street, Ashok Nagar, Brigade Road, Bangalore has been rated 4.6\n And the average price for two people is: 1100\nHigh Ultra Lounge in 26/1, 31st Floor, Dr. Rajkumar Road, World Trade Centre, Brigade Gateway Campus, Malleshwaram, Bangalore has been rated 4.4\n And the average price for two people is: 2600\nChina Pearl in 53/1, 5th Cross, Koramangala 6th Block, Bangalore has been rated 4.4\n And the average price for two people is: 1100\nMamagoto in 949, 12th Main, Ground Floor, Off 100 Feet Road, Indiranagar, Bangalore has been rated 4.3\n And the average price for two people is: 2000\nSriracha in 204, 2nd Level, 4th Floor, Comet Block, UB City, Vittal Mallya Road, Lavelle Road, Bangalore has been rated 4.3\n And the average price for two people is: 1500\nThe Lantern Restaurant & Bar - The Ritz-Carlton, Bangalore in The Ritz-Carlton, 99, Residency Road, Bangalore has been rated 4.3\n And the average price for two people is: 3500\nBangalore Mandarin in 196, 3rd Floor, Double Road, Indiranagar, Bangalore has been rated 4.3\n And the average price for two people is: 1100\nKitchen On Table in Gate 9, P.A.E. Canteen, Bellary Road, Palace Ground, Sadashiv Nagar, Bangalore has been rated 4.2\n And the average price for two people is: 1500\n"}
    - slot{"rest_found": true}
	- utter_email_conf
* affirm
    - utter_email_id_ask
* restaurant_search{"email": "abc.def@gmail.com"}
    - slot{"email": "abc.def@gmail.com"}
    - action_sendemail
    - utter_email_sent
    - utter_goodbye
	- action_restart
	
## complete path with 2 entities location and budget
* greet
    - utter_greet
* restaurant_search{"price": "medium", "location": "delhi"}
    - slot{"price": "medium"}
    - slot{"location": "delhi"}
    - action_chklocation
    - slot{"loc_avl": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese", "location": "delhi"}
    - slot{"cuisine": "chinese"}
    - action_chkcuisine
    - slot{"cusn_avl": true}
    - action_search_restaurants
    - slot{"emailbody": "Showing you top rated restaurants:Yauatcha in Level 5, 1 MG Lido Mall, MG Road, Bangalore has been rated 4.7\n And the average price for two people is: 2000\nThe Fatty Bao - Asian Gastro Bar in 610, 3rd Floor, 12th Main, Off 80 Feet Road, Indiranagar, Bangalore has been rated 4.6\n And the average price for two people is: 1200\nHae Kum Gang in 20, Pauls Castle, Castle Street, Ashok Nagar, Brigade Road, Bangalore has been rated 4.6\n And the average price for two people is: 1100\nHigh Ultra Lounge in 26/1, 31st Floor, Dr. Rajkumar Road, World Trade Centre, Brigade Gateway Campus, Malleshwaram, Bangalore has been rated 4.4\n And the average price for two people is: 2600\nChina Pearl in 53/1, 5th Cross, Koramangala 6th Block, Bangalore has been rated 4.4\n And the average price for two people is: 1100\nMamagoto in 949, 12th Main, Ground Floor, Off 100 Feet Road, Indiranagar, Bangalore has been rated 4.3\n And the average price for two people is: 2000\nSriracha in 204, 2nd Level, 4th Floor, Comet Block, UB City, Vittal Mallya Road, Lavelle Road, Bangalore has been rated 4.3\n And the average price for two people is: 1500\nThe Lantern Restaurant & Bar - The Ritz-Carlton, Bangalore in The Ritz-Carlton, 99, Residency Road, Bangalore has been rated 4.3\n And the average price for two people is: 3500\nBangalore Mandarin in 196, 3rd Floor, Double Road, Indiranagar, Bangalore has been rated 4.3\n And the average price for two people is: 1100\nKitchen On Table in Gate 9, P.A.E. Canteen, Bellary Road, Palace Ground, Sadashiv Nagar, Bangalore has been rated 4.2\n And the average price for two people is: 1500\n"}
    - slot{"rest_found": true}
	- utter_email_conf
* affirm
    - utter_email_id_ask
* restaurant_search{"email": "abc.def@gmail.com"}
    - slot{"email": "abc.def@gmail.com"}
    - action_sendemail
    - utter_email_sent
    - utter_goodbye
	- action_restart

## complete path with 2 entities cuisine and budget
* greet
    - utter_greet
* restaurant_search{"price": "medium", "cuisine": "chinese"}
    - slot{"price": "medium"}
	- slot{"cuisine": "chinese"}
    - action_chkcuisine
    - slot{"cusn_avl": true}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_chklocation
    - slot{"loc_avl": true}
    - action_search_restaurants
    - slot{"emailbody": "Showing you top rated restaurants:Yauatcha in Level 5, 1 MG Lido Mall, MG Road, Bangalore has been rated 4.7\n And the average price for two people is: 2000\nThe Fatty Bao - Asian Gastro Bar in 610, 3rd Floor, 12th Main, Off 80 Feet Road, Indiranagar, Bangalore has been rated 4.6\n And the average price for two people is: 1200\nHae Kum Gang in 20, Pauls Castle, Castle Street, Ashok Nagar, Brigade Road, Bangalore has been rated 4.6\n And the average price for two people is: 1100\nHigh Ultra Lounge in 26/1, 31st Floor, Dr. Rajkumar Road, World Trade Centre, Brigade Gateway Campus, Malleshwaram, Bangalore has been rated 4.4\n And the average price for two people is: 2600\nChina Pearl in 53/1, 5th Cross, Koramangala 6th Block, Bangalore has been rated 4.4\n And the average price for two people is: 1100\nMamagoto in 949, 12th Main, Ground Floor, Off 100 Feet Road, Indiranagar, Bangalore has been rated 4.3\n And the average price for two people is: 2000\nSriracha in 204, 2nd Level, 4th Floor, Comet Block, UB City, Vittal Mallya Road, Lavelle Road, Bangalore has been rated 4.3\n And the average price for two people is: 1500\nThe Lantern Restaurant & Bar - The Ritz-Carlton, Bangalore in The Ritz-Carlton, 99, Residency Road, Bangalore has been rated 4.3\n And the average price for two people is: 3500\nBangalore Mandarin in 196, 3rd Floor, Double Road, Indiranagar, Bangalore has been rated 4.3\n And the average price for two people is: 1100\nKitchen On Table in Gate 9, P.A.E. Canteen, Bellary Road, Palace Ground, Sadashiv Nagar, Bangalore has been rated 4.2\n And the average price for two people is: 1500\n"}
    - slot{"rest_found": true}
	- utter_email_conf
* affirm
    - utter_email_id_ask
* restaurant_search{"email": "abc.def@gmail.com"}
    - slot{"email": "abc.def@gmail.com"}
    - action_sendemail
    - utter_email_sent
    - utter_goodbye
	- action_restart

## complete path with 2 entities cuisine and budget
* greet
    - utter_greet
* restaurant_search{"price": "medium", "cuisine": "chinese"}
    - slot{"price": "medium"}
	- slot{"cuisine": "chinese"}
    - action_chkcuisine
    - slot{"cusn_avl": false}
	- utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_chkcuisine
    - slot{"cusn_avl": true}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_chklocation
    - slot{"loc_avl": true}
    - action_search_restaurants
    - slot{"emailbody": "Showing you top rated restaurants:Yauatcha in Level 5, 1 MG Lido Mall, MG Road, Bangalore has been rated 4.7\n And the average price for two people is: 2000\nThe Fatty Bao - Asian Gastro Bar in 610, 3rd Floor, 12th Main, Off 80 Feet Road, Indiranagar, Bangalore has been rated 4.6\n And the average price for two people is: 1200\nHae Kum Gang in 20, Pauls Castle, Castle Street, Ashok Nagar, Brigade Road, Bangalore has been rated 4.6\n And the average price for two people is: 1100\nHigh Ultra Lounge in 26/1, 31st Floor, Dr. Rajkumar Road, World Trade Centre, Brigade Gateway Campus, Malleshwaram, Bangalore has been rated 4.4\n And the average price for two people is: 2600\nChina Pearl in 53/1, 5th Cross, Koramangala 6th Block, Bangalore has been rated 4.4\n And the average price for two people is: 1100\nMamagoto in 949, 12th Main, Ground Floor, Off 100 Feet Road, Indiranagar, Bangalore has been rated 4.3\n And the average price for two people is: 2000\nSriracha in 204, 2nd Level, 4th Floor, Comet Block, UB City, Vittal Mallya Road, Lavelle Road, Bangalore has been rated 4.3\n And the average price for two people is: 1500\nThe Lantern Restaurant & Bar - The Ritz-Carlton, Bangalore in The Ritz-Carlton, 99, Residency Road, Bangalore has been rated 4.3\n And the average price for two people is: 3500\nBangalore Mandarin in 196, 3rd Floor, Double Road, Indiranagar, Bangalore has been rated 4.3\n And the average price for two people is: 1100\nKitchen On Table in Gate 9, P.A.E. Canteen, Bellary Road, Palace Ground, Sadashiv Nagar, Bangalore has been rated 4.2\n And the average price for two people is: 1500\n"}
    - slot{"rest_found": true}
	- utter_email_conf
* affirm
    - utter_email_id_ask
* restaurant_search{"email": "abc.def@gmail.com"}
    - slot{"email": "abc.def@gmail.com"}
    - action_sendemail
    - utter_email_sent
    - utter_goodbye
	- action_restart
	
## happy path 1
* restaurant_search{"cuisine": "chinese", "location": "delhi","price": "medium"}
    - slot{"cuisine": "chinese"}
    - action_chkcuisine
    - slot{"cusn_avl": true}
    - slot{"location": "delhi"}
    - slot{"price": "medium"}
	- action_chklocation
    - slot{"loc_avl": true}
    - action_search_restaurants
    - slot{"emailbody": "Showing you top rated restaurants:Yauatcha in Level 5, 1 MG Lido Mall, MG Road, Bangalore has been rated 4.7\n And the average price for two people is: 2000\nThe Fatty Bao - Asian Gastro Bar in 610, 3rd Floor, 12th Main, Off 80 Feet Road, Indiranagar, Bangalore has been rated 4.6\n And the average price for two people is: 1200\nHae Kum Gang in 20, Pauls Castle, Castle Street, Ashok Nagar, Brigade Road, Bangalore has been rated 4.6\n And the average price for two people is: 1100\nHigh Ultra Lounge in 26/1, 31st Floor, Dr. Rajkumar Road, World Trade Centre, Brigade Gateway Campus, Malleshwaram, Bangalore has been rated 4.4\n And the average price for two people is: 2600\nChina Pearl in 53/1, 5th Cross, Koramangala 6th Block, Bangalore has been rated 4.4\n And the average price for two people is: 1100\nMamagoto in 949, 12th Main, Ground Floor, Off 100 Feet Road, Indiranagar, Bangalore has been rated 4.3\n And the average price for two people is: 2000\nSriracha in 204, 2nd Level, 4th Floor, Comet Block, UB City, Vittal Mallya Road, Lavelle Road, Bangalore has been rated 4.3\n And the average price for two people is: 1500\nThe Lantern Restaurant & Bar - The Ritz-Carlton, Bangalore in The Ritz-Carlton, 99, Residency Road, Bangalore has been rated 4.3\n And the average price for two people is: 3500\nBangalore Mandarin in 196, 3rd Floor, Double Road, Indiranagar, Bangalore has been rated 4.3\n And the average price for two people is: 1100\nKitchen On Table in Gate 9, P.A.E. Canteen, Bellary Road, Palace Ground, Sadashiv Nagar, Bangalore has been rated 4.2\n And the average price for two people is: 1500\n"}
    - slot{"rest_found": true}
	- utter_email_conf
* affirm
    - utter_email_id_ask
* restaurant_search{"email": "abc.def@gmail.com"}
    - slot{"email": "abc.def@gmail.com"}
    - action_sendemail
    - utter_email_sent
    - utter_goodbye
	- action_restart
	
## complete path with location true 1 deny
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_chklocation
    - slot{"loc_avl": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_chkcuisine
    - slot{"cusn_avl": true}
    - utter_ask_budget
* restaurant_search{"price": "medium"}
    - slot{"price": "medium"}
    - action_search_restaurants
    - slot{"emailbody": "Showing you top rated restaurants:Yauatcha in Level 5, 1 MG Lido Mall, MG Road, Bangalore has been rated 4.7\n And the average price for two people is: 2000\nThe Fatty Bao - Asian Gastro Bar in 610, 3rd Floor, 12th Main, Off 80 Feet Road, Indiranagar, Bangalore has been rated 4.6\n And the average price for two people is: 1200\nHae Kum Gang in 20, Pauls Castle, Castle Street, Ashok Nagar, Brigade Road, Bangalore has been rated 4.6\n And the average price for two people is: 1100\nHigh Ultra Lounge in 26/1, 31st Floor, Dr. Rajkumar Road, World Trade Centre, Brigade Gateway Campus, Malleshwaram, Bangalore has been rated 4.4\n And the average price for two people is: 2600\nChina Pearl in 53/1, 5th Cross, Koramangala 6th Block, Bangalore has been rated 4.4\n And the average price for two people is: 1100\nMamagoto in 949, 12th Main, Ground Floor, Off 100 Feet Road, Indiranagar, Bangalore has been rated 4.3\n And the average price for two people is: 2000\nSriracha in 204, 2nd Level, 4th Floor, Comet Block, UB City, Vittal Mallya Road, Lavelle Road, Bangalore has been rated 4.3\n And the average price for two people is: 1500\nThe Lantern Restaurant & Bar - The Ritz-Carlton, Bangalore in The Ritz-Carlton, 99, Residency Road, Bangalore has been rated 4.3\n And the average price for two people is: 3500\nBangalore Mandarin in 196, 3rd Floor, Double Road, Indiranagar, Bangalore has been rated 4.3\n And the average price for two people is: 1100\nKitchen On Table in Gate 9, P.A.E. Canteen, Bellary Road, Palace Ground, Sadashiv Nagar, Bangalore has been rated 4.2\n And the average price for two people is: 1500\n"}
    - slot{"rest_found": true}
	- utter_email_conf
* deny
    - utter_goodbye
	- action_restart

## complete path with location true 1 and cusiine false 2 deny
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_chklocation
    - slot{"loc_avl": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_chkcuisine
    - slot{"cusn_avl": false}
	- utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_chkcuisine
    - slot{"cusn_avl": true}
    - utter_ask_budget
* restaurant_search{"price": "medium"}
    - slot{"price": "medium"}
    - action_search_restaurants
    - slot{"emailbody": "Showing you top rated restaurants:Yauatcha in Level 5, 1 MG Lido Mall, MG Road, Bangalore has been rated 4.7\n And the average price for two people is: 2000\nThe Fatty Bao - Asian Gastro Bar in 610, 3rd Floor, 12th Main, Off 80 Feet Road, Indiranagar, Bangalore has been rated 4.6\n And the average price for two people is: 1200\nHae Kum Gang in 20, Pauls Castle, Castle Street, Ashok Nagar, Brigade Road, Bangalore has been rated 4.6\n And the average price for two people is: 1100\nHigh Ultra Lounge in 26/1, 31st Floor, Dr. Rajkumar Road, World Trade Centre, Brigade Gateway Campus, Malleshwaram, Bangalore has been rated 4.4\n And the average price for two people is: 2600\nChina Pearl in 53/1, 5th Cross, Koramangala 6th Block, Bangalore has been rated 4.4\n And the average price for two people is: 1100\nMamagoto in 949, 12th Main, Ground Floor, Off 100 Feet Road, Indiranagar, Bangalore has been rated 4.3\n And the average price for two people is: 2000\nSriracha in 204, 2nd Level, 4th Floor, Comet Block, UB City, Vittal Mallya Road, Lavelle Road, Bangalore has been rated 4.3\n And the average price for two people is: 1500\nThe Lantern Restaurant & Bar - The Ritz-Carlton, Bangalore in The Ritz-Carlton, 99, Residency Road, Bangalore has been rated 4.3\n And the average price for two people is: 3500\nBangalore Mandarin in 196, 3rd Floor, Double Road, Indiranagar, Bangalore has been rated 4.3\n And the average price for two people is: 1100\nKitchen On Table in Gate 9, P.A.E. Canteen, Bellary Road, Palace Ground, Sadashiv Nagar, Bangalore has been rated 4.2\n And the average price for two people is: 1500\n"}
    - slot{"rest_found": true}
	- utter_email_conf
* deny
    - utter_goodbye
	- action_restart
	
## complete path with location false 1 deny
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_chklocation
    - slot{"loc_avl": false}
    - utter_goodbye
	- action_restart

## complete path with cuisine first 1 deny
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_chkcuisine
    - slot{"cusn_avl": true}
	- utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_chklocation
    - slot{"loc_avl": true}
    - utter_ask_budget
* restaurant_search{"price": "medium"}
    - slot{"price": "medium"}
    - action_search_restaurants
    - slot{"emailbody": "Showing you top rated restaurants:Yauatcha in Level 5, 1 MG Lido Mall, MG Road, Bangalore has been rated 4.7\n And the average price for two people is: 2000\nThe Fatty Bao - Asian Gastro Bar in 610, 3rd Floor, 12th Main, Off 80 Feet Road, Indiranagar, Bangalore has been rated 4.6\n And the average price for two people is: 1200\nHae Kum Gang in 20, Pauls Castle, Castle Street, Ashok Nagar, Brigade Road, Bangalore has been rated 4.6\n And the average price for two people is: 1100\nHigh Ultra Lounge in 26/1, 31st Floor, Dr. Rajkumar Road, World Trade Centre, Brigade Gateway Campus, Malleshwaram, Bangalore has been rated 4.4\n And the average price for two people is: 2600\nChina Pearl in 53/1, 5th Cross, Koramangala 6th Block, Bangalore has been rated 4.4\n And the average price for two people is: 1100\nMamagoto in 949, 12th Main, Ground Floor, Off 100 Feet Road, Indiranagar, Bangalore has been rated 4.3\n And the average price for two people is: 2000\nSriracha in 204, 2nd Level, 4th Floor, Comet Block, UB City, Vittal Mallya Road, Lavelle Road, Bangalore has been rated 4.3\n And the average price for two people is: 1500\nThe Lantern Restaurant & Bar - The Ritz-Carlton, Bangalore in The Ritz-Carlton, 99, Residency Road, Bangalore has been rated 4.3\n And the average price for two people is: 3500\nBangalore Mandarin in 196, 3rd Floor, Double Road, Indiranagar, Bangalore has been rated 4.3\n And the average price for two people is: 1100\nKitchen On Table in Gate 9, P.A.E. Canteen, Bellary Road, Palace Ground, Sadashiv Nagar, Bangalore has been rated 4.2\n And the average price for two people is: 1500\n"}
    - slot{"rest_found": true}
	- utter_email_conf
* deny
    - utter_goodbye
	- action_restart

## complete path with budget first deny
* greet
    - utter_greet
* restaurant_search{"price": "medium"}
    - slot{"price": "medium"}
	- utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_chklocation
    - slot{"loc_avl": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_chkcuisine
    - slot{"cusn_avl": true}
    - action_search_restaurants
    - slot{"emailbody": "Showing you top rated restaurants:Yauatcha in Level 5, 1 MG Lido Mall, MG Road, Bangalore has been rated 4.7\n And the average price for two people is: 2000\nThe Fatty Bao - Asian Gastro Bar in 610, 3rd Floor, 12th Main, Off 80 Feet Road, Indiranagar, Bangalore has been rated 4.6\n And the average price for two people is: 1200\nHae Kum Gang in 20, Pauls Castle, Castle Street, Ashok Nagar, Brigade Road, Bangalore has been rated 4.6\n And the average price for two people is: 1100\nHigh Ultra Lounge in 26/1, 31st Floor, Dr. Rajkumar Road, World Trade Centre, Brigade Gateway Campus, Malleshwaram, Bangalore has been rated 4.4\n And the average price for two people is: 2600\nChina Pearl in 53/1, 5th Cross, Koramangala 6th Block, Bangalore has been rated 4.4\n And the average price for two people is: 1100\nMamagoto in 949, 12th Main, Ground Floor, Off 100 Feet Road, Indiranagar, Bangalore has been rated 4.3\n And the average price for two people is: 2000\nSriracha in 204, 2nd Level, 4th Floor, Comet Block, UB City, Vittal Mallya Road, Lavelle Road, Bangalore has been rated 4.3\n And the average price for two people is: 1500\nThe Lantern Restaurant & Bar - The Ritz-Carlton, Bangalore in The Ritz-Carlton, 99, Residency Road, Bangalore has been rated 4.3\n And the average price for two people is: 3500\nBangalore Mandarin in 196, 3rd Floor, Double Road, Indiranagar, Bangalore has been rated 4.3\n And the average price for two people is: 1100\nKitchen On Table in Gate 9, P.A.E. Canteen, Bellary Road, Palace Ground, Sadashiv Nagar, Bangalore has been rated 4.2\n And the average price for two people is: 1500\n"}
    - slot{"rest_found": true}
	- utter_email_conf
* deny
    - utter_goodbye
	- action_restart

## complete path with 2 entities location and cuisine deny
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "delhi"}
    - slot{"cuisine": "chinese"}
    - action_chkcuisine
    - slot{"cusn_avl": true}
    - slot{"location": "delhi"}
    - action_chklocation
    - slot{"loc_avl": true}
    - utter_ask_budget
* restaurant_search{"price": "medium"}
    - slot{"price": "medium"}
    - action_search_restaurants
    - slot{"emailbody": "Showing you top rated restaurants:Yauatcha in Level 5, 1 MG Lido Mall, MG Road, Bangalore has been rated 4.7\n And the average price for two people is: 2000\nThe Fatty Bao - Asian Gastro Bar in 610, 3rd Floor, 12th Main, Off 80 Feet Road, Indiranagar, Bangalore has been rated 4.6\n And the average price for two people is: 1200\nHae Kum Gang in 20, Pauls Castle, Castle Street, Ashok Nagar, Brigade Road, Bangalore has been rated 4.6\n And the average price for two people is: 1100\nHigh Ultra Lounge in 26/1, 31st Floor, Dr. Rajkumar Road, World Trade Centre, Brigade Gateway Campus, Malleshwaram, Bangalore has been rated 4.4\n And the average price for two people is: 2600\nChina Pearl in 53/1, 5th Cross, Koramangala 6th Block, Bangalore has been rated 4.4\n And the average price for two people is: 1100\nMamagoto in 949, 12th Main, Ground Floor, Off 100 Feet Road, Indiranagar, Bangalore has been rated 4.3\n And the average price for two people is: 2000\nSriracha in 204, 2nd Level, 4th Floor, Comet Block, UB City, Vittal Mallya Road, Lavelle Road, Bangalore has been rated 4.3\n And the average price for two people is: 1500\nThe Lantern Restaurant & Bar - The Ritz-Carlton, Bangalore in The Ritz-Carlton, 99, Residency Road, Bangalore has been rated 4.3\n And the average price for two people is: 3500\nBangalore Mandarin in 196, 3rd Floor, Double Road, Indiranagar, Bangalore has been rated 4.3\n And the average price for two people is: 1100\nKitchen On Table in Gate 9, P.A.E. Canteen, Bellary Road, Palace Ground, Sadashiv Nagar, Bangalore has been rated 4.2\n And the average price for two people is: 1500\n"}
    - slot{"rest_found": true}
	- utter_email_conf
* deny
   - utter_goodbye
	- action_restart

## complete path with 2 entities location and budget deny
* greet
    - utter_greet
* restaurant_search{"price": "medium", "location": "delhi"}
    - slot{"price": "medium"}
    - slot{"location": "delhi"}
    - action_chklocation
    - slot{"loc_avl": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese", "location": "delhi"}
    - slot{"cuisine": "chinese"}
    - action_chkcuisine
    - slot{"cusn_avl": true}
    - action_search_restaurants
    - slot{"emailbody": "Showing you top rated restaurants:Yauatcha in Level 5, 1 MG Lido Mall, MG Road, Bangalore has been rated 4.7\n And the average price for two people is: 2000\nThe Fatty Bao - Asian Gastro Bar in 610, 3rd Floor, 12th Main, Off 80 Feet Road, Indiranagar, Bangalore has been rated 4.6\n And the average price for two people is: 1200\nHae Kum Gang in 20, Pauls Castle, Castle Street, Ashok Nagar, Brigade Road, Bangalore has been rated 4.6\n And the average price for two people is: 1100\nHigh Ultra Lounge in 26/1, 31st Floor, Dr. Rajkumar Road, World Trade Centre, Brigade Gateway Campus, Malleshwaram, Bangalore has been rated 4.4\n And the average price for two people is: 2600\nChina Pearl in 53/1, 5th Cross, Koramangala 6th Block, Bangalore has been rated 4.4\n And the average price for two people is: 1100\nMamagoto in 949, 12th Main, Ground Floor, Off 100 Feet Road, Indiranagar, Bangalore has been rated 4.3\n And the average price for two people is: 2000\nSriracha in 204, 2nd Level, 4th Floor, Comet Block, UB City, Vittal Mallya Road, Lavelle Road, Bangalore has been rated 4.3\n And the average price for two people is: 1500\nThe Lantern Restaurant & Bar - The Ritz-Carlton, Bangalore in The Ritz-Carlton, 99, Residency Road, Bangalore has been rated 4.3\n And the average price for two people is: 3500\nBangalore Mandarin in 196, 3rd Floor, Double Road, Indiranagar, Bangalore has been rated 4.3\n And the average price for two people is: 1100\nKitchen On Table in Gate 9, P.A.E. Canteen, Bellary Road, Palace Ground, Sadashiv Nagar, Bangalore has been rated 4.2\n And the average price for two people is: 1500\n"}
    - slot{"rest_found": true}
	- utter_email_conf
* deny
    - utter_goodbye
	- action_restart

## complete path with 2 entities cuisine and budget deny
* greet
    - utter_greet
* restaurant_search{"price": "medium", "location": "delhi"}
    - slot{"price": "medium"}
	- slot{"cuisine": "chinese"}
    - action_chkcuisine
    - slot{"cusn_avl": true}
    - slot{"loc_avl": true}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_chklocation
    - slot{"loc_avl": true}
    - action_search_restaurants
    - slot{"emailbody": "Showing you top rated restaurants:Yauatcha in Level 5, 1 MG Lido Mall, MG Road, Bangalore has been rated 4.7\n And the average price for two people is: 2000\nThe Fatty Bao - Asian Gastro Bar in 610, 3rd Floor, 12th Main, Off 80 Feet Road, Indiranagar, Bangalore has been rated 4.6\n And the average price for two people is: 1200\nHae Kum Gang in 20, Pauls Castle, Castle Street, Ashok Nagar, Brigade Road, Bangalore has been rated 4.6\n And the average price for two people is: 1100\nHigh Ultra Lounge in 26/1, 31st Floor, Dr. Rajkumar Road, World Trade Centre, Brigade Gateway Campus, Malleshwaram, Bangalore has been rated 4.4\n And the average price for two people is: 2600\nChina Pearl in 53/1, 5th Cross, Koramangala 6th Block, Bangalore has been rated 4.4\n And the average price for two people is: 1100\nMamagoto in 949, 12th Main, Ground Floor, Off 100 Feet Road, Indiranagar, Bangalore has been rated 4.3\n And the average price for two people is: 2000\nSriracha in 204, 2nd Level, 4th Floor, Comet Block, UB City, Vittal Mallya Road, Lavelle Road, Bangalore has been rated 4.3\n And the average price for two people is: 1500\nThe Lantern Restaurant & Bar - The Ritz-Carlton, Bangalore in The Ritz-Carlton, 99, Residency Road, Bangalore has been rated 4.3\n And the average price for two people is: 3500\nBangalore Mandarin in 196, 3rd Floor, Double Road, Indiranagar, Bangalore has been rated 4.3\n And the average price for two people is: 1100\nKitchen On Table in Gate 9, P.A.E. Canteen, Bellary Road, Palace Ground, Sadashiv Nagar, Bangalore has been rated 4.2\n And the average price for two people is: 1500\n"}
    - slot{"rest_found": true}
	- utter_email_conf
* deny
    - utter_goodbye
	- action_restart
	
## happy path 1 deny
* restaurant_search{"cuisine": "chinese", "location": "delhi","price": "medium"}
    - slot{"cuisine": "chinese"}
    - action_chkcuisine
    - slot{"cusn_avl": true}
    - slot{"location": "delhi"}
    - slot{"price": "medium"}
	- action_chklocation
    - slot{"loc_avl": true}
    - action_search_restaurants
    - slot{"emailbody": "Showing you top rated restaurants:Yauatcha in Level 5, 1 MG Lido Mall, MG Road, Bangalore has been rated 4.7\n And the average price for two people is: 2000\nThe Fatty Bao - Asian Gastro Bar in 610, 3rd Floor, 12th Main, Off 80 Feet Road, Indiranagar, Bangalore has been rated 4.6\n And the average price for two people is: 1200\nHae Kum Gang in 20, Pauls Castle, Castle Street, Ashok Nagar, Brigade Road, Bangalore has been rated 4.6\n And the average price for two people is: 1100\nHigh Ultra Lounge in 26/1, 31st Floor, Dr. Rajkumar Road, World Trade Centre, Brigade Gateway Campus, Malleshwaram, Bangalore has been rated 4.4\n And the average price for two people is: 2600\nChina Pearl in 53/1, 5th Cross, Koramangala 6th Block, Bangalore has been rated 4.4\n And the average price for two people is: 1100\nMamagoto in 949, 12th Main, Ground Floor, Off 100 Feet Road, Indiranagar, Bangalore has been rated 4.3\n And the average price for two people is: 2000\nSriracha in 204, 2nd Level, 4th Floor, Comet Block, UB City, Vittal Mallya Road, Lavelle Road, Bangalore has been rated 4.3\n And the average price for two people is: 1500\nThe Lantern Restaurant & Bar - The Ritz-Carlton, Bangalore in The Ritz-Carlton, 99, Residency Road, Bangalore has been rated 4.3\n And the average price for two people is: 3500\nBangalore Mandarin in 196, 3rd Floor, Double Road, Indiranagar, Bangalore has been rated 4.3\n And the average price for two people is: 1100\nKitchen On Table in Gate 9, P.A.E. Canteen, Bellary Road, Palace Ground, Sadashiv Nagar, Bangalore has been rated 4.2\n And the average price for two people is: 1500\n"}
    - slot{"rest_found": true}
	- utter_email_conf
* deny
    - utter_goodbye
	- action_restart

## complete path with location true 1 without affirm
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_chklocation
    - slot{"loc_avl": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_chkcuisine
    - slot{"cusn_avl": true}
    - utter_ask_budget
* restaurant_search{"price": "medium"}
    - slot{"price": "medium"}
    - action_search_restaurants
    - slot{"emailbody": "Showing you top rated restaurants:Yauatcha in Level 5, 1 MG Lido Mall, MG Road, Bangalore has been rated 4.7\n And the average price for two people is: 2000\nThe Fatty Bao - Asian Gastro Bar in 610, 3rd Floor, 12th Main, Off 80 Feet Road, Indiranagar, Bangalore has been rated 4.6\n And the average price for two people is: 1200\nHae Kum Gang in 20, Pauls Castle, Castle Street, Ashok Nagar, Brigade Road, Bangalore has been rated 4.6\n And the average price for two people is: 1100\nHigh Ultra Lounge in 26/1, 31st Floor, Dr. Rajkumar Road, World Trade Centre, Brigade Gateway Campus, Malleshwaram, Bangalore has been rated 4.4\n And the average price for two people is: 2600\nChina Pearl in 53/1, 5th Cross, Koramangala 6th Block, Bangalore has been rated 4.4\n And the average price for two people is: 1100\nMamagoto in 949, 12th Main, Ground Floor, Off 100 Feet Road, Indiranagar, Bangalore has been rated 4.3\n And the average price for two people is: 2000\nSriracha in 204, 2nd Level, 4th Floor, Comet Block, UB City, Vittal Mallya Road, Lavelle Road, Bangalore has been rated 4.3\n And the average price for two people is: 1500\nThe Lantern Restaurant & Bar - The Ritz-Carlton, Bangalore in The Ritz-Carlton, 99, Residency Road, Bangalore has been rated 4.3\n And the average price for two people is: 3500\nBangalore Mandarin in 196, 3rd Floor, Double Road, Indiranagar, Bangalore has been rated 4.3\n And the average price for two people is: 1100\nKitchen On Table in Gate 9, P.A.E. Canteen, Bellary Road, Palace Ground, Sadashiv Nagar, Bangalore has been rated 4.2\n And the average price for two people is: 1500\n"}
    - slot{"rest_found": true}
	- utter_email_conf
* restaurant_search{"email": "abc.def@gmail.com"}
    - slot{"email": "abc.def@gmail.com"}
    - action_sendemail
    - utter_email_sent
    - utter_goodbye
	- action_restart
	
## complete path with location false 1  without affirm
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_chklocation
    - slot{"loc_avl": false}
    - utter_goodbye
	- action_restart

## complete path with cuisine first 1  without affirm
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_chkcuisine
    - slot{"cusn_avl": true}
	- utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_chklocation
    - slot{"loc_avl": true}
    - utter_ask_budget
* restaurant_search{"price": "medium"}
    - slot{"price": "medium"}
    - action_search_restaurants
    - slot{"emailbody": "Showing you top rated restaurants:Yauatcha in Level 5, 1 MG Lido Mall, MG Road, Bangalore has been rated 4.7\n And the average price for two people is: 2000\nThe Fatty Bao - Asian Gastro Bar in 610, 3rd Floor, 12th Main, Off 80 Feet Road, Indiranagar, Bangalore has been rated 4.6\n And the average price for two people is: 1200\nHae Kum Gang in 20, Pauls Castle, Castle Street, Ashok Nagar, Brigade Road, Bangalore has been rated 4.6\n And the average price for two people is: 1100\nHigh Ultra Lounge in 26/1, 31st Floor, Dr. Rajkumar Road, World Trade Centre, Brigade Gateway Campus, Malleshwaram, Bangalore has been rated 4.4\n And the average price for two people is: 2600\nChina Pearl in 53/1, 5th Cross, Koramangala 6th Block, Bangalore has been rated 4.4\n And the average price for two people is: 1100\nMamagoto in 949, 12th Main, Ground Floor, Off 100 Feet Road, Indiranagar, Bangalore has been rated 4.3\n And the average price for two people is: 2000\nSriracha in 204, 2nd Level, 4th Floor, Comet Block, UB City, Vittal Mallya Road, Lavelle Road, Bangalore has been rated 4.3\n And the average price for two people is: 1500\nThe Lantern Restaurant & Bar - The Ritz-Carlton, Bangalore in The Ritz-Carlton, 99, Residency Road, Bangalore has been rated 4.3\n And the average price for two people is: 3500\nBangalore Mandarin in 196, 3rd Floor, Double Road, Indiranagar, Bangalore has been rated 4.3\n And the average price for two people is: 1100\nKitchen On Table in Gate 9, P.A.E. Canteen, Bellary Road, Palace Ground, Sadashiv Nagar, Bangalore has been rated 4.2\n And the average price for two people is: 1500\n"}
    - slot{"rest_found": true}
	- utter_email_conf
* restaurant_search{"email": "abc.def@gmail.com"}
    - slot{"email": "abc.def@gmail.com"}
    - action_sendemail
    - utter_email_sent
    - utter_goodbye
	- action_restart

## complete path with budget first without affirm
* greet
    - utter_greet
* restaurant_search{"price": "medium"}
    - slot{"price": "medium"}
	- utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_chklocation
    - slot{"loc_avl": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_chkcuisine
    - slot{"cusn_avl": true}
    - action_search_restaurants
    - slot{"emailbody": "Showing you top rated restaurants:Yauatcha in Level 5, 1 MG Lido Mall, MG Road, Bangalore has been rated 4.7\n And the average price for two people is: 2000\nThe Fatty Bao - Asian Gastro Bar in 610, 3rd Floor, 12th Main, Off 80 Feet Road, Indiranagar, Bangalore has been rated 4.6\n And the average price for two people is: 1200\nHae Kum Gang in 20, Pauls Castle, Castle Street, Ashok Nagar, Brigade Road, Bangalore has been rated 4.6\n And the average price for two people is: 1100\nHigh Ultra Lounge in 26/1, 31st Floor, Dr. Rajkumar Road, World Trade Centre, Brigade Gateway Campus, Malleshwaram, Bangalore has been rated 4.4\n And the average price for two people is: 2600\nChina Pearl in 53/1, 5th Cross, Koramangala 6th Block, Bangalore has been rated 4.4\n And the average price for two people is: 1100\nMamagoto in 949, 12th Main, Ground Floor, Off 100 Feet Road, Indiranagar, Bangalore has been rated 4.3\n And the average price for two people is: 2000\nSriracha in 204, 2nd Level, 4th Floor, Comet Block, UB City, Vittal Mallya Road, Lavelle Road, Bangalore has been rated 4.3\n And the average price for two people is: 1500\nThe Lantern Restaurant & Bar - The Ritz-Carlton, Bangalore in The Ritz-Carlton, 99, Residency Road, Bangalore has been rated 4.3\n And the average price for two people is: 3500\nBangalore Mandarin in 196, 3rd Floor, Double Road, Indiranagar, Bangalore has been rated 4.3\n And the average price for two people is: 1100\nKitchen On Table in Gate 9, P.A.E. Canteen, Bellary Road, Palace Ground, Sadashiv Nagar, Bangalore has been rated 4.2\n And the average price for two people is: 1500\n"}
    - slot{"rest_found": true}
	- utter_email_conf
* restaurant_search{"email": "abc.def@gmail.com"}
    - slot{"email": "abc.def@gmail.com"}
    - action_sendemail
    - utter_email_sent
    - utter_goodbye
	- action_restart

## complete path with 2 entities location and cuisine without affirm
* restaurant_search{"cuisine": "chinese", "location": "delhi"}
    - slot{"cuisine": "chinese"}
    - action_chkcuisine
    - slot{"cusn_avl": true}
    - slot{"location": "delhi"}
    - action_chklocation
    - slot{"loc_avl": true}
    - utter_ask_budget
* restaurant_search{"price": "medium"}
    - slot{"price": "medium"}
    - action_search_restaurants
    - slot{"emailbody": "Showing you top rated restaurants:Yauatcha in Level 5, 1 MG Lido Mall, MG Road, Bangalore has been rated 4.7\n And the average price for two people is: 2000\nThe Fatty Bao - Asian Gastro Bar in 610, 3rd Floor, 12th Main, Off 80 Feet Road, Indiranagar, Bangalore has been rated 4.6\n And the average price for two people is: 1200\nHae Kum Gang in 20, Pauls Castle, Castle Street, Ashok Nagar, Brigade Road, Bangalore has been rated 4.6\n And the average price for two people is: 1100\nHigh Ultra Lounge in 26/1, 31st Floor, Dr. Rajkumar Road, World Trade Centre, Brigade Gateway Campus, Malleshwaram, Bangalore has been rated 4.4\n And the average price for two people is: 2600\nChina Pearl in 53/1, 5th Cross, Koramangala 6th Block, Bangalore has been rated 4.4\n And the average price for two people is: 1100\nMamagoto in 949, 12th Main, Ground Floor, Off 100 Feet Road, Indiranagar, Bangalore has been rated 4.3\n And the average price for two people is: 2000\nSriracha in 204, 2nd Level, 4th Floor, Comet Block, UB City, Vittal Mallya Road, Lavelle Road, Bangalore has been rated 4.3\n And the average price for two people is: 1500\nThe Lantern Restaurant & Bar - The Ritz-Carlton, Bangalore in The Ritz-Carlton, 99, Residency Road, Bangalore has been rated 4.3\n And the average price for two people is: 3500\nBangalore Mandarin in 196, 3rd Floor, Double Road, Indiranagar, Bangalore has been rated 4.3\n And the average price for two people is: 1100\nKitchen On Table in Gate 9, P.A.E. Canteen, Bellary Road, Palace Ground, Sadashiv Nagar, Bangalore has been rated 4.2\n And the average price for two people is: 1500\n"}
    - slot{"rest_found": true}
	- utter_email_conf
* restaurant_search{"email": "abc.def@gmail.com"}
    - slot{"email": "abc.def@gmail.com"}
    - action_sendemail
    - utter_email_sent
    - utter_goodbye
	- action_restart

## complete path with 2 entities location and cuisine without affirm
* restaurant_search{"cuisine": "chinese", "location": "delhi"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - action_chklocation
    - slot{"loc_avl": true}
	- action_chkcuisine
    - slot{"cusn_avl": false}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese", "location": "delhi"}
    - slot{"cuisine": "chinese"}
    - action_chkcuisine
    - slot{"cusn_avl": true} 
    - utter_ask_budget
* restaurant_search{"price": "medium"}
    - slot{"price": "medium"}
    - action_search_restaurants
    - slot{"emailbody": "Showing you top rated restaurants:Yauatcha in Level 5, 1 MG Lido Mall, MG Road, Bangalore has been rated 4.7\n And the average price for two people is: 2000\nThe Fatty Bao - Asian Gastro Bar in 610, 3rd Floor, 12th Main, Off 80 Feet Road, Indiranagar, Bangalore has been rated 4.6\n And the average price for two people is: 1200\nHae Kum Gang in 20, Pauls Castle, Castle Street, Ashok Nagar, Brigade Road, Bangalore has been rated 4.6\n And the average price for two people is: 1100\nHigh Ultra Lounge in 26/1, 31st Floor, Dr. Rajkumar Road, World Trade Centre, Brigade Gateway Campus, Malleshwaram, Bangalore has been rated 4.4\n And the average price for two people is: 2600\nChina Pearl in 53/1, 5th Cross, Koramangala 6th Block, Bangalore has been rated 4.4\n And the average price for two people is: 1100\nMamagoto in 949, 12th Main, Ground Floor, Off 100 Feet Road, Indiranagar, Bangalore has been rated 4.3\n And the average price for two people is: 2000\nSriracha in 204, 2nd Level, 4th Floor, Comet Block, UB City, Vittal Mallya Road, Lavelle Road, Bangalore has been rated 4.3\n And the average price for two people is: 1500\nThe Lantern Restaurant & Bar - The Ritz-Carlton, Bangalore in The Ritz-Carlton, 99, Residency Road, Bangalore has been rated 4.3\n And the average price for two people is: 3500\nBangalore Mandarin in 196, 3rd Floor, Double Road, Indiranagar, Bangalore has been rated 4.3\n And the average price for two people is: 1100\nKitchen On Table in Gate 9, P.A.E. Canteen, Bellary Road, Palace Ground, Sadashiv Nagar, Bangalore has been rated 4.2\n And the average price for two people is: 1500\n"}
    - slot{"rest_found": true}
	- utter_email_conf
* restaurant_search{"email": "abc.def@gmail.com"}
    - slot{"email": "abc.def@gmail.com"}
    - action_sendemail
    - utter_email_sent
    - utter_goodbye
	- action_restart
	
## complete path with 2 entities location and budget without affirm
* greet
    - utter_greet
* restaurant_search{"price": "medium", "location": "delhi"}
    - slot{"price": "medium"}
    - slot{"location": "delhi"}
    - action_chklocation
    - slot{"loc_avl": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese", "location": "delhi"}
    - slot{"cuisine": "chinese"}
    - action_chkcuisine
    - slot{"cusn_avl": true}
    - action_search_restaurants
    - slot{"emailbody": "Showing you top rated restaurants:Yauatcha in Level 5, 1 MG Lido Mall, MG Road, Bangalore has been rated 4.7\n And the average price for two people is: 2000\nThe Fatty Bao - Asian Gastro Bar in 610, 3rd Floor, 12th Main, Off 80 Feet Road, Indiranagar, Bangalore has been rated 4.6\n And the average price for two people is: 1200\nHae Kum Gang in 20, Pauls Castle, Castle Street, Ashok Nagar, Brigade Road, Bangalore has been rated 4.6\n And the average price for two people is: 1100\nHigh Ultra Lounge in 26/1, 31st Floor, Dr. Rajkumar Road, World Trade Centre, Brigade Gateway Campus, Malleshwaram, Bangalore has been rated 4.4\n And the average price for two people is: 2600\nChina Pearl in 53/1, 5th Cross, Koramangala 6th Block, Bangalore has been rated 4.4\n And the average price for two people is: 1100\nMamagoto in 949, 12th Main, Ground Floor, Off 100 Feet Road, Indiranagar, Bangalore has been rated 4.3\n And the average price for two people is: 2000\nSriracha in 204, 2nd Level, 4th Floor, Comet Block, UB City, Vittal Mallya Road, Lavelle Road, Bangalore has been rated 4.3\n And the average price for two people is: 1500\nThe Lantern Restaurant & Bar - The Ritz-Carlton, Bangalore in The Ritz-Carlton, 99, Residency Road, Bangalore has been rated 4.3\n And the average price for two people is: 3500\nBangalore Mandarin in 196, 3rd Floor, Double Road, Indiranagar, Bangalore has been rated 4.3\n And the average price for two people is: 1100\nKitchen On Table in Gate 9, P.A.E. Canteen, Bellary Road, Palace Ground, Sadashiv Nagar, Bangalore has been rated 4.2\n And the average price for two people is: 1500\n"}
    - slot{"rest_found": true}
	- utter_email_conf
* restaurant_search{"email": "abc.def@gmail.com"}
    - slot{"email": "abc.def@gmail.com"}
    - action_sendemail
    - utter_email_sent
    - utter_goodbye
	- action_restart

## complete path with 2 entities location and budget without affirm
* greet
    - utter_greet
* restaurant_search{"price": "medium", "location": "delhi"}
    - slot{"price": "medium"}
    - slot{"location": "delhi"}
    - action_chklocation
    - slot{"loc_avl": false}
	- utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_chklocation
    - slot{"loc_avl": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese", "location": "delhi"}
    - slot{"cuisine": "chinese"}
    - action_chkcuisine
    - slot{"cusn_avl": true}
    - action_search_restaurants
    - slot{"emailbody": "Showing you top rated restaurants:Yauatcha in Level 5, 1 MG Lido Mall, MG Road, Bangalore has been rated 4.7\n And the average price for two people is: 2000\nThe Fatty Bao - Asian Gastro Bar in 610, 3rd Floor, 12th Main, Off 80 Feet Road, Indiranagar, Bangalore has been rated 4.6\n And the average price for two people is: 1200\nHae Kum Gang in 20, Pauls Castle, Castle Street, Ashok Nagar, Brigade Road, Bangalore has been rated 4.6\n And the average price for two people is: 1100\nHigh Ultra Lounge in 26/1, 31st Floor, Dr. Rajkumar Road, World Trade Centre, Brigade Gateway Campus, Malleshwaram, Bangalore has been rated 4.4\n And the average price for two people is: 2600\nChina Pearl in 53/1, 5th Cross, Koramangala 6th Block, Bangalore has been rated 4.4\n And the average price for two people is: 1100\nMamagoto in 949, 12th Main, Ground Floor, Off 100 Feet Road, Indiranagar, Bangalore has been rated 4.3\n And the average price for two people is: 2000\nSriracha in 204, 2nd Level, 4th Floor, Comet Block, UB City, Vittal Mallya Road, Lavelle Road, Bangalore has been rated 4.3\n And the average price for two people is: 1500\nThe Lantern Restaurant & Bar - The Ritz-Carlton, Bangalore in The Ritz-Carlton, 99, Residency Road, Bangalore has been rated 4.3\n And the average price for two people is: 3500\nBangalore Mandarin in 196, 3rd Floor, Double Road, Indiranagar, Bangalore has been rated 4.3\n And the average price for two people is: 1100\nKitchen On Table in Gate 9, P.A.E. Canteen, Bellary Road, Palace Ground, Sadashiv Nagar, Bangalore has been rated 4.2\n And the average price for two people is: 1500\n"}
    - slot{"rest_found": true}
	- utter_email_conf
* restaurant_search{"email": "abc.def@gmail.com"}
    - slot{"email": "abc.def@gmail.com"}
    - action_sendemail
    - utter_email_sent
    - utter_goodbye
	- action_restart

## complete path with 2 entities location and budget without affirm
* greet
    - utter_greet
* restaurant_search{"price": "low", "location": "delhi"}
    - slot{"price": "low"}
    - slot{"location": "delhi"}
    - action_chklocation
    - slot{"loc_avl": false}
	- utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_chklocation
    - slot{"loc_avl": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese", "location": "delhi"}
    - slot{"cuisine": "chinese"}
    - action_chkcuisine
    - slot{"cusn_avl": true}
    - action_search_restaurants
    - slot{"emailbody": "Showing you top rated restaurants:Yauatcha in Level 5, 1 MG Lido Mall, MG Road, Bangalore has been rated 4.7\n And the average price for two people is: 2000\nThe Fatty Bao - Asian Gastro Bar in 610, 3rd Floor, 12th Main, Off 80 Feet Road, Indiranagar, Bangalore has been rated 4.6\n And the average price for two people is: 1200\nHae Kum Gang in 20, Pauls Castle, Castle Street, Ashok Nagar, Brigade Road, Bangalore has been rated 4.6\n And the average price for two people is: 1100\nHigh Ultra Lounge in 26/1, 31st Floor, Dr. Rajkumar Road, World Trade Centre, Brigade Gateway Campus, Malleshwaram, Bangalore has been rated 4.4\n And the average price for two people is: 2600\nChina Pearl in 53/1, 5th Cross, Koramangala 6th Block, Bangalore has been rated 4.4\n And the average price for two people is: 1100\nMamagoto in 949, 12th Main, Ground Floor, Off 100 Feet Road, Indiranagar, Bangalore has been rated 4.3\n And the average price for two people is: 2000\nSriracha in 204, 2nd Level, 4th Floor, Comet Block, UB City, Vittal Mallya Road, Lavelle Road, Bangalore has been rated 4.3\n And the average price for two people is: 1500\nThe Lantern Restaurant & Bar - The Ritz-Carlton, Bangalore in The Ritz-Carlton, 99, Residency Road, Bangalore has been rated 4.3\n And the average price for two people is: 3500\nBangalore Mandarin in 196, 3rd Floor, Double Road, Indiranagar, Bangalore has been rated 4.3\n And the average price for two people is: 1100\nKitchen On Table in Gate 9, P.A.E. Canteen, Bellary Road, Palace Ground, Sadashiv Nagar, Bangalore has been rated 4.2\n And the average price for two people is: 1500\n"}
    - slot{"rest_found": true}
	- utter_email_conf
* deny
    - utter_goodbye
    - action_restart
	
## complete path with 2 entities cuisine and budget without affirm
* greet
    - utter_greet
* restaurant_search{"price": "medium", "cuisine": "chinese"}
    - slot{"price": "medium"}
	- slot{"cuisine": "chinese"}
    - action_chkcuisine
    - slot{"cusn_avl": true}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_chklocation
    - slot{"loc_avl": true}
    - action_search_restaurants
    - slot{"emailbody": "Showing you top rated restaurants:Yauatcha in Level 5, 1 MG Lido Mall, MG Road, Bangalore has been rated 4.7\n And the average price for two people is: 2000\nThe Fatty Bao - Asian Gastro Bar in 610, 3rd Floor, 12th Main, Off 80 Feet Road, Indiranagar, Bangalore has been rated 4.6\n And the average price for two people is: 1200\nHae Kum Gang in 20, Pauls Castle, Castle Street, Ashok Nagar, Brigade Road, Bangalore has been rated 4.6\n And the average price for two people is: 1100\nHigh Ultra Lounge in 26/1, 31st Floor, Dr. Rajkumar Road, World Trade Centre, Brigade Gateway Campus, Malleshwaram, Bangalore has been rated 4.4\n And the average price for two people is: 2600\nChina Pearl in 53/1, 5th Cross, Koramangala 6th Block, Bangalore has been rated 4.4\n And the average price for two people is: 1100\nMamagoto in 949, 12th Main, Ground Floor, Off 100 Feet Road, Indiranagar, Bangalore has been rated 4.3\n And the average price for two people is: 2000\nSriracha in 204, 2nd Level, 4th Floor, Comet Block, UB City, Vittal Mallya Road, Lavelle Road, Bangalore has been rated 4.3\n And the average price for two people is: 1500\nThe Lantern Restaurant & Bar - The Ritz-Carlton, Bangalore in The Ritz-Carlton, 99, Residency Road, Bangalore has been rated 4.3\n And the average price for two people is: 3500\nBangalore Mandarin in 196, 3rd Floor, Double Road, Indiranagar, Bangalore has been rated 4.3\n And the average price for two people is: 1100\nKitchen On Table in Gate 9, P.A.E. Canteen, Bellary Road, Palace Ground, Sadashiv Nagar, Bangalore has been rated 4.2\n And the average price for two people is: 1500\n"}
    - slot{"rest_found": true}
	- utter_email_conf
* restaurant_search{"email": "abc.def@gmail.com"}
    - slot{"email": "abc.def@gmail.com"}
    - action_sendemail
    - utter_email_sent
    - utter_goodbye
	- action_restart
	
## happy path 1 without affirm
* restaurant_search{"cuisine": "chinese", "location": "delhi","price": "medium"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - slot{"price": "medium"}
	- action_chklocation
    - slot{"loc_avl": true}
	- action_chkcuisine
    - slot{"cusn_avl": true}
    - action_search_restaurants
    - slot{"emailbody": "Showing you top rated restaurants:Yauatcha in Level 5, 1 MG Lido Mall, MG Road, Bangalore has been rated 4.7\n And the average price for two people is: 2000\nThe Fatty Bao - Asian Gastro Bar in 610, 3rd Floor, 12th Main, Off 80 Feet Road, Indiranagar, Bangalore has been rated 4.6\n And the average price for two people is: 1200\nHae Kum Gang in 20, Pauls Castle, Castle Street, Ashok Nagar, Brigade Road, Bangalore has been rated 4.6\n And the average price for two people is: 1100\nHigh Ultra Lounge in 26/1, 31st Floor, Dr. Rajkumar Road, World Trade Centre, Brigade Gateway Campus, Malleshwaram, Bangalore has been rated 4.4\n And the average price for two people is: 2600\nChina Pearl in 53/1, 5th Cross, Koramangala 6th Block, Bangalore has been rated 4.4\n And the average price for two people is: 1100\nMamagoto in 949, 12th Main, Ground Floor, Off 100 Feet Road, Indiranagar, Bangalore has been rated 4.3\n And the average price for two people is: 2000\nSriracha in 204, 2nd Level, 4th Floor, Comet Block, UB City, Vittal Mallya Road, Lavelle Road, Bangalore has been rated 4.3\n And the average price for two people is: 1500\nThe Lantern Restaurant & Bar - The Ritz-Carlton, Bangalore in The Ritz-Carlton, 99, Residency Road, Bangalore has been rated 4.3\n And the average price for two people is: 3500\nBangalore Mandarin in 196, 3rd Floor, Double Road, Indiranagar, Bangalore has been rated 4.3\n And the average price for two people is: 1100\nKitchen On Table in Gate 9, P.A.E. Canteen, Bellary Road, Palace Ground, Sadashiv Nagar, Bangalore has been rated 4.2\n And the average price for two people is: 1500\n"}
    - slot{"rest_found": true}
	- utter_email_conf
* restaurant_search{"email": "abc.def@gmail.com"}
    - slot{"email": "abc.def@gmail.com"}
    - action_sendemail
    - utter_email_sent
    - utter_goodbye
	- action_restart


## interactive_story_1
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_chkcuisine
    - slot{"cusn_avl": true}
    - utter_ask_location
* restaurant_search{"location": "jayanagar"}
    - slot{"location": "jayanagar"}
    - action_chklocation
    - slot{"loc_avl": false}
    - utter_ask_location
* restaurant_search{"location": "Delhi"}
    - slot{"location": "Delhi"}
    - action_chklocation
    - slot{"loc_avl": true}
    - utter_ask_budget
* greet{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - slot{"emailbody": "Showing you top rated restaurants:\nPa Pa Ya in A-3, Select Citywalk, District Centre, Saket, New Delhi has been rated 4.9. And the average price for two people is: 2500\nPlum By Bent Chair in Ground Floor, Worldmark 2, Aerocity, New Delhi has been rated 4.6. And the average price for two people is: 2200\nHonk - Pullman New Delhi Aerocity in Pullman New Delhi Aerocity, Asset 2, GMR Hospitality District, Near IGI Airport, Aerocity, New Delhi has been rated 4.6. And the average price for two people is: 2500\nYou Mee in M 27, Ground Floor, Greater Kailash 2 (GK 2), New Delhi has been rated 4.5. And the average price for two people is: 1000\nMaster Koii's in Shop 19, Flavor Town, Bestech Chambers, Sushant Lok, Gurgaon has been rated 4.5. And the average price for two people is: 1900\nBoa Village in 13, Alipur Road, Civil Lines, New Delhi has been rated 4.3. And the average price for two people is: 2300\nChew - Pan Asian Cafe in M-16, 1st Floor, Outer Circle, Connaught Place, New Delhi has been rated 4.2. And the average price for two people is: 1700\nNoshi - Yum Asian Delivery in 23, Community Centre, Zamrudpur, Greater Kailash 1 (GK 1), New Delhi has been rated 4.2. And the average price for two people is: 1000\nKylin Experience in T-302, 3rd Floor, Ambience Mall, Vasant Kunj, New Delhi has been rated 4.2. And the average price for two people is: 1800\nNagaland's Kitchen in S-2, Uphaar Cinema Complex, Green Park Extension Market, Green Park, New Delhi has been rated 4.2. And the average price for two people is: 1500\n"}
    - slot{"rest_found": true}
	- utter_email_conf
* affirm
    - utter_email_id_ask
* restaurant_search{"email": "urspraveenb@gmail.com"}
    - slot{"email": "urspraveenb@gmail.com"}
    - action_sendemail
    - utter_email_sent
    - utter_goodbye
    - action_restart

## interactive_story_2
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Hubli"}
    - slot{"location": "Hubli"}
    - action_chklocation
    - slot{"loc_avl": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
	- action_chkcuisine
    - slot{"cusn_avl": true}
    - utter_ask_budget
* restaurant_search{"price": "medium"}
    - slot{"price": "medium"}
    - action_search_restaurants
    - slot{"emailbody": "Showing you top rated restaurants:\nDoughpaze Pizzeria in Doughpaze Food Villa, Hubballi, Vidya Nagar, Hubli has been rated 4.5. And the average price for two people is: 350\nRolls Mania in Prashant Colony, Shirur Park, Vidya Nagar, Hubli has been rated 4.4. And the average price for two people is: 300\nMcDonald's in BVB College Of Engg. & Tech, Old PB Road, Vidya Nagar, Hubli has been rated 4.3. And the average price for two people is: 500\nLeelavati Palace in Opposite Urban Oasis Mall, Gokul Road, Rajendra Nagar, Hubli has been rated 4.3. And the average price for two people is: 400\nDomino's Pizza in 1, Upper Ground Floor, Times Square, Prashant Colony, Vidya Nagar, Hubli has been rated 4.2. And the average price for two people is: 400\nHotel Shree Panjurlli in Revankar Complex, T B Road, Deshpandenagar, Hubli - 580029, Opposite ICICI Bank, Keshwapur, Hubli has been rated 4.1. And the average price for two people is: 350\n(IFC) Shadan's Biryani Express in Opposite Samarth PU College, Shirur Park, Vidya Nagar, Hubli has been rated 4.1. And the average price for two people is: 300\nHotel MoonLight in Station Road, New Hubli, Hubli has been rated 4.1. And the average price for two people is: 500\nHotel Shree Panjurlli in Bhage Building, P B Road, Vidyanagar, Hubli - 580021, Opposite BVB College, Vidya Nagar, Hubli has been rated 4.0. And the average price for two people is: 600\nKFC in Gokul Road, Chaitanya Nagar, Industrial Estate, New Hubli, Hubli has been rated 4.0. And the average price for two people is: 450\n"}
    - slot{"rest_found": true}
	- utter_email_conf
* deny
    - utter_goodbye
    - action_restart

## interactive_story_3
* restaurant_search{"cuisine": "North Indian", "location": "Bangalore"}
    - slot{"cuisine": "North Indian"}
    - slot{"location": "Bangalore"}
    - action_chklocation
    - slot{"loc_avl": true}
	- action_chkcuisine
    - slot{"cusn_avl": true}
    - utter_ask_budget
* restaurant_search{"price": "medium"}
    - slot{"price": "medium"}
    - action_search_restaurants
    - slot{"emailbody": "Showing you top rated restaurants:\nThe Hole In The Wall Cafe in 4, 8th Main Road, Koramangala 4th Block, Bangalore has been rated 4.4. And the average price for two people is: 600\nKota Kachori in 635, 100 Feet Road, Koramangala 6th Block, Bangalore has been rated 4.2. And the average price for two people is: 400\n"}
    - slot{"rest_found": true}
	- utter_email_conf
* deny
    - utter_goodbye
    - action_restart

## interactive_story_4
* restaurant_search{"price": "mid", "cuisine": "south", "location": "bangalore"}
    - slot{"cuisine": "south"}
    - slot{"location": "bangalore"}
    - slot{"price": "mid"}
	- action_chklocation
    - slot{"loc_avl": true}
	- action_chkcuisine
    - slot{"cusn_avl": true}
    - action_search_restaurants
    - slot{"emailbody": "Sorry, No results found for your criteria. Would you like to search for some other restaurant criteria?\n"}
    - slot{"rest_found": false}
	- action_restart

## interactive_story_5
* restaurant_search{"price": "low", "cuisine": "Italian", "location": "bangalore"}
    - slot{"cuisine": "Italian"}
    - slot{"location": "bangalore"}
    - slot{"price": "low"}
    - action_chklocation
    - slot{"loc_avl": true}
	- action_chkcuisine
    - slot{"cusn_avl": true}
    - action_search_restaurants
    - slot{"emailbody": "Sorry, No results found for your criteria. Would you like to search for some other restaurant criteria?\n"}
    - slot{"rest_found": false}
	- action_restart

## interactive_story_6
* restaurant_search{"price": "low", "cuisine": "italian", "location": "bangalore"}
    - slot{"cuisine": "italian"}
    - slot{"location": "bangalore"}
    - slot{"price": "low"}
    - action_chklocation
    - slot{"loc_avl": true}
	- action_chkcuisine
    - slot{"cusn_avl": true}
    - action_search_restaurants
    - utter_email_conf
* restaurant_search{"location": "bangalore", "price": "low", "cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - slot{"location": "bangalore"}
    - slot{"price": "low"}
    - action_chklocation
    - slot{"loc_avl": true}
    - action_search_restaurants

## interactive_story_1
* restaurant_search{"price": "low", "cuisine": "Italian", "location": "bangalore"}
    - slot{"cuisine": "Italian"}
    - slot{"location": "bangalore"}
    - slot{"price": "low"}
    - action_chklocation
    - slot{"loc_avl": true}
	- action_chkcuisine
    - slot{"cusn_avl": true}
    - action_search_restaurants
    - slot{"emailbody": "Sorry, No results found for your criteria. Would you like to search for some other restaurant criteria?\n"}
    - slot{"rest_found": false}
    - action_restart

## interactive_story_2
* restaurant_search{"location": "rishikesh"}
    - slot{"location": "rishikesh"}
    - action_chklocation
    - slot{"loc_avl": false}
    - action_restart

## interactive_story_3
* restaurant_search{"cuisine": "south indian", "location": "mumbai"}
    - slot{"cuisine": "south indian"}
    - slot{"location": "mumbai"}
    - action_chklocation
    - slot{"loc_avl": true}
	- action_chkcuisine
    - slot{"cusn_avl": true}
    - utter_ask_budget
* restaurant_search{"price": "medium"}
    - slot{"price": "medium"}
    - action_search_restaurants
    - slot{"emailbody": "Showing you top rated restaurants:\nA.Rama Nayak's Udipi Shri Krishna Boarding in 1st Floor, LBS Market Building, Near Matunga Central Railway Station, Matunga East, Mumbai has been rated 4.8. And the average price for two people is: 400\nDakshinayan in Gandhigram Road, Near Hare Krishna Temple, Juhu, Mumbai has been rated 4.4. And the average price for two people is: 400\nArya Bhavan in Shop 9 & 10, Bhanujyoti Building, Opposite LBS Market, Matunga East, Mumbai has been rated 4.4. And the average price for two people is: 400\nGranville IDC Kitchen in Shop 1, Bhandarkar Bhavan Court Lane, SV Road, Near Borivali Station, Borivali West, Mumbai has been rated 4.3. And the average price for two people is: 300\nDakshinayan in 183, Teen Batti Road, Walkeshwar, Malabar Hill, Mumbai has been rated 4.2. And the average price for two people is: 600\nGughan Supreme South Indian in 91, Ground Floor, Shalimar Building, Near Registrar Of Companies, G Road, Marine Lines, Mumbai has been rated 4.1. And the average price for two people is: 500\nArya Bhavan in G-2, Plot 211, Ground Floor, Dalamal Tower, Free Press Journal Marg, Nariman Point, Mumbai has been rated 4.1. And the average price for two people is: 400\nAnniyam in Shop 7, Royal Classic Building, New Link Road, Andheri Lokhandwala, Andheri West, Mumbai has been rated 4.1. And the average price for two people is: 350\nSouth Tiffin House in Shop 5, Mishra Compound, Charkop, Near Hindustan Naka, M.G.Road, Kandivali West, Mumbai has been rated 4.1. And the average price for two people is: 300\nVanakkam Cafe in Shop 7, Nilgiri Apartments, Opposite Ridhivinayak Mandir, S.V. Road, Malad West, Mumbai has been rated 3.9. And the average price for two people is: 500\n"}
    - slot{"rest_found": true}
    - utter_email_conf
* restaurant_search{"email": "urspraveenb@gmail.com"}
    - slot{"email": "urspraveenb@gmail.com"}
    - action_sendemail
    - utter_email_sent
    - utter_goodbye
    - action_restart

## interactive_story_4
* restaurant_search{"cuisine": "north indian", "price": "low"}
    - slot{"cuisine": "north indian"}
    - slot{"price": "low"}
	- action_chkcuisine
    - slot{"cusn_avl": true}
    - utter_ask_location
* restaurant_search{"location": "bendakaluru"}
    - slot{"location": "bendakaluru"}
    - action_chklocation
    - slot{"loc_avl": false}
	- utter_ask_location
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_chklocation
    - slot{"loc_avl": true}
    - action_search_restaurants
    - slot{"emailbody": "Sorry, No results found for your criteria. Would you like to search for some other restaurant criteria?\n"}
    - slot{"rest_found": false}
    - action_restart

## interactive_story_1
* restaurant_search{"location": "kolkata"}
    - slot{"location": "kolkata"}
    - action_chklocation
    - slot{"loc_avl": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
	- action_chkcuisine
    - slot{"cusn_avl": true}
    - utter_ask_budget
* greet{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - slot{"emailbody": "Showing you top rated restaurants:\nBarbeque Nation in 1st Floor, 24, Park Center Building, Park Street Area, Kolkata has been rated 4.6. And the average price for two people is: 1800\nFusion Fantasea in 14B, Anil Roy Road, Southern Avenue, Kolkata has been rated 4.4. And the average price for two people is: 1000\nChili's Grill & Bar in 33, 4th Floor, Quest Mall, Syed Ali Amir Avenue, Ballygunge, Kolkata has been rated 4.4. And the average price for two people is: 1200\nSpice Kraft in 54/1/2A, Hazra Road, Near Hazra Law College, Ballygunge, Kolkata has been rated 4.4. And the average price for two people is: 850\nOudh 1590 in Shop 23/B, Desapriya Park, Kolkata has been rated 4.4. And the average price for two people is: 1200\nRoastery Coffee House in 70 B, Calcutta South India Club, Gariahat, Kolkata has been rated 4.3. And the average price for two people is: 800\nTraffic Gastropub in 2nd Floor, City Centre 2 Mall, Rajarhat Newtown, Chinar Park, Kolkata has been rated 4.3. And the average price for two people is: 1500\nWhat's Up in 122A, Gate -2, Opposite Nazrul Manch, Southern Avenue, Kolkata has been rated 4.3. And the average price for two people is: 1500\nCalcutta 64 in BC 25, Sector 1, Salt Lake, Kolkata has been rated 4.3. And the average price for two people is: 1000\nPeter Cat in 18A, Park Street, Park Street Area, Kolkata has been rated 4.3. And the average price for two people is: 1000\n"}
    - slot{"rest_found": true}
    - utter_email_conf
* restaurant_search{"email": "urspraveenb@gmail.com"}
    - slot{"email": "urspraveenb@gmail.com"}
    - action_sendemail
    - utter_email_sent
    - utter_goodbye
    - action_restart

## interactive_story_2
* restaurant_search{"cuisine": "american", "location": "kolkata", "price": "high"}
    - slot{"cuisine": "american"}
    - slot{"location": "kolkata"}
    - slot{"price": "high"}
	- action_chklocation
    - slot{"loc_avl": true}
    - action_chkcuisine
    - slot{"cusn_avl": true}
    - action_search_restaurants
    - slot{"emailbody": "Showing you top rated restaurants:\nThe Wise Owl Steakhouse in Rooftop, 66/2B, Purna Das Road, Hindustan Park, Kolkata has been rated 3.6. And the average price for two people is: 1000\n"}
    - slot{"rest_found": true}
    - utter_email_conf
* restaurant_search{"email": "abc@com"}
    - slot{"email": "abc@com"}
    - action_sendemail
    - utter_email_sent
    - utter_goodbye
    - action_restart

## interactive_story_3
* restaurant_search{"location": "mumbaim"}
    - slot{"location": "mumbaim"}
    - action_chklocation
    - slot{"loc_avl": false}
    - action_restart


## interactive_story_1
* restaurant_search{"location": "bagalore"}
    - slot{"location": "bagalore"}
    - action_chklocation
    - slot{"loc_avl": false}
    - action_restart

## interactive_story_2
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_chklocation
    - slot{"loc_avl": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - action_chkcuisine
    - slot{"cusn_avl": true}
    - utter_ask_budget
* restaurant_search{"price": "medium"}
    - slot{"price": "medium"}
    - action_search_restaurants
    - slot{"emailbody": "Showing you top rated restaurants:\nThe Hole In The Wall Cafe in 4, 8th Main Road, Koramangala 4th Block, Bangalore has been rated 4.4. And the average price for two people is: 600\nKota Kachori in 635, 100 Feet Road, Koramangala 6th Block, Bangalore has been rated 4.2. And the average price for two people is: 400\n"}
    - slot{"rest_found": true}
    - utter_email_conf
* affirm
    - utter_email_id_ask
* restaurant_search{"email": "gb@gbail.com"}
    - slot{"email": "gb@gbail.com"}
    - action_sendemail
    - utter_email_sent
    - utter_goodbye
    - action_restart

## interactive_story_3
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_chklocation
    - slot{"loc_avl": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Thai"}
    - slot{"cuisine": "Thai"}
    - action_chkcuisine
    - slot{"cusn_avl": false}
	- utter_ask_cuisine
* restaurant_search{"cuisine": "Biriyani"}
    - slot{"cuisine": "Biriyani"}
    - action_chkcuisine
    - slot{"cusn_avl": false}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Biriyani"}
    - slot{"cuisine": "Biriyani"}
    - action_chkcuisine
    - slot{"cusn_avl": false}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - action_chkcuisine
    - slot{"cusn_avl": true}
    - utter_ask_budget
* restaurant_search{"price": "medium"}
    - slot{"price": "medium"}
    - action_search_restaurants
    - slot{"emailbody": "Showing you top rated restaurants:\nThe Hole In The Wall Cafe in 4, 8th Main Road, Koramangala 4th Block, Bangalore has been rated 4.4. And the average price for two people is: 600\nKota Kachori in 635, 100 Feet Road, Koramangala 6th Block, Bangalore has been rated 4.2. And the average price for two people is: 400\n"}
    - slot{"rest_found": true}
    - utter_email_conf
* restaurant_search{"email": "urd@gmall.com"}
    - slot{"email": "urd@gmall.com"}
    - action_sendemail
    - utter_email_sent
    - utter_goodbye
    - action_restart

## interactive_story_4
* restaurant_search{"cuisine": "chinese", "location": "bangalore"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "bangalore"}
    - action_chklocation
    - slot{"loc_avl": true}
    - action_chkcuisine
    - slot{"cusn_avl": true}
    - utter_ask_budget
* restaurant_search{"price": "medium"}
    - slot{"price": "medium"}
    - action_search_restaurants
    - slot{"emailbody": "Showing you top rated restaurants:\nKhawa Karpo in 50/1,  Near Jyothi Nivas College, Koramangala 5th Block, Bangalore has been rated 4.3. And the average price for two people is: 350\nWok Paper Scissors in 50/1, Opposite Jyothi Niwas College, Koramangala 5th Block, Bangalore has been rated 4.2. And the average price for two people is: 600\nYo! Chow in 90/3, Sri Sapthagiri Complex, Oppsite Innovative Multiplex, Outer Ring Road, Marathahalli, Bangalore has been rated 4.2. And the average price for two people is: 400\nGreen Onion in 43 - 44, Chandraprabha Complex, Residency Road, Bangalore has been rated 4.2. And the average price for two people is: 600\nSzechuan Dragon in 8, 2nd Floor, 1st Main, Arush Trapeze, Mount Joy Road, Behind BMS College of Engineering, Hanumanthnagar, Banashankari, Bangalore has been rated 4.1. And the average price for two people is: 500\nTibetan Mother's Kitchen in 404, 1st C Cross, Near Vodafone Store, Koramangala 7th Block, Bangalore has been rated 4.1. And the average price for two people is: 500\nMomoz in 806, Near ICICI Bank, 7th Cross, 16th Main, 2nd Stage, BTM, Bangalore has been rated 4.1. And the average price for two people is: 600\n"}
    - slot{"rest_found": true}
    - utter_email_conf
* deny
    - utter_goodbye
    - action_restart

## interactive_story_5
* restaurant_search{"cuisine": "Thai", "location": "Bangalore"}
    - slot{"cuisine": "Thai"}
    - slot{"location": "Bangalore"}
    - action_chklocation
    - slot{"loc_avl": true}
    - action_chkcuisine
    - slot{"cusn_avl": false}
    - action_chklocation
    - slot{"loc_avl": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - utter_ask_budget
* restaurant_search{"price": "medium"}
    - slot{"price": "medium"}
    - action_search_restaurants
    - slot{"emailbody": "Showing you top rated restaurants:\nThe Hole In The Wall Cafe in 4, 8th Main Road, Koramangala 4th Block, Bangalore has been rated 4.4. And the average price for two people is: 600\nKota Kachori in 635, 100 Feet Road, Koramangala 6th Block, Bangalore has been rated 4.2. And the average price for two people is: 400\n"}
    - slot{"rest_found": true}
    - utter_email_conf
* deny
    - utter_goodbye
    - action_restart

## interactive_story_6
* greet
    - utter_greet
* restaurant_search{"location": "delhi", "price": "medium"}
    - slot{"location": "delhi"}
    - slot{"price": "medium"}
    - action_chklocation
    - slot{"loc_avl": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - action_chkcuisine
    - slot{"cusn_avl": true}
    - action_search_restaurants
    - slot{"emailbody": "Showing you top rated restaurants:\nAMA Cafe in House 6, New Colony, Majnu ka Tilla, New Delhi has been rated 4.5. And the average price for two people is: 550\nPunjabi Angithi in 32-22, A 4, DDA Market, Paschim Vihar, New Delhi has been rated 4.3. And the average price for two people is: 400\n"}
    - slot{"rest_found": true}
    - utter_email_conf
* deny
    - utter_goodbye
    - action_restart

## interactive_story_7
* restaurant_search{"location": "kolkata"}
    - slot{"location": "kolkata"}
    - action_chklocation
    - slot{"loc_avl": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Thai"}
    - slot{"cuisine": "Thai"}
    - action_chkcuisine
    - slot{"cusn_avl": false}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - action_chkcuisine
    - slot{"cusn_avl": true}
    - utter_ask_budget
* restaurant_search{"price": "medium"}
    - slot{"price": "medium"}
    - action_search_restaurants
    - slot{"emailbody": "Showing you top rated restaurants:\nBlue Mug in 1/121, Jodhpur Park, Kolkata has been rated 4.2. And the average price for two people is: 650\n"}
    - slot{"rest_found": true}
    - utter_email_conf
* restaurant_search{"email": "gib@gibb.com"}
    - slot{"email": "gib@gibb.com"}
    - action_sendemail
    - utter_email_sent
    - utter_goodbye
    - action_restart

## interactive_story_1
* restaurant_search{"location": "jayanager", "price": "low"}
    - slot{"location": "jayanager"}
    - slot{"price": "low"}
    - action_chklocation
    - slot{"loc_avl": false}
    - utter_ask_location
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_chklocation
    - slot{"loc_avl": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "biriyani"}
    - slot{"cuisine": "biriyani"}
    - action_chkcuisine
    - slot{"cusn_avl": false}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - action_chkcuisine
    - slot{"cusn_avl": true}
    - action_search_restaurants
    - slot{"emailbody": "Sorry, No results found for your criteria. Would you like to search for some other restaurant criteria?\n"}
    - slot{"rest_found": false}
    - utter_email_conf
* deny
    - utter_goodbye
    - action_restart

## interactive_story_2
* restaurant_search{"location": "delhi", "cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "delhi"}
    - action_chklocation
    - slot{"loc_avl": true}
    - action_chkcuisine
    - slot{"cusn_avl": true}
    - utter_ask_budget
* restaurant_search{"price": "medium"}
    - slot{"price": "medium"}
    - action_search_restaurants
    - slot{"emailbody": "Showing you top rated restaurants:\nThey Make Tacos in 100, Block UB, Jawahar Nagar, Kamla Nagar, New Delhi has been rated 4.2. And the average price for two people is: 300\nGronito.Com in A 8, Sanjay Enclave, Raja Puri Road, Uttam Nagar, New Delhi has been rated 3.9. And the average price for two people is: 600\nThe Rolling Kitchen in DLF Phase 4, Gurgaon has been rated 3.7. And the average price for two people is: 600\nLet's Nachos in Sapphire, Sector 83, Gurgaon has been rated 3.3. And the average price for two people is: 500\n"}
    - slot{"rest_found": true}
    - utter_email_conf
* deny
    - utter_goodbye
    - action_restart

## interactive_story_3
* greet
    - utter_greet
