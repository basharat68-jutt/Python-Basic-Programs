"""Q7-Validate Input : keep asking the user for input untill theu enter
a number between 1 and 10."""

while True: #jb tk user theek input nehein deta tb tk pochty rhna hai
    number = int(input("enter value between 1 and 10: "))

    if 1<= number <= 10:
        print("thanks")
        break
    else:
        print("invalid number,try again")
