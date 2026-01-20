def save_enriched_data(enriched_transactions, filename='data/enriched_sales_data.txt'):
    with open(filename, 'w') as f:
        header = (
            "TransactionID|Date|ProductID|ProductName|Quantity|UnitPrice|"
            "CustomerID|Region|API_Category|API_Brand|API_Rating|API_Match\n"
        )
        f.write(header)

        for t in enriched_transactions:
            f.write(
                f"{t['TransactionID']}|{t['Date']}|{t['ProductID']}|"
                f"{t['ProductName']}|{t['Quantity']}|{t['UnitPrice']}|"
                f"{t['CustomerID']}|{t['Region']}|"
                f"{t.get('API_Category')}|{t.get('API_Brand')}|"
                f"{t.get('API_Rating')}|{t['API_Match']}\n"
            )
