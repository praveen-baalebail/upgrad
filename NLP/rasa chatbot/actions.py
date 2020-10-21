from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_sdk import Action
from rasa_sdk.events import SlotSet
import zomatopy
import json

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

#This class will search restaurants based on provided location, cuisine and price range.
class ActionSearchRestaurants(Action):
    def name(self):
        return 'action_search_restaurants'
        
    def run(self, dispatcher, tracker, domain): 
        #use zompato api key.
        config={"user_key":"bc4e4a608fc7c3eb63e9f45f80c01fa9"}
        zomato = zomatopy.initialize_app(config)
        
        #Set default flag for search results
        found=False
        
        #Get location, cuisine and price for search.
        loc = tracker.get_slot('location')
        cuisine = tracker.get_slot('cuisine')
        price = tracker.get_slot('price')

        #If mandatory fields not passed then display error the message.
        if loc is None:
            response= "Sorry, we don't operate in this city.Please provide Tier-1/Tier-2 City name "+"\n"
            found=False
            dispatcher.utter_message(response)
            return False
        
        elif cuisine is None:
            response= "Please provide available Cuisine types"+"\n"
            found=False
            dispatcher.utter_message(response)
            return False
            
        elif price is None:
            response= "Please provide Budget criteria "+"\n"
            found=False
            dispatcher.utter_message(response)
            return False
        
        #Prepare the dictionary for cuisine and price
        cuisines_dict={'chinese':25,'italian':55,'north indian':50,'south indian':85,'american':1,'mexican':73}
        price_dict = {'low':1,'medium':2,'high':3}
        
        #prepare and Pass the required parameters to zomato restaurant_search method.
        location_detail=zomato.get_location(loc, 1)
        d1 = json.loads(location_detail)
        lat=d1["location_suggestions"][0]["latitude"]
        lon=d1["location_suggestions"][0]["longitude"]
        
        results=zomato.restaurant_search("", lat, lon, str(cuisines_dict.get(cuisine)), 50000)
        
        d = json.loads(results)
        count = 0
        response="Showing you top rated restaurants:"+"\n"
        
        #If no resoults found from api call display the message.
        if d['results_found'] == 0:
            response= "No restaurant found for your criteria"+"\n"
            found=False
            dispatcher.utter_message(response)
            
        #if results found get top 10 restaurants with top rating first.
        else:           
            for restaurant in sorted(d['restaurants'],
                                     key=lambda x: x['restaurant']['user_rating']['aggregate_rating']
                                     , reverse=True): 
                
                #assign values to variables for reusability.
                cost_for_2=restaurant['restaurant']['average_cost_for_two']
                rstrnt_nm=restaurant['restaurant']['name']
                rstrnt_addr=restaurant['restaurant']['location']['address']
                rstrnt_rtng=restaurant['restaurant']['user_rating']['aggregate_rating']
                
                #If price range is low, get top 10 restaurants from this loop
                if((price_dict.get(price) == 1) and (int(cost_for_2) < 300) and (count < 10)):
                    response=response+ rstrnt_nm + " in "+ rstrnt_addr + " has been rated "+ rstrnt_rtng +"."
                    response=response+" And the average price for two people is: "+ str(cost_for_2) +"\n"
                    count = count + 1
                    
                #If price range is medium, get top 10 restaurants from this loop        
                elif((price_dict.get(price) == 2) and (int(cost_for_2) >= 300) and (int(cost_for_2) <= 700) and (count < 10)):
                    response=response+ rstrnt_nm + " in "+ rstrnt_addr + " has been rated "+ rstrnt_rtng +"."
                    response=response+" And the average price for two people is: "+ str(cost_for_2) +"\n"
                    count = count + 1      
                    
                #If price range is high, get top 10 restaurants from this loop     
                elif((price_dict.get(price) == 3) and (int(cost_for_2) > 700) and (count < 10)):
                    response=response+ rstrnt_nm + " in "+ rstrnt_addr + " has been rated "+ rstrnt_rtng +"."
                    response=response+" And the average price for two people is: "+ str(cost_for_2) +"\n"
                    count = count + 1 
                    
                #Once count is 5, send the message to rasa with results.
                if(count==5):
                    dispatcher.utter_message(response)
                    found=True
                    
        #if the overall count is between 0 and 5, return the results to rasa
        if(count<5 and count>0):
            dispatcher.utter_message(response)
            found=True
        
        #if no results found for given price range then, return this message to rasa
        if(count==0):
            response = "Sorry, No results found for your criteria. Would you like to search for some other restaurant criteria?"+"\n"
            found=False
            dispatcher.utter_message(response)
        
        #Set emailbody content with top 10 results for future use if user opts for email option.
        return [SlotSet('emailbody',response),SlotSet('rest_found',found)]

#This class will send mail to given user email id.
class ActionSendEmail(Action):

    def name(self):
        return 'action_sendemail'

    def run(self, dispatcher, tracker, domain):
        
        #Config username and password for chatbot to send mails to user.
        from_user = 'baalebail.udemy@gmail.com'
        to_user = tracker.get_slot('email')
        password = 'Epsilon19'
        
        #smpt configuration for gmail.
        server = smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.login(from_user, password)
        
        #
        subject = 'Hello from chatbox'
        msg = MIMEMultipart()
        msg['From'] = from_user
        msg['TO'] = to_user
        msg['Subject'] = subject
        body = tracker.get_slot('emailbody')
        msg.attach(MIMEText(body,'plain'))
        text = msg.as_string()
        server.sendmail(from_user,to_user,text)
        server.close()

#This class will be used for checking if provided cuisine name belongs to listed cuisines.
class ActionCheckCuisine(Action):

    def name(self):
        return 'action_chkcuisine'

    def run(self, dispatcher, tracker, domain):
        cusn = tracker.get_slot('cuisine')
        found=False

        #Read cuisine.txt file where all cuisine names are listed.
        cuisine_file = open("data/cuisine.txt", "r")
        cuisines = []
        for line in cuisine_file:
            stripped_line = line.strip()
            cuisines.append(stripped_line.lower())

        cuisine_file.close()
        
        #If cuisine name is not in the list then return a message.
        if cusn.lower() not in cuisines:
            
            found=False
            response = "Can you please pick from available options for cuisine"+"\n"
            dispatcher.utter_message(response)
        else:
            found=True
        return [SlotSet('cusn_avl',found)]

#This class will be used for checking if provided city name belongs to Tier-1 and Tier-2 or not.
class ActionCheckLocation(Action):

    def name(self):
        return 'action_chklocation'

    def run(self, dispatcher, tracker, domain):
        loc = tracker.get_slot('location')
        found=False

        #Read city.txt file where all tier1 and tier 2 city names are listed.
        city_file = open("data/city.txt", "r")
        cities = []
        for line in city_file:
            stripped_line = line.strip()
            cities.append(stripped_line.lower())

        city_file.close()
        
        #If city name is not in the list then return a message.
        if loc.lower() not in cities:
            
            found=False
            response = " Sorry, we don’t operate in this city. Can you please specify some other location"+"\n"
            dispatcher.utter_message(response)
        else:
            found=True
        return [SlotSet('loc_avl',found)]