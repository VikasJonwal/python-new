import random
Questions = [
    ["Which city is known as Pink City in India?", "Banglore", "Maysore", "Jaipur", "Kochi",3],
    ["Who wrote India's National Anthem?", "Rabindranath Tagore", "Lal Bahadur Shastri", "Chetan Bhagat", "RK Narayan",1],
    ["Where in India Gate located?", "Agra", "Punjab", "Mumbai", "New Delhi",4],
    ["Which of the following is not a state of India?", "Vrindachal", "Goa", "Jharkhand", "Chattisgarh",1],
    ["Which Indian city hosts Indian movie industry?", "Goa", "Mumbai", "Chennai", "Calcutta",2],
    ["Which city is known as the Silicon Valley Of India?", "Delhi", "Mumbai", "Chennai", "Bangalore",4],
]
Levels = [100, 1000, 10000, 100000, 1000000, 10000000]
prizemoney = 0
print("Welcome To Koun Banega Crorepat! \n Powered by Vicky Sir")

for i in range(0, 5):
   
    Question = Questions[random.randrange(0,5)]
    print(f"Here is your First Question for Rupees {Levels[i]} !")
    print(f"Question 1. {Question[0]}")
    print(f'''1.{Question[1]}  2.{Question[2]} \n3.{Question[3]} 4.{Question[4]} ''')
    ans = int(input("Enter Your Answer: "))
    if ans == Question[-1]:
        print(f"Sahiii Jawabbbb! you have won {Levels[i]}")
        prizemoney = prizemoney + Levels[i]
        print(f"your current prize money is {prizemoney}") 
    else:
        print(f" wrong answer ! try on next question \n your prize money stays on {prizemoney}")

