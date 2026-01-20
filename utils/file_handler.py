def read_sales_data(filename):
    """
    Reads sales data from file handling encoding issues
    Returns: list of raw lines (strings)
    """
    encodings = ['utf-8', 'latin-1', 'cp1252']

    for encoding in encodings:
        try:
            with open(filename, 'r', encoding=encoding) as file:
                lines = file.readlines()

            # Remove header & empty lines
            cleaned = [line.strip() for line in lines[1:] if line.strip()]
            return cleaned

        except FileNotFoundError:
            print(f"❌ File not found: {filename}")
            return []
        except UnicodeDecodeError:
            continue

    print("❌ Unable to read file with supported encodings")
    return []

