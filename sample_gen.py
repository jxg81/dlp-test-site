import random
import json
import csv
import pandas as pd
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, landscape
from io import StringIO, BytesIO
from faker import Faker

fake = Faker()
cc_type_allowed = ['amex', 'visa', 'mastercard']    

def credit_card_gen(qty: int, cc_types: list = cc_type_allowed) -> list:
    cc_types = [cc for cc in cc_types if cc in cc_type_allowed]
    output: list = []
    for _ in range(qty):
        card = fake.credit_card_full(random.choice(cc_types))
        card = card.splitlines()
        card_dict = {'type': card[0], 'name': card[1], 'number': card[2].split(' ')[0], 'expiry': card[2].split(' ')[1], 'cvc': card[3].split(' ')[1]}
        output.append(card_dict)
    return output

def pii_gen(qty: int) -> list:
    output: list = []
    for _ in range(qty):
        profile = fake.profile()
        del profile['current_location']
        del profile['website']
        profile['birthdate'] = str(profile['birthdate'])
        profile['address'] = profile['address'].replace("\n", " ")
        profile['residence'] = profile['residence'].replace("\n", " ")
        output.append(profile)
    return output

def bank_gen(qty: int) -> list:
    output: list = []
    for n in range(qty):
        iban=fake.iban()
        company=fake.company()
        output.append({'company': company, 'iban': iban})
    return output

def cc_and_pii(qty: int) -> list:
    cc_data = credit_card_gen(qty)
    pii_data = pii_gen(qty)
    count = qty -1
    output: list = []
    while count > 0:
        output.append(cc_data[count] | pii_data[count])
        count -= 1
    return output

def csv_formatter(content: list[dict]):
    fieldnames = content[0].keys()
    file = StringIO()
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(content)
    return file

def text_formatter(content: list[dict]):
    data = csv_formatter(content)
    data.seek(0)
    data_frame = pd.read_csv(data)
    file = StringIO(data_frame.to_string(header=True, index=False))
    return file

def pdf_formatter(content: list[dict]):
    file = BytesIO()
    c = canvas.Canvas(file, pagesize=landscape(A4))
    t = c.beginText()
    t.setFont('Helvetica', size=4.8)
    t.setTextOrigin(10, 588)
    t.textLine(" ".join(content[0].keys()))
    for record in content:
        text = " ".join(record.values())
        t.textLine(text)
    c.drawText(t)
    c.save()
    return file

def json_formatter(content: list[dict]) -> StringIO:
    file = StringIO(json.dumps(content))
    return file

def data_generator(data_type: str, output_format: str, qty: int):
    def string_to_bytes(string_file):
        bytes_file = BytesIO()
        bytes_file.write(string_file.getvalue().encode())
        return bytes_file
    
    if data_type == 'cc':
        content = credit_card_gen(qty)
    elif data_type == 'pii':
            content = pii_gen(qty)
    if data_type == 'cc+pii':
        content = cc_and_pii(qty)
    elif data_type == 'bank':
            content = bank_gen(qty)
            
    if output_format == 'csv':
            string_file = csv_formatter(content)
            bytes_file = string_to_bytes(string_file)
    if output_format == 'pdf':
            bytes_file = pdf_formatter(content)
    if output_format == 'json':
            string_file = json_formatter(content)
            bytes_file = string_to_bytes(string_file)
    if output_format == 'txt':
            string_file = text_formatter(content)
            bytes_file = string_to_bytes(string_file)
           
    bytes_file.seek(0)
    return bytes_file
