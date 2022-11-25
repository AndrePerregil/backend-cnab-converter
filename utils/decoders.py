def decode_data(str):
    type_encoded = str[0:1]
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
    value_decoded = int(str[10:19])/100
    cpf_decoded = str[19:30]
    card_decoded = str[30:42]
    time_decoded = f'{str[42:44]}:{str[44:46]}:{str[46:48]}'
    owner_decoded = str[48:62]
    bussiness_decoded = str[62:80]

    return {
        "type": type_decoded[0], 
        "nature": type_decoded[1], 
        "date": date_decoded, 
        "value": value_decoded,
        "cpf": cpf_decoded,
        "card": card_decoded,
        "time": time_decoded,
        "owner": owner_decoded,
        "business": bussiness_decoded 
        }
