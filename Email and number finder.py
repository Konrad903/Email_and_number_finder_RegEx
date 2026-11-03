import re
def file(filepath):
    with open(filepath) as file:
        return file.read()

def e_pattern(text):
    email_pattern=r'(\b[a-zA-Z0-9._+%-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b)'
    return re.findall(email_pattern,text)

def p_pattern(text):
    phone_pattern=r'(\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4})'
    return re.findall(phone_pattern,text)

def main():
    text=file('sample 1.txt')

    emails=e_pattern(text)
    phones=p_pattern(text)

    print('Emails Found:')
    for i in emails:
        print(f' - {i}')
    print('Phone Numbers found:')
    for i in phones:
        print(f' - {i}')    

main()