variants = (".ru", ".com", ".net")

def send_email(string, recipient, sender = "university.help@gmail.com") :
    if "@" not in sender or not sender.endswith(variants) or ' ' not in sender :
        print("Невозможно отправить письмо с адреса", sender,  "на адрес", recipient + ".")
    elif recipient == sender :
        print("Нельзя отправить письмо самому себе!")
    elif sender == "university.help@gmail.com" :
        print("Письмо успешно отправлено с адреса", sender, "на адрес", recipient + ".")
    else :
        print("НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса", sender, "на адрес" + recipient + ".")


email = input("Введите почту отправителя или пробел:")
send_to = None
while send_to == None :
    check = input("Введите почту получателя: ")
    if "@" in check and check.endswith(variants) and ' ' not in check:
        send_to = check
        break
    else :
        print("Некорректно введённый адрес! Используйте адреса (.ru/.com/.net")
        continue



content = input("Введите сообщение: ")

if email == " " :
    send_email(content, send_to)
else :
    send_email(content, send_to, email)