from datetime import datetime


def generate_sales_report(transactions, enriched_transactions, output_file='output/sales_report.txt'):
    summary = {
        'records': len(transactions),
        'generated': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    with open(output_file, 'w') as f:
        f.write("=" * 45 + "\n")
        f.write("SALES ANALYTICS REPORT\n")
        f.write(f"Generated: {summary['generated']}\n")
        f.write(f"Records Processed: {summary['records']}\n")
        f.write("=" * 45 + "\n\n")

        f.write("API ENRICHMENT SUMMARY\n")
        success = sum(1 for t in enriched_transactions if t['API_Match'])
        total = len(enriched_transactions)

        f.write(f"Total Products Enriched: {success}\n")
        f.write(f"Success Rate: {(success / total) * 100:.2f}%\n")
