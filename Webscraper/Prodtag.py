import webscrapev2


# variables for rating
product_rating = 0
seller_rating = 0
delivery_rating = 0


# variables to get total value of product rating
product_quality = 0
seller_service = 0
delivery_service = 0


# variables for quantity of each tag
overall_rating = 0
product_quantity = 0
seller_quantity = 0
delivery_quantity = 0


# Product Quality
# Function to get Product rating tag value
def Product_quality(rating):
    switcher = {
        # 5 Star
        "Excellent quality" : 5,
        "Good quality": 4,
        "Well-packaged": 4,
        "Will  order again": 4,
        "Ok quality" : 3,
        "Standard packaging" : 3,
        "Poor quality" : 2,
        "Poor packaging" : 2,
        "Damaged / Defective item" : 1,
        "Item different from picture " : 1,
        "Will not order again" : 1,
        "Damaged packaging" : 1,
    }
  
    return switcher.get(rating, 0)

#Seller Service
# Function to get Product rating tag value
def Seller_service(rating):
    switcher = {
        "Very accommodating seller" : 5,
        "Accommodating seller" : 4,
        "Responsive seller " : 3,
        "Seller not responsive" : 2,
        "Wrong item received" : 1,
        "Rude seller" : 1,
        "Did not receive item" : 1,
        
    }

    return switcher.get(rating, 0)
  
# Delivery Service
# Function to get Product rating tag value
def Delivery_service(rating):
    switcher = {
        "Item shipped immediately" : 5, 
        "Item shipped quickly" : 4,
        "Item shipped on-time" : 3,
        "Item shipped late" : 2,
        "Item shipped very late" : 1,

    }

    return switcher.get(rating, 0)




# Driver program
if __name__ == "__main__":

    # Input
    rating= webscrapev2.rating
    
    #Summmarize the Product Rating Tag
    # initializing dict to store frequency of each element
    elements_count = {}
    # iterating over the elements for frequency
    for element in rating:
        # checking whether it is in the dict or not
        if element in elements_count:
      # incerementing the count by 1
            elements_count[element] += 1
        else:
        # setting the count to 1
            elements_count[element] = 1


    # Print the frequency of every product ratinng tag
    print("Summarize Product Tags: ")
    for key, value in elements_count.items():
       print(f"{key}: {value}")

    print("\n")

    # get the rate value for every rating 
    for x in rating:

        # add the rate if  it is a Product quality tag
        rate = Product_quality(x) 
        if(rate != 0):
            product_quality += rate
            product_quantity+=1

        # add the rate if  it is a Seller service tag
        rate = Seller_service(x) 
        if(rate != 0):
            seller_service += rate
            seller_quantity+=1

        # add the rate if  it is a Delivery service tag
        rate = Delivery_service(x) 
        if(rate != 0):
            delivery_service += rate
            delivery_quantity+=1

    # Get the ratings value
    if product_quantity != 0:
        product_rating = product_quality / product_quantity


    if seller_quantity != 0:
        seller_rating = seller_service / seller_quantity


    if delivery_quantity != 0:
        delivery_rating = delivery_service / delivery_quantity

    # Convert the ratings value into Percentage
    product_rating = (product_rating / 5) * 100
    seller_rating = (seller_rating / 5) * 100
    delivery_rating = (delivery_rating / 5) * 100

    # Check if there is a category that is not yet rated
    # if there is, exclude that in computing overall ratings
    no_rating = 0;
    if(product_rating == 0):
        no_rating += 1

    if(seller_rating == 0):
        no_rating += 1
    
    if(delivery_rating == 0):
        no_rating += 1

    # Get the overall rating
    overall_rating = product_quantity + seller_rating + delivery_rating
    overall_rating /= (3 - no_rating) 

    # Print the ratings
    print("Overall Rating: ",overall_rating)
    print("Product Rating: ",product_rating)
    print("Seller Rating: ",seller_rating)
    print("Delivery Rating: ",delivery_rating)
    print("\n")

#For GUI
# Intatiate the GUI
from tkinter.constants import BOTH, END
import tkinter as tk
import tkinter.font as tkFont

window = tk.Tk()

window.title("Prodtag")

window.geometry('600x500')

# GUI event
def clicked():
    url = txtfield.get("1.0",END)
    print(url)

# GUI Components

# Textbox label
lbl_font = tkFont.Font(family="Lucida Grande", size=10)
lbl = tk.Label(window, text="Enter Product URL: ", font= lbl_font)
lbl.place(x = 100,y = 190)

# Input textbox
txtfield = tk.Text(window, height = 2, width = 52)
txtfield.place(x = 100,y = 210)

# Output Prodtag
Prodtag_lbl_font = tkFont.Font(family="Lucida Grande", size=40)
Prodtag_lbl = tk.Label(window,text = "Prodtag", font=Prodtag_lbl_font)
Prodtag_lbl.place(x = 220,y = 85)

# Analyze button 
btn = tk.Button(window, text="Analyze It!", width= 10, height= 2, command=clicked)
btn.place(x = 220,y = 270)


window.mainloop()