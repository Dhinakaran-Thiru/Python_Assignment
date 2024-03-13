def is_valid_email(email):

    username, domain = email.split('@')
    website, extension = domain.split('.')
    return all(c.isalnum() or c in ['-', '_'] for c in username) \
           and all(c.isalnum() for c in website) \
           and extension.isalpha() \
           and len(extension) <= 3


def main():
    n = int(input("Enter the number of email addresses: "))
    emails = [input().strip() for _ in range(n)]
    valid_emails = filter_emails(emails)
    print(valid_emails)


def filter_emails(emails):
    return sorted(filter(is_valid_email, emails))
