def read_temperatures(filename):
    f1=open(filename,"r")
    #f1=f1.read()
    lst=[]
    for a in f1:
        lst1=[]
        a=a.rstrip()
        a=a.split()
        
        a[0]=int(a[0])
        a[1]=int(a[1])
        a[2]=int(a[2])
        a[3]=float(a[3])
        lst1.append(a[0])
        lst1.append(a[1])
        lst1.append(a[2])
        lst1.append(a[3])
        lst.append(lst1)    
        
    
    return lst



def delete_year(data, year):
    data2=[]
    for i in data:
         if int(i[2])!=year:
             data2.append(i)
        
    return data2



def monthly_averages(data, year):
    lst=[]
    for j in range(1,13):
        summ=0
        count=0
        for i in data:
            if i[2]==year:
                if i[0]==j:
                        if not i[3]==-99:
                            summ+=i[3]
                            count+=1
        avg=summ/count            
        lst.append(avg)                    
                
                        
                
                
            
    return lst



def yearly_average(data):
    f1=open("out.txt","w")
    lst=[]
    for j in range(1995,2020):
        summ=0
        count=0
        for i in data:
                        if not i[3]==-99:
                            summ+=i[3]
                            count+=1
        avg=summ/count       
        avg=format(avg,".2f")
        a=str(j) + "," +str(avg) + "\n"
        f1.write(a)  
    
    


def main():
    """
    The code given here is for you test your functions. You can modify
    it to perform more tests. When submitting, make sure the code you
    leave under main() does not cause a syntax error.
    """
    # Testing Part A
    istanbul_data = read_temperatures("ISTANBUL.txt")
    ankara_data = read_temperatures("ANKARA.txt")
    #print(istanbul_data)
    print(ankara_data)
    
    # Testing Part B
    #istanbul_data = delete_year(istanbul_data, 2020)
    ankara_data = delete_year(ankara_data, 2020)
    #print(istanbul_data)
    print(ankara_data)
    
    # Testing Part C 
    #print(monthly_averages(istanbul_data, 2017))
    print(monthly_averages(ankara_data, 2017))
    
    # Testing Part D
    yearly_average(ankara_data)
  
    
################################################################ 
"""
DO NOT EDIT BELOW THIS LINE
"""
main()
