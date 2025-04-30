import csv
import ipaddress

input_file = 'tw.csv'
output_file = 'taiwan_mikrotik.rsc'

with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
    reader = csv.reader(infile)
    for row in reader:
        if len(row) >= 2:
            start_ip, end_ip = row[0].strip(), row[1].strip()
            try:
                networks = ipaddress.summarize_address_range(
                    ipaddress.IPv4Address(start_ip),
                    ipaddress.IPv4Address(end_ip)
                )
                for network in networks:
                    outfile.write(f"/ip firewall address-list add address={network} list=taiwan\n")
            except ValueError as e:
                print(f"خطا در پردازش IP {start_ip}-{end_ip}: {e}")

print("✅ فایل اسکریپت میکروتیک با موفقیت ایجاد شد.")
