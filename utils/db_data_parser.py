import ipdb
from utils.handlers import summary_generator

def db_parser(file_data):
    if file_data == "not CNAB":
        return "<h1>Not a valid CNAB file</h1>"
    summary_data = summary_generator()
    data_from_file = ""
    summary = ""
    for entry in file_data:
        line = (
            f"<li>{entry}</li>"
        )
        data_from_file += line

    for entry in summary_data:
        user_business_data = ""
        for business in entry["businesses"]:
            line = (
                f"<li>Name:{business['business_name']} - Balance: R$ {business['business_balance']}</li>"
            )
            user_business_data += line

        line = (
            f"<h4>{entry['username']}</h4>"
            f"<p>Balance: R$ {entry['total_balance']}</p>"
            "<h4>Businesses</h4>"
            f"<ul>{user_business_data}</ul>"
            "</br>"
        )
        summary += line
    
    return (
        "<h2>This is the data that was in the CNAB file</h2>",
        "<ol>",
            data_from_file,
        "</ol>"
        "<h2>This is the balance of the users and their businesses</h2>",
            summary,
        "<h5>Note: The balance takes into account all transactions currently in the DB</h5>"
    )
