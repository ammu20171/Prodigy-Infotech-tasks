import re

password = input("Enter your password: ")

score = 0
feedback = []

# Check length
if len(password) >= 8:
    score += 1
else:
    feedback.append("Password should be at least 8 characters long.")

# Check uppercase letters
if re.search(r"[A-Z]", password):
    score += 1
else:
    feedback.append("Add at least one uppercase letter.")

# Check lowercase letters
if re.search(r"[a-z]", password):
    score += 1
else:
    feedback.append("Add at least one lowercase letter.")

# Check digits
if re.search(r"\d", password):
    score += 1
else:
    feedback.append("Add at least one number.")

# Check special characters
if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
    score += 1
else:
    feedback.append("Add at least one special character.")

# Display password strength
print("\nPassword Strength:")

if score == 5:
    print("Strong")
elif score >= 3:
    print("Medium")
else:
    print("Weak")

# Display feedback
if feedback:
    print("\nSuggestions to improve your password:")
    for item in feedback:
        print("-", item)
else:
    print("Your password meets all the recommended security requirements.")