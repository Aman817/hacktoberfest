# Python program for implementation of Selection Sort 
import sys 
X = [100, 56, 24, 76, 11,1,30,46,67,78,90] 
  

for i in range(len(X)): 
      
    
    min_idx = i 
    for j in range(i+1, len(X)): 
        if X[min_idx] > X[j]: 
            min_idx = j 
              
           
    X[i], X[min_idx] = X[min_idx], X[i] 
  

print ("Sorted array") 
for i in range(len(X)): 
    print("%d" %X[i]),  
    
    
