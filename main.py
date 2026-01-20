from utils.file_handler import read_sales_data
from utils.data_processor import (
    parse_and_clean_data,
    validate_transactions,
    sales_summary,
    region_wise_performance
)
from utils.api_handler import fetch_all_products, create_product_mapping
from utils.report_generator import generate_sales_report
from utils.save_enriched_data import save_enriched_data


def main():
    try:
        print("=" * 40)
        print("SALES ANALYTICS SYSTEM")
        print("=" * 40)

        print("[1/10] Reading sales data...")
        lines = read_sales_data("data/sales_data.txt")
        print(f"✓ Successfully read {len(lines)} transactions")

        print("[2/10] Parsing and cleaning data...")
        transactions = parse_and_clean_data(lines)

        print("[4/10] Validating transactions...")
        valid, invalid = validate_transactions(transactions)
        print(f"✓ Valid: {len(valid)} | Invalid: {len(invalid)}")

        print("[6/10] Fetching product data from API...")
        products = fetch_all_products()
        mapping = create_product_mapping(products)

        print("[7/10] Enriching sales data...")
        enriched = []
        for t in valid:
            pid = ''.join(filter(str.isdigit, t['ProductID']))
            pid = int(pid) if pid else None

            if pid in mapping:
                t.update({
                    'API_Category': mapping[pid]['category'],
                    'API_Brand': mapping[pid]['brand'],
                    'API_Rating': mapping[pid]['rating'],
                    'API_Match': True
                })
            else:
                t.update({
                    'API_Category': None,
                    'API_Brand': None,
                    'API_Rating': None,
                    'API_Match': False
                })

            enriched.append(t)

        print("[8/10] Saving enriched data...")
        save_enriched_data(enriched)

        print("[9/10] Generating report...")
        generate_sales_report(valid, enriched)

        print("[10/10] Process Complete!")

    except Exception as e:
        print("❌ Error occurred:", e)


if __name__ == "__main__":
    main()

