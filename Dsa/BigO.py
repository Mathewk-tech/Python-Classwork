import time
    

def Calculate_sum(n):
      sum=0
      for numb in range(1,sum+1):
         print(f"sum={sum},numb={numb}")
         sum=sum+numb
      print(f"For {n} The sum is {sum}")
      return sum

def Calculate_sum2(x):
      sum1=0
      
      for numb in range(1,sum1+1):
         print(f"sum={sum1},numb={numb}")
         sum1=sum1+numb
      print(f"For {x} The sum is {sum1}")
      return sum1
def Calculate_sum3(y):
      sum2=0
      for numb in range(1,sum2+1):
         print(f"sum={sum2},numb={numb}")
         sum2=sum2+numb
      print(f"For {y} The sum is {sum2}")
      return sum2

start_time=time.time()
Calculate_sum(2343)
Calculate_sum2(2343)
Calculate_sum3(2343)
end_time=time.time()
diff=end_time-start_time
print(f"Speed {diff}")