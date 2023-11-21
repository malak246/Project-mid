print('Welcome To Our Resturant')
item={}
list_order=[]
while True:
 print("1 To ADD New Item ")
 print("2_To Search For An Item")
 print("3_To Delete An Item")
 print("4_To Exit")
 print("___"*20)
 choice=input("Please Insert Your Choice:  ")
 if choice=='1':
    
    while True:            
                    try: 
                          size = int(input("Enter The Size Of Your Order: "))
                          break     
                    except ValueError as e :
                            
                            print('You Insert A WrongValue Size')
                            continue
    for i in range(size):
        ID = input("Enter The ID Of Menu: ")
        Name=input('Enter Name: ')
        while True:            
                    try: 
                            Price=int(input('Enter Price: '))
                            break     
                    except ValueError as e :
                            
                            print('You Insert A WrongValue Price')
                            continue
      
                        
        item[ID] = {}                      
        DES = input("Enter Description: ")
        item[ID]["Name"] = Name
        item[ID]["Price"] = Price
        item[ID]["Description"] = DES
        print(item)
 elif choice=='2':
       print('Do You Need Help ? ')
       for i in item:
              num=input('Enter The ID Address:')
              if item[ID]==num:
                     print('Found ',item)
              else:
                     print('Item Dose Not Exist !')       
 elif choice=='3':
        print('Do You Need Help ? ')
        for i in item:
              num=input('Enter The ID Address:')
              if item[ID]==num:
                     del item[ID]
                     print(item)
              else:
                     print('Error,Item Dose Not Exist !')  
        
 elif choice=='4':
       break
                    
