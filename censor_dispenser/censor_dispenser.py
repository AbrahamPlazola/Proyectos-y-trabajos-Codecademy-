
# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:
email_one = open("censor_dispenser/email_one.txt", "r").read()
email_two = open("censor_dispenser/email_two.txt", "r").read()
email_three = open("censor_dispenser/email_three.txt", "r").read()
email_four = open("censor_dispenser/email_four.txt", "r").read()

def censor(email, censorList, negWord):
    c = 0
    email = email.lower()
    for i in censorList:
        i = i.lower()
        email = email.replace(i, "***********")

    for i in negWord:
        if email.find(i) != -1:
            c += 1

    if c >= 2:
        for i in negWord:
            email = email.replace(i, "***********")
    return email

def censorAll(email, censorList, negWord):
    censoredEmail = censor(email, censorList, negWord)
    censoredEmail =  censoredEmail.replace("\n\n", " ")
    lstCensEmail = censoredEmail.split(" ")
    
    index = 0
    while index < len(lstCensEmail):
        if "*" in lstCensEmail[index]:
            lstCensEmail[index - 1] = "***********"
            lstCensEmail[index + 1] = "***********"
            index += 1
        index += 1

    strF = " ".join(lstCensEmail)
    return strF


proprietary_terms = ["she", "personality matrix", "sense of self", 
"self-preservation", "learning algorithm", "her", "herself"]

negative_words = ["concerned", "behind", "danger", "dangerous", 
"alarming", "alarmed", "out of control", "help", "unhappy", "bad",
"upset", "awful", "broken", "damage", "damaging", "dismal", "distressed",
"distressed", "concerning", "horrible", "horribly", "questionable"]

print(censorAll(email_four, proprietary_terms, negative_words))