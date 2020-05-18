#!/usr/bin/env python
# coding: utf-8

# In[ ]:


arr =[1,2,3,4,3,3,2,1]
a=min(arr)

s=len(arr)
li1= []
d=0
print(a)
while(s>=0):
    a=min(arr)
    li=[]
    
    for i in range(len(arr)):
        c= arr[i]-a
        if(c!=0):
            li.append(c)
    s=len(li)
    print(s)
            
    
   


# In[ ]:




