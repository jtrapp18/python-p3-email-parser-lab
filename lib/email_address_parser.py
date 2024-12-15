# your code goes here!
import re

class EmailAddressParser:

    def __init__(self, email_addresses):
        self.email_addresses = email_addresses

    def parse(self):
        split_code = r",\s*|\s"
        split_regax = re.compile(split_code)

        raw_split = split_regax.split(self.email_addresses)
        raw_unique = set(raw_split)
        validated_emails = [email for email in raw_unique if self.validate_email(email)]

        return sorted(validated_emails)

    def validate_email(self, raw_email):
        email_address = r"[A-z][A-z0-9._-]+@\w+\.[a-z]+"
        email_regex = re.compile(email_address)

        return email_regex.fullmatch(raw_email)

email_addresses = "talk@talk.com john.jones@flatironschool.com alexa@amazon.com"
parser = EmailAddressParser(email_addresses)

print(parser.parse())

