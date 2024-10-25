Servises={"service1" : "private rooms",
          "service 2" : "Advance reservation",
}

employees2={"Shaving5: Ali",
            "Shaving6: daher",
            "Shaving 7 : Hussuin"
}

employees={"Boss" : "Mohammad",
           "shaving1" : "Mohammad",
           "shaving2" : "faraj" ,
           "Shaving2" : "Bahaa",
           "shaving3" : "deaa"
}

information_about_shope={"start" : 2022,
                         " leader" : "Mohammad Harb",
                         " location" : "Irbid: university stree",
                         " Our Motto" : "Satisfying our customers"
                         }
print("Hello sir how i can help you ")

     
def check_services():
    service=int(input("enter a number to choice your service"))
    
    services=[1,2,3,4]
    if service ==1:
        print("hello sir your service 1 consist of saving head")
    elif service ==2:
        print("hello sir your secound service consest of shaving head and beard")
    elif service ==3:
        print("Hello Sir, Service Number  3 consists of cleaning the skin")
    elif service ==4:
        print("Hello Sir, Service No. 4 consists of a full haircut, beard and skin cleansing")
    else:
        while service not in services:
                service=input("enter a number to choice your service")



def check_employees():
    check_emolyee=input("please sir enter your name To access your own website")
    list_of_employees=["Mohammad", "Baha", "deaa","faraj"]

    while check_emolyee not in list_of_employees:
        print("Sorry sir, you can't come in. You don't work here")
        check_emolyee=input("please sir enter your name To access your own website").lower()

    else:
            
        password=input("hello sir please enter your password")
        sername=input("hello sir please enter your full name")
        
     
    
#system obout employees





#رجعها ل ليست
def information():
    Know_inf=input("what is your information you need to know?")
    print(" first thanks for coming to my shope if you want to to get to know some information about my shope")            
    list_of_inf=["start","leader","location","Our Motto"]
    for i in list_of_inf:
        if know_inf =="start":
            print(information_about_shope["start"])
        elif know_inf== "leader":
            print(information_about_shope[" leader"])
        elif know_inf =="location":
            print(information_about_shope["location"])
        elif know_inf == "Our Motto":
            print(information_about_shope[" Our Motto"])
        else :
            while Know_inf not in list_of_inf:
                
                print( "invalid value ")
                Know_inf=input("what is your information you need to know?")

def know_prices():
    prices=input("hello sir to know our prices please enter the service ")
    list_of_prices=["head", "head and beard" , "clean skin" , "full service face"]
        #convert to numbers down
    if prices == "head":
        print("Head shaving is 5 dinars")
    elif prices =="head and beard":
        print("head and beard shaving is 10 dinars")
    elif prices == "clean skin ":
        print("your clean and skin shaving is 15 dinars")
    elif prices =="full service face ":
        print("your full service face shaving  is 20 dinars ")
    else:
        while prices not in list_of_prices:
            
            print("We do not have any other services, sir")
            prices=input("hello sir to know our prices please enter the service ")

def New_shope():
    print("Hello sir how i can help you")
    print("please inter a number to do a service ")
    print(" 1_private rooms , 2_Advance reservation")
    enter =int(input("enter a number between 1 and 2 "))
    if  enter== 1:
        print(Servises["service1"])
        print("your choice is great sir")
    elif enter ==2:
        print(Servises ["service1"])
        print("Your choice is great ")
        
        
        
    
    
    
def transform():
    
    switch=input("Do you want to switch to the other store?")
    if switch=="yes ":
        New_shope()
        
    elif switch =="NO":
            switch=input("Do you want to switch to the other store?")
    else :
        while True :
            
            switch=input("Do you want to switch to the other store?")

while True:
    chosse = int(input("""
                  1-check_services 
                  2- know_prices
                  3- check_employees
                  4- information
                  5- exit\n
                  6-transform \n"""))
    
    
    if chosse == 1:
        check_services()
    elif chosse == 2:
        know_prices()
    elif chosse == 3 :
        check_employees()
    elif chosse == 4 :
        information()
    elif chosse== 6:
        transform()
    else:
        break 

    
    




