from src.MailGrabber import MailGrabber
import time

with MailGrabber() as mail:
    mail.show_intro()
    mail.go_to_gmail("https://accounts.google.com/v3/signin/identifier?dsh=S1225616175%3A1678737332875395&authuser=0"
                     "&continue=https%3A%2F%2Fmail.google.com&ec=GAlAFw&hl=en-GB&service=mail&flowName=GlifWebSignIn"
                     "&flowEntry=AddSession")
    # mail.get_email_field("//input[@id='identifierId']",
      #                   int(input("Enter Numbers: = > ")), int(input("How many times you want to try? => ")))

    mail.start_grabbing("//input[@id='identifierId']", "01765792357", 10, 8)

# schedule.every(1).minutes.do(execute)


