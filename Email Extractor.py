import re

def extract_emails(input_file, output_file):
    try:
        with open(input_file, 'r') as f:
            content = f.read()

        email_pattern = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
        emails = re.findall(email_pattern, content)

        if emails:
            print("\n📧 Emails found:")
            for email in emails:
                print(email)

            with open(output_file, 'w') as f_out:
                for email in emails:
                    f_out.write(email + '\n')
            print(f"\n✅ {len(emails)} email(s) also saved to '{output_file}'")
        else:
            print("⚠️ No emails found.")

    except FileNotFoundError:
        print(f"❌ File '{input_file}' not found.")

if __name__ == "__main__":
    input_filename = input("Enter the input file name (e.g., sample.txt): ")
    output_filename = input("Enter the output file name (e.g., emails.txt): ")
    extract_emails(input_filename, output_filename)

