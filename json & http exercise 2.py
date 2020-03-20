import random
import requests
import json
import html

url = ("https://opentdb.com/api.php?amount=1")
endgame = " "

will = input("Do you like to play quiz game?")
if will.lower() == "yes" :
    qn = 1
    c_n = 0
    ic_n = 0
    while endgame != "quit" :
        r = requests.get(url)
        if  r.status_code != 200 :
            endgame = input("Sorry, there's some error happen, please hit any key to continue :")
        else :
            print("Question ",qn," is :")
            question = json.loads(r.text)
            print(html.unescape(question["results"][0]["question"]))
            c_ans = question["results"][0]["correct_answer"]
            answers = question["results"][0]["incorrect_answers"]
            answers.append(c_ans)
            random.shuffle(answers)
            an = 1
            for ans in answers :
                print(an,". ",html.unescape(ans))
                an = an + 1
                
            valid_ans = False
            while valid_ans == False :
                user_ans = input("Please select the correct answer : ")
                try : 
                    user_ans = int(user_ans) 
                    if user_ans > len(answers) or user_ans <= 0 :
                        print("Your answer can't be bigger than"," ",len(answers), " or less than 0")
                    else :
                        valid_ans = True
                except :
                    print("Your answer is invalid, please input again :")
            user_ans = answers[int(user_ans)-1]
            if user_ans == c_ans :
                print("Congratulations!, you are right. The answer is ", c_ans)
                c_n = c_n + 1
            else :
                print("Sorry, your answer is incorrect, the correct is", c_ans)
                ic_n = ic_n + 1
                
            print("Your correct answer is :", c_n)
            print("your incorrect answer is :", ic_n)

        x = input("Do you like to play again?")
        if x.lower() == "yes" :
            qn = qn +1
        else :
            print("Thank you, see you next time")
            endgame = "quit"
else :
    print("OK, maybe next time")
            







            




                











                        
            
            
