import re
phone_pattern = r"(\+)?\d(-)?(\d+)(-|.)?(\d+)(-|.)?(\d+)(-|.)?\w+"
email_pattern = r"\w+(-|.)?(\w+)?@\w+(-)?(\w+)?(.)\w+"
phone_list = []
email_list = []
with open("potential-contacts.txt", "r")as f:
    text_content = f.read()
matches = re.finditer(phone_pattern, text_content)
for match in matches:
    phone_list.append(match.group())
matches = re.finditer(email_pattern, text_content)
for match in matches:
    email_list.append(match.group())
def phone_filter(phone_list):
    new_phonelist = []
    for numbmer in phone_list:
        new_num = ""
        jump = False
        counter = 0
        for num in numbmer:
            if not jump:
                if counter < 10:    
                    try:
                        num = int(num)
                        if counter == 3 or counter == 6:
                            new_num += "-"
                        new_num += str(num)
                        counter += 1
                    except ValueError:
                        pass
            if num == '+':
                jump = True
            else:
                jump = False      
        if len(new_num) == 11:
            mod_num = "206-"
            new_num = [int(num) for num in new_num if num != "-"]
            counter_in = 1
            for num in new_num:
                if counter_in <= 7:
                    if counter_in == 4:
                        mod_num += "-"
                    mod_num += str(num)
                counter_in += 1
            new_num = mod_num          
        new_phonelist.append(new_num)
    return new_phonelist
phone_list = phone_filter(phone_list)
phone_list.sort()
email_list.sort()
with open("phone_numbers.txt", "w")as f:
    for number in phone_list:
        f.write(number + "\n")
duplicate = []
with open(".emails.txt", "w")as f:
    for email in email_list:
        if email not in duplicate:
            f.write(email + "\n")
            duplicate.append(email)




























# import re

# pattern_phone = r'\d(-)?(\d+)(-|.)?(\d+)(-|.)?(\d+)(-|.)?\w+'

# pattern_email = r"\w+(-|.)?(\w+)?@\w+(-)?(\w+)?(.)\w+"

# phone_num = []

# email = []

# with open("potential-contacts.txt", "r")as f:
#     text_content = f.read()
#     matches = re.finditer(pattern_phone, text_content)
#     for match in matches:
#         phone_num.append(match.group())
    
#     matches2 = re.finditer(pattern_email, text_content)
#     for match in matches2:
#         email.append(match.group())
#     # print(matches)


# # print(email)

# def phone_filter(phone_num):
#     for number in phone_num:
#         new_num = 0
#         jump = False
#         for num in number:
            
#             if not jump:
#                 try:
#                     num = int(num)
#                     new_num += num
#                 except TypeError:
#                     pass

#             if num == '+':
#                 jump = True
#             else:
#                 jump =False
                


