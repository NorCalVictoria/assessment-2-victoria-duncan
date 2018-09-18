 def print_melon_at_price(price):
    """Given a price, print all melons available at that price, in alphabetical order.

    Here are a list of melon names and prices:

     Honeydew 2.50
     Cantaloupe 2.50
     Watermelon 2.95
     Musk 3.25
     Crenshaw 3.25
     Christmas 14.25
     (it was a bad year for Christmas melons -- supply is low!)

     If there are no melons at that price print "None found"

         >>> print_melon_at_price(2.50)
         Cantaloupe
         Honeydew

         >>> print_melon_at_price(2.95)
         Watermelon

         >>> print_melon_at_price(5.50)
         None found
     """
     #create a dictionary of melon prices
     melon_prices = {   
          'Honeydew': 2.50,         'Cantaloupe': 2.50,
          'Watermelon': 2.95,
         'Musk': 3.25,
         'Crenshaw': 3.25,
         'Christmas': 14.25
     }
    
     #if inputted price is in the values list of melon_prices
     if price in melon_prices.values():
         #Iterate through iteritems
         for melon, cost in sorted(melon_prices.iteritems()):
             #if price is equal to the cost of the melon
#             if price == cost:
                 #print melon
                 print melon
     #If you don't find the cost in the values, print 'None found'
     else: 
         print 'None found'
            


    
 print_melon_at_price(3.25)