class phone_Contacts:                                                                                   
    
    def __init__(self,Firstname,Phone_number,Email_ID,Groups,DOB):                             
        self.firstname=Firstname
        self.phonenumber=Phone_number
        self.emailid=Email_ID
        self.groups=Groups
        self.dob=DOB
        
        
    def open_phcontacts(self):
        print("Phone Contacts")
    
        
    def firstname_verification(self):
        if type(self.firstname) == str:
            if len(self.firstname) <= 15:                                                                                
                print("Firstnameame verified")
               
            else:
                raise ValueError("Firstnameame should contain lesser than or equal to 15 letters")
        else:
            raise TypeError("Firstname should contain letters only")

    def phonenumber_verification(self):
        if (len(self.phonenumber)==10):
            if type(self.phonenumber) == str:                                                                            
                print("Phone number verified")
            else:
                raise TypeError("Phone number should contain only integers ")
            
        
    def emailid_verification(self):
        if type(self.emailid) == str:                                                                               
            if len(self.emailid) <= 25:                                                                              
                print("Emailid verified")
            else:
                raise ValueError("Emailid should not contain more than 25 values")
        else:
            raise TypeError("Invalid emailid")    
        

    def groups_verification(self):
        if type(self.groups) == str:
            if len(self.groups) <= 10:                                                                              
                print("Groups verified")
            else:
                raise ValueError("Groups should contain lesser than or equal to 10 letters")
        else:
            raise TypeError("Groups should contain letters only")

    def dob_verification(self):
        if isinstance(self.dob,str):                                                                                
            if len(self.dob) <= 10:                                                                                 
                print("DOB verified")
            else:
                raise ValueError("DOB should contain lesser than or equal to 10 letters")
        else:
            raise TypeError("DOB should contain numbers and symbols only")   
   
a={}
con=[]
namec=input("enter the first name")
numberc=input("enter the number")
emailc=input("enter the email id")
familyc=input("enter the family")
dobc=input("enter the dob")
mano=phone_Contacts(namec,numberc,emailc,familyc,dobc)
mano.open_phcontacts()
mano.firstname_verification()
mano.phonenumber_verification()
mano.emailid_verification()
mano.groups_verification()
mano.dob_verification()



        
user=input("enter the number to search")
phone=filter(lambda x: x["Firstname"]==user,[{"Firstname":"vasu","Phno":9854261725,"Email_id":"123@gmail.com","Groups":"Family","DOB":"08/04/2001"},                                  
       {"Firstname":"kumar","Phno":9987968725,"Email_id":"abc@gmail.com","Groups":"Friends","DOB":"03/05/2001"},
       {"Firstname":"nanbi","Phno":9854068725,"Email_id":"123@gmail.com","Groups":"Family","DOB":"08/04/2001"},                                  
       {"Firstname":"nanu","Phno":9987968725,"Email_id":"abc@gmail.com","Groups":"Friends","DOB":"03/05/2001"},
       {"Firstname":"barath","Phno":9854268725,"Email_id":"123@gmail.com","Groups":"Family","DOB":"08/04/2001"},                                  
       {"Firstname":"nani","Phno":9987768725,"Email_id":"abc@gmail.com","Groups":"Friends","DOB":"03/05/2001"},
       {"Firstname":"lila","Phno":9854228725,"Email_id":"123@gmail.com","Groups":"Family","DOB":"08/04/2001"},                                  
       {"Firstname":"ola","Phno":9987969725,"Email_id":"abc@gmail.com","Groups":"Friends","DOB":"03/05/2001"},
       {"Firstname":"Abu","Phno":9854262725,"Email_id":"123@gmail.com","Groups":"Family","DOB":"08/04/2001"},                                  
       {"Firstname":"bhii","Phno":9987988725,"Email_id":"abc@gmail.com","Groups":"Friends","DOB":"03/05/2001"},
       {"Firstname":"kila","Phno":9854298725,"Email_id":"123@gmail.com","Groups":"Family","DOB":"08/04/2001"},                                  
       {"Firstname":"anni","Phno":9987948725,"Email_id":"abc@gmail.com","Groups":"Friends","DOB":"03/05/2001"},
       {"Firstname":"hila","Phno":9854288725,"Email_id":"123@gmail.com","Groups":"Family","DOB":"08/04/2001"},                                  
       {"Firstname":"dhii","Phno":9854238725,"Email_id":"123@gmail.com","Groups":"Family","DOB":"08/04/2001"}])
for i in phone:
    print(i)
