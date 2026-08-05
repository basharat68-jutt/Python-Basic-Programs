"""Q8-password strength checker:check if a password is weak,medium or strong.
Criteria:<6 chars(weak),6-10 chars(medium),>10 chars(strong)"""

password = "security"
password_length = len(password)

if password_length < 6:
    strength = "weak"
elif password_length <= 10:
    strength = "medium"
else:
    strength = "strong"

print("your password length is: " , strength)