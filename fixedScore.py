def main ():
    score = user_score()
    if score < 0 :
        print("Invalid score")
    elif score > 100 :
        print("Invalid score")
    elif score >= 90 :
        print("Excellent")
    elif score >= 50 :
        print("Passable")
    else :
        print("Bad")


def user_score():
    score = float(input("Enter score"))
    return score


main()




