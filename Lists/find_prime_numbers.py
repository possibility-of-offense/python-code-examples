# JS equivalent 

# let primeNumbers = [];

# for(let i = 2; i <= 20; i++) {
#   let cont = false;
  
#     for(let k = 2; k < i; k++){
       
#         if(i % k === 0) {
#           cont = true;
#           break;
#         } 
#     }
#     if(!cont) {
#       primeNumbers.push(i);
#     }
# }

prime_numbers = []

for num in range(2, 20):
    for x in range(2, num):
        if(num % x == 0):
            break
    else:
        prime_numbers.append(num)

if len(prime_numbers) > 0:
    print('Prime numbers:')
    
    for i in prime_numbers:
        print(i)