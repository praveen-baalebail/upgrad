## intent:affirm
- yes
- yep
- yeah
- indeed
- that's right
- ok
- great
- right, thank you
- correct
- great choice
- sounds really good
- thanks

## intent:deny
- No
- no,thanks
- not required
- nope
- no thanks
- no
- no, thanks

## intent:goodbye
- bye
- goodbye
- good bye
- stop
- end
- farewell
- Bye bye
- have a good one

## intent:greet
- hey
- howdy
- hey there
- hello
- hi
- good morning
- good evening
- dear sir
- hola

## intent:restaurant_search
- i'm looking for a place to eat
- I want to grab lunch
- I am searching for a dinner spot
- I am looking for some restaurants in [Delhi](location).
- I am looking for some restaurants in [Bangalore](location)
- show me [chinese](cuisine) restaurants
- show me [chines]{"entity": "cuisine", "value": "chinese"} restaurants in the [New Delhi]{"entity": "location", "value": "Delhi"}
- show me a [mexican](cuisine) place in the [centre](location)
- i am looking for an [indian](cuisine) spot called olaolaolaolaolaola
- search for restaurants
- anywhere in the [west](location)
- I am looking for [asian fusion](cuisine) food
- I am looking a restaurant in [294328](location)
- in [Gurgaon](location)
- [South Indian](cuisine)
- [North Indian](cuisine)
- [Italian](cuisine)
- [Chinese]{"entity": "cuisine", "value": "chinese"}
- [chinese](cuisine)
- [Lithuania](location)
- Oh, sorry, in [Italy](location)
- in [delhi](location)
- I am looking for some restaurants in [Mumbai](location)
- I am looking for [mexican indian fusion](cuisine)
- can you book a table in [rome](location) in a [medium](price) price range with [british](cuisine) food for [four]{"entity": "people", "value": "4"} people
- can you book a table in [rome](location) in a [low](price) price range with [british](cuisine) food for [four]{"entity": "people", "value": "4"} people
- [central](location) [indian](cuisine) restaurant
- please help me to find restaurants in [pune](location)
- Please find me a restaurantin [bangalore](location)
- [mumbai](location)
- show me restaurants
- please find me [chinese](cuisine) restaurant in [delhi](location)
- can you find me a [chinese](cuisine) restaurant
- [delhi](location)
- please find me a restaurant in [ahmedabad](location)
- please show me a few [italian](cuisine) restaurants in [bangalore](location)
- restaurants
- [bangalore](location)
- restaurant in [bangalore](location)
- I am looking for some restaurants in [Mumbai](location) in a [low](price) price range
- I am looking for some restaurants in [Mumbai](location) in a [meduim]{"entity": "price", "value": "medium"} price range
- I am looking for some restaurants in [Mumbai](location) in a [high](price) price range
- restaurant in [bangalore](location) [chinese](cuisine) cuisine in a [high](price) price range
- restaurant in [bangalore](location) [chinese](cuisine) cuisine in a [low](price) price range
- restaurant in [bangalore](location) [chinese](cuisine) cuisine in a [medium](price) price range
- [low](price) price
- find [chinese](cuisine) restaurant in [bangalore](location) with [high](price) price
- restaurants in [bangalore](location)
- [medium](price)
- [high](price)
- [bengaluru](location) restaurants for [south indian](cuisine) cuisine in [medium](price) range
- find restaurant in [Bangalore](location) with [south indian](cuisine) cuisine for [medium](price) price
- [abcd@gmail.com](email)
- [abcd.def@gmail.com](email)
- restaurants in [Bangalore](location) for [high](price) price with [chinese](cuisine) cuisine
- find me [mid]{"entity": "price", "value": "medium"} price [south]{"entity": "location", "value": "South Indian"} restaurants in [bangalore](location)
- find me [mid]{"entity": "price", "value": "medium"} price [north]{"entity": "location", "value": "North Indian"} restaurants in [Delhi](location)
- [mid]{"entity": "price", "value": "medium"} range.
- [south]{"entity": "location", "value": "South Indian"} restaurants
- find [low](price) price [Italian](cuisine) restaurants in [bangalore](location)
- find restaurants in [rishikesh](location)
- in [bangalore](location)
- find [south indian](cuisine) restaurant in [mumbai](location)
- yes, send it to [urspraveenb@gmail.com](email)
- show me [north indian](cuisine) restaurants for [low](price) price
- [bendakaluru](location)
- show me in [bangalore](location)
- show me restaurants in [kolkata](location)
- [American](cuisine)
- find [american](cuisine) restaurants in [kolkata](location) for [high](price) price
- send it to [abc@com](email)
- show me restaurants in [mumbaim](location)
- find restaurants in [Bombay]{"entity": "location", "value": "Mumbai"}
- I'll prefer [Italian](cuisine)!
- in range of [300 to 700]{"entity": "price", "value": "medium"}
- find biryani cuisine in [bangalore](location)
- I like Thai !
- find restaurants in [bagalore](location)
- find restaurants in [bangalore](location)
- [gb@gbail.com](email)
- I prefer [Thai](cuisine)
- [Biriyani](cuisine)
- yes, send it to [urd@gmall.com](email)
- find [chinese](cuisine) restaurant in [bangalore](location)
- find [Thai](cuisine) restaurant in [Bangalore](location)
- [Mexican](cuisine)
- show me some good restaurants in [delhi](location) for [mid]{"entity": "price", "value": "medium"} price
- find restaurants in [kolkata](location)
- I prefer [Thai](cuisine) cuisine
- yes send it to [gib@gibb.com](email)
- find me restaurants in [jayanager](location) for [low](price) price
- [bangalore](location)
- [biriyani](cuisine)
- [Mexican](cuisine)
- show me restaurants in [delhi](location) for [chinese](cuisine) and [mexican](cuisine) cuisine
- [medium](price)

## synonym:4
- four

## synonym:Bangalore
- Bengaluru

## synonym:Delhi
- New Delhi
- Dilli

## synonym:Kolkata
- Calcutta

## synonym:Mumbai
- Bombay
- bombay

## synonym:North Indian
- north

## synonym:Pondicherry
- Pondi

## synonym:South Indian
- south

## synonym:Thiruvananthapuram
- Trivandrum

## synonym:chinese
- chines
- Chinese
- Chines

## synonym:medium
- meduim
- mid
- 300 to 700
- moderate

## synonym:vegetarian
- veggie
- vegg

## regex:email
- ^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$

## regex:greet
- hey[^\s]*

## regex:pincode
- [0-9]{6}

## lookup:location
  data/city.txt

## lookup:cuisine
  data/cuisine.txt
