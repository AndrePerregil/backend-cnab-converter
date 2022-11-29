import ipdb

def decode_data(str):
    result = ""
    error = "not CNAB"
    type_encoded = str[0:1]

    """Checking if str starts with a number from 1 to 9, and has a lenght of 80 or 82 
    (not sure why, but the last line always has a length of 80 in the CNAB example provided)"""
    
    if (
        len(str) > 82 
        or len(str) < 80 
        or type_encoded == "0"
        or not type_encoded.isnumeric()
    ):
        return error
    
    types=[
        ["debit", "income"],
        ["ticket", "expense"],
        ["financing", "expense"],
        ["credit", "income"],
        ["loan", "income"],
        ["sales", "income"],
        ["express transfer, income"],
        ["standart transfer", "income"],
        ["rent", "expense"],
    ]
    
    type_decoded = types[int(type_encoded)-1]
    date_decoded = f'{str[1:5]}-{str[5:7]}-{str[7:9]}'
    cpf_decoded = str[19:30]    
    card_decoded = str[30:42]
    time_decoded = f'{str[42:44]}:{str[44:46]}:{str[46:48]}'
    owner_decoded = str[48:62]
    bussiness_decoded = str[62:80]
    
    value_decoded = str[10:19]
    if value_decoded.isnumeric():
        value_decoded = int(str[10:19])/100

    """validating that all data make sense in the context of the application"""

    if (
        not type_encoded.isnumeric()
        #date must be made of integers
        or not (str[1:5] + str[5:7] + str[7:9]).isnumeric()
        #value must be interger
        or not str[10:19].isnumeric()
        #CPF must be integer
        or not cpf_decoded.isnumeric()
        #card_details must be 4 integers enveloping "****"
        or not (str[30:34] + str[38:42]).isnumeric()
        or str[34:38] != "****"
        #time must be interger
        or not (str[42:44] + str[44:46] + str[46:48]).isnumeric()
    ):
        return error
    
    
    return {
        "type": type_decoded[0], 
        "nature": type_decoded[1], 
        "date": date_decoded, 
        "value": value_decoded,
        "cpf": cpf_decoded,
        "card": card_decoded,
        "time": time_decoded,
        "owner": owner_decoded,
        "business": bussiness_decoded ,    
    }
