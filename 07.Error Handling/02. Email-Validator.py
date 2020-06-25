class NameTooShortError(Exception):
    """ Raised when username is 4 symbols or less """
    def __init__(self, message="Name must be more than 4 characters"):
        self.message = message
        super().__init__(message)


class MustContainSymbolError(Exception):
    """ Raised when the email is missing @ """
    def __init__(self, message="Email must contain @"):
        self.message = message
        super().__init__(message)


class InvalidDomainError(Exception):
    """ Raised when email has invalid domain """
    def __init__(self, message="Domain must be one of the following: .com, .bg, .org, .net"):
        self.message = message
        super().__init__(message)


def validate_name(email):
    username = email.split("@")[0]
    if len(username) <= 4:
        raise NameTooShortError()


def validate_at_symbol(email):
    if "@" not in email:
        raise MustContainSymbolError()


def validate_domain(email):
    valid_domains = ("com", "net", "bg", "org")
    email_domain = email.split(".")[-1]
    if email_domain not in valid_domains:
        raise InvalidDomainError()


while True:
    line = input()

    if line == "End":
        break

    validate_name(line)
    validate_at_symbol(line)
    validate_domain(line)

    print("Email is valid")
