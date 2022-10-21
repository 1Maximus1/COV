end=False
while not end:
    try:
        number_of_task=int(input("Please, enter number of task(1,2,3,4,5 or 0 - exit): "))
        if number_of_task ==1:

            print("\nData on the recipient of the letter of the post according to the standards of Ukrposhta.(task 1)\n")
    
            #input block

            name_user= input("Please, enter your name: ")
            surname_user=input("Please, enter your surname: ")
            i=0
            while i==0:
                try:
                    number_user=int(input("Please, enter your phone number: "))
                    i+=1
                except:
                    print("Wrong number!")
            street_user=input("Please, enter your street name: ")
            j=0
            while j==0:
                try:
                    number_house_user=int(input("Please, enter your house number: "))
                    j+=1
                except:
                    print("Error! Please, enter correct data!")
            k=0
            while k==0:
                try:
                    number_flat_user=int(input("Please, enter your apartment number: "))
                    k+=1
                except:
                    print("Error! Please, enter correct data!")
            city_user= input("Please, enter your city: ")
            l=0
            while l==0:
                try:
                    index_user=int(input("Please, enter your index: "))
                    l+=1
                except:
                    print("Error! Please, enter correct data!")

            country_user=input("Please, enter your county: ")

            #output block

            print("\nInformation about user: \n")
            print(name_user+" "+ surname_user+'\n'+str(number_user)+'\n'+f'Str. {street_user} {number_house_user}, ap. {number_flat_user}, {city_user} \n'+str(index_user)+'\n'+country_user+'\n')

        elif number_of_task==2:
            print("\nThe magnetic table of earthquakes on the Richter scale. (task 2)\n")
            i=0
            while i==0:
                try:
                    magnitude_user=float(input("Please, enter your magnitude(1-12): "))
                    if magnitude_user>12 or magnitude_user<0:
                        print("There is no such scale!")
                    else:
                        i+=1
                except:
                    print("Error! Please, enter correct data!")
                    
            if magnitude_user<2:
                print("Inconspicuous earthquake")
            elif (magnitude_user>=2) and (magnitude_user<3):
                print("Almost imperceptible earthquake")
            elif (magnitude_user>=3) and (magnitude_user<4):
                print("Very weak earthquake")
            elif (magnitude_user>=4) and (magnitude_user<5):
                print("Weak earthquake")
            elif (magnitude_user>=5) and (magnitude_user<6):
                print("Moderate earthquake")
            elif (magnitude_user>=6) and (magnitude_user<7):
                print("Strong earthquake")
            elif (magnitude_user>=7) and (magnitude_user<8):
                print("Destructive earthquake")
            elif (magnitude_user>=8) and (magnitude_user<10):
                print("Devastating earthquake")
            elif magnitude_user>10:
                print('Severe disaster: ')

        elif number_of_task==3:

            print("\nThe program that calculates the amount of funds that the subscriber will have to pay for a month. (task 3) \n")
            i=0
            while i==0:
                try:
                    minutes_user=int(input("Please, enter how many minutes you spent on calls: "))
                    i+=1
                except:
                    print("Error! Please, enter correct data!")
            if minutes_user < 0:
                print("Error")
            elif minutes_user <=50:
                summ_user=100
                print(str(summ_user)+ " UAH")
            elif (minutes_user>=50) and (minutes_user<=100):
                summ_user=150
                print(str(summ_user)+ " UAH")
            elif minutes_user>100:
                summ_user=(minutes_user-100)*2+150
                print(str(summ_user)+ " UAH")
        elif number_of_task==4:
            print("\nThe program generates a table with new prices. (task 4)\n")
            products_list=[]
            products_list1=[]
            products_list2=[]
            i=0
            while i==0:
                try:
                    quantity=int(input("How many prices do you want to change: "))
                    i+=1
                except:
                    print("Error! Please, enter correct data!")

            for i in range(0,quantity):
                l=0
                while l==0:
                    try:
                        print("Write the", i+1 , "price: ",end='')
                        products_list.append(float(input()))
                        l+=1
                    except:
                        print("Error! Please, enter correct data!")
                products_list1.append(round(products_list[i],2))
                products_list1[i]= round(((products_list1[i]*60)/100),2)
                products_list2.append(products_list1[i])
                products_list2[i]=round((products_list[i]-products_list1[i]),2)
            for i in range (0,quantity):
               str1,str2,str3=str(products_list[i]),str(products_list1[i]),str(products_list2[i])
               print(str1.center(10),  str3.center(10),str2.center(10))
            print(products_list)
        elif number_of_task==5:
            l=0
            while l==0:
                try:
                    quantit_user=int(input("How many words do you want to write: "))
                    l+=1
                except:
                    print("Error! Please, enter correct data!")
            words_user=[]
            for i in range(0,quantit_user):
                print("Write the", i+1 , "word: ",end='')
                words_user.append(input())
              
            for i in range(0,quantit_user):
                if quantit_user==1:
                    words_user[i]=words_user[i]
                elif (i == quantit_user and quantit_user==2) or i==quantit_user-1:
                    words_user[i]='and '+words_user[i]
                elif i<quantit_user-1 and quantit_user!=2:
                    words_user[i]=words_user[i]+','
                print(words_user[i],end=' ')
        elif number_of_task==0:
            end=True
        else:
            print("There is no such task!")
    except:
        print("Error! Wrong data")