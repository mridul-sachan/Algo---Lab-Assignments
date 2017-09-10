QUESTION 1:
SOLUTION:


n=int(input("Enter total no. of time slots:  "))
network_A_list=[]
network_D_list=[]
temp_list=[]
i=0
while i<n:
       network_A_list.append(input("Enter ratings for network A show:  "))
       if i==0:
               x=network_A_list[i]
       elif x<network_A_list[i]:
               x=network_A_list[i]  
       i=i+1
i=0
while i<n:
       network_D_list.append(input("Enter ratings for network B show:  "))
       if i==0:
               y1=network_D_list[i]
       elif y1<network_D_list[i]:
               y1=network_D_list[i]  
       i=i+1
def matching():
       i=0
       w=0
       y=0
       while i<n:
               j=0
               count1=0
               count2=0
               while j<n:
                       if network_A_list[i]>network_D_list[j]:
                               count1=count1+1
                       elif network_A_list[i]<network_D_list[j]:
                               count2=count2+1
                       else:
                               print("Its not stable")
                               return 
                       j=j+1
               if count1!=n:
                       if count2!=n:       
                               print("Its not stable")
                               return                        
               if count1==n:
                       w=w+1
               if count2==n:
                       y=y+1
               i=i+1
       
       print("It is stable matching")
       if x>y1:
               print("Network A win",w,"slots")
               print("Network D win",y,"slots")
       else:
               print("Network A win",y,"slots")
               print("Network D win",w,"slots")
if x>y1:
       matching()
elif x<y1:
       temp_list=network_A_list
       network_A_list=network_D_list
       network_D_list=temp_list
       matching()

