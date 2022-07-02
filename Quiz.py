print("---------------------------------------------------")
print("           WHO WANTS TO BE A MILLIONAIRE?          ")
print("---------------------------------------------------")
print("Welcome!!")
print("A total of 10 Questions will be asked")
print("For every question correctly answered you would earn an amount")
print("------------------------------------------------------------------")
amount = 0
for i in range(1, 11):
    answer = ""
    if i == 1:
        print("Q1) What is the Capital of Brazil?")
        A = "Rome"
        B = "Sao Paulo"
        C = "Lisbon"
        D = "Rio de Janeiro"
        print("A) Rome")
        print("B) Sao Paulo")
        print("C) Lisbon")
        print("D) Rio de Janeiro")
        answer = input("Enter your Option :  ")
        if answer == "D":
            amount = 1000
            print("Congrats!!!! You move onto the next question")
            print("YOU WON $1000")
            print("--------------------------------------------------------------------")
        else:
            print("Sorry!!!! Wrong answer")
            print("--------------------------------------------------------------------")
            break

    elif i == 2:
        print("Q2) What is 5 multiply by 122")
        A = "598"
        B = "600"
        C = "610"
        D = "608"
        print("A) 598")
        print("B) 600")
        print("C) 610")
        print("D) 608")
        answer = input("Enter your Option :  ")
        if answer == "C":
            amount = 2000
            print("Congrats!!!! You move onto the next question")
            print("YOU WON $2000")
            print("--------------------------------------------------------------------")
        else:
            print("Sorry!!!! Wrong answer")
            print("--------------------------------------------------------------------")
            break

    elif i == 3:
        print("Q3) A Magnet will likely attract which of the following?")
        A = "Metal"
        B = "Plastic"
        C = "Wood"
        D = "The wrong man"
        print("A) Metal")
        print("B) Plastic")
        print("C) Wood")
        print("D) The wrong man")
        answer = input("Enter your Option :  ")
        if answer == "A":
            amount = 4000
            print("Congrats!!!! You move onto the next question")
            print("YOU WON $4000")
            print("--------------------------------------------------------------------")
        else:
            print("Sorry!!!! Wrong answer")
            print("--------------------------------------------------------------------")
            break

    elif i == 4:
        print("Q4) Which two words traditionally appear onscreen at the termination of a feature film?")
        A = "The End"
        B = "The Conclusion"
        C = "The Finish"
        D = "The Pizza Rolls Are Done"
        print("A) The End")
        print("B) The Conclusion")
        print("C) The Finish")
        print("D) The Pizza Rolls Are Done")
        answer = input("Enter your Option :  ")
        if answer == "A":
            amount = 8000
            print("Congrats!!!! You move onto the next question")
            print("YOU WON $8000")
            print("--------------------------------------------------------------------")
        else:
            print("Sorry!!!! Wrong answer")
            print("--------------------------------------------------------------------")
            break

    elif i == 5:
        print("Q5) Which of these pairs of apps offers roughly the same type of service?")
        A = "Snapchat and Grubhub"
        B = "Whatsapp and Youtube"
        C = "TikTok and Spotify"
        D = "Careem and Uber"
        print("A) Snapchat and Grubhub")
        print("B) Whatsapp and Youtube")
        print("C) TikTok and Spotify")
        print("D) Careem and Uber")
        answer = input("Enter your Option :  ")
        if answer == "D":
            amount = 16000
            print("Congrats!!!! You move onto the next question")
            print("YOU WON $16000")
            print("--------------------------------------------------------------------")
        else:
            print("Sorry!!!! Wrong answer")
            print("--------------------------------------------------------------------")
            break

    elif i == 6:
        print("Q6) A person who is not a banker and lends money at an extremely high interest rate is known as what?")
        A = "Loan shark"
        B = "Green snake"
        C = "Paper tiger"
        D = "Brother-in-law"
        print("A) Loan shark")
        print("B) Green snake")
        print("C) Paper tiger")
        print("D) Brother-in-law")
        answer = input("Enter your Option :  ")
        if answer == "A":
            amount = 32000
            print("Congrats!!!! You move onto the next question")
            print("YOU WON $32000")
            print("--------------------------------------------------------------------")
        else:
            print("Sorry!!!! Wrong answer")
            print("--------------------------------------------------------------------")
            break

    elif i == 7:
        print("Q7) A well-known lyric in the holiday song \"Silver Bells\" promises that \"soon it will be\" what?")
        A = "July 4th weekend"
        B = "Halloween night"
        C = "Christmas Day"
        D = "National Burrito Month"
        print("A) July 4th weekend")
        print("B) Halloween night")
        print("C) Christmas Day")
        print("D) National Burrito Month")
        answer = input("Enter your Option :  ")
        if answer == "C":
            amount = 64000
            print("Congrats!!!! You move onto the next question")
            print("YOU WON $64000")
            print("--------------------------------------------------------------------")
        else:
            print("Sorry!!!! Wrong answer")
            print("--------------------------------------------------------------------")
            break

    elif i == 8:
        print("Q8) When a tree is cut down, the part that remains in the ground is called what?")
        A = "Rump"
        B = "Hump"
        C = "Stump"
        D = "Leftovers"
        print("A) Rump")
        print("B) Hump")
        print("C) Stump")
        print("D) Leftovers")
        answer = input("Enter your Option :  ")
        if answer == "C":
            amount = 125000
            print("Congrats!!!! You move onto the next question")
            print("YOU WON $125000")
            print("--------------------------------------------------------------------")
        else:
            print("Sorry!!!! Wrong answer")
            print("--------------------------------------------------------------------")
            break

    elif i == 9:
        print("Q9) According to the proverb, \"Early to bed and early to rise\" makes you \"healthy, wealthy and\" what?")
        A = "Wise"
        B = "Boring"
        C = "Brave"
        D = "Stealthy"
        print("A) Wise")
        print("B) Boring")
        print("C) Brave")
        print("D) Stealthy")
        answer = input("Enter your Option :  ")
        if answer == "A":
            amount = 125000
            print("Congrats!!!! You move onto the next question")
            print("YOU WON $250000")
            print("--------------------------------------------------------------------")
        else:
            print("Sorry!!!! Wrong answer")
            print("--------------------------------------------------------------------")
            break

    else:
        print("Q10) Which of these is a musical instrument?")
        A = "Mandrake"
        B = "Mandalay"
        C = "Mandolin"
        D = "Mandrill"
        print("A) Mandrake")
        print("B) Mandalay")
        print("C) Mandolin")
        print("D) Mandrill")
        answer = input("Enter your Option :  ")
        if answer == "C":
            amount = 500000
            print("Congrats!!!! You move onto the next question")
            print("YOU WON $500000")
            print("--------------------------------------------------------------------")
        else:
            print("Sorry!!!! Wrong answer")
            print("--------------------------------------------------------------------")
            break

print("         THE END")
print("You leave with $" + str(amount))












