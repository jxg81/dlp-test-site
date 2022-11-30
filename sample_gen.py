import random
from faker import Faker

fake = Faker()
cc_type_allowed = ['amex', 'visa', 'mastercard']    

def credit_card_gen(qty: int, cc_types: list = cc_type_allowed) -> list:
    cc_types = [cc for cc in cc_types if cc in cc_type_allowed]
    output: list = []
    for n in range(qty):
        output.append(fake.credit_card_full(random.choice(cc_types)))
    return output

def pii_gen(qty: int) -> list:
    output: list = []
    for n in range(qty):
        output.append(fake.profile())
    return output

def bank_gen(qty: int) -> list:
    output: list = []
    for n in range(qty):
        iban=fake.iban()
        company=fake.company()
        output.append({'company': company, 'iban': iban})
    return output

def csv_formatter():
    pass

def text_formatter():
    pass

def pdf_formatter():
    pass

def json_formatter():
    pass

def data_generator(data_type: str['pii', 'bank', 'credit'], output_format: str, qty: int):
    result = None
    return result
    

    
## fake.profile for PII