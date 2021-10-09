import yagmail, csv

yag = yagmail.SMTP(user='massmailer69@gmail.com', password='************')
with open('csv.csv') as file:
    reader = csv.reader(file)
    next(reader)
    for name, email, message in reader:
        yag.send(to=email, subject=f'Hey {name}', contents=message)
print("Email sent successfully")
