n=input("enter no.f time slots:  ")
s=[]
t=[]
e=[]
i=0
while i<n:
        s.append(input("enter rating for network A show:  "))
        if i==0:
                x=s[i]
        elif x<s[i]:
                x=s[i]  
        i=i+1
i=0
while i<n:
        t.append(input("enter rating for network B show:  "))
        if i==0:
                y1=t[i]
        elif y1<t[i]:
                y1=t[i]  
        i=i+1
def m():
        i=0
        w=0
        y=0
        while i<n:
                j=0
                c1=0
                c2=0
                while j<n:
                        if s[i]>t[j]:
                                c1=c1+1
                        elif s[i]<t[j]:
                                c2=c2+1
                        else:
                                print("not stable")
                                return 
                        j=j+1
                if c1!=n:
                        if c2!=n:       
                                print("not stable")
                                return                        
                if c1==n:
                        w=w+1
                if c2==n:
                        y=y+1
                i=i+1
        
        print("stable")
        if x>y1:
                print "network A win",w,"slots"
                print "network B win",y,"slots"
        else:
                print "network A win",y,"slots"
                print "network B win",w,"slots"
if x>y1:
        m()
elif x<y1:
        e=s
        s=t
        t=e
        m()
        
        
                
