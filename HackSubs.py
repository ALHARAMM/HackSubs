import requests
from urllib.parse import urlparse
import time
import argparse
import sys
from colorama import Fore
import subprocess

version = 2.2

# Subprocess function
def run_subdomain_tools(url, output_file):
    if output_file:
        subprocess.run(['sublist3r', '-d', url, '-o', output_file], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        subprocess.run(['subfinder', '-d', url, '-o', output_file], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        subprocess.run(['assetfinder', '-subs-only', url], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

# Download progress function
def download_progress():
    for i in range(101):
        print(Fore.RESET + f"\r[*][{'=' * (i//5):<20}] {i}%", end='', flush=True)
        time.sleep(0.05)

# Parse command-line arguments
def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--domain', type=str, required=True, help='Target Domain.')
    parser.add_argument('-o', '--output', type=str, help='Output to File.')
    return parser.parse_args()

# Banner function
def banner():
    global version
    print(Fore.LIGHTBLUE_EX,'''
.----------------------------------------------------------------------------.
|.##.....##....###.....######..##....##..######..##.....##.########...######.|
|.##.....##...##.##...##....##.##...##..##....##.##.....##.##.....##.##....##|
|.##.....##..##...##..##.......##..##...##.......##.....##.##.....##.##......|
|.#########.##.....##.##.......#####.....######..##.....##.########...######.|
|.##.....##.#########.##.......##..##.........##.##.....##.##.....##.......##|
|.##.....##.##.....##.##....##.##...##..##....##.##.....##.##.....##.##....##|
|.##.....##.##.....##..######..##....##..######...#######..########...######.|
'----------------------------------------------------------------------------'
''')
    print(Fore.RESET,'Name: HackSubs')
    print(Fore.RESET,f'Version: {version}')
    print(Fore.RESET,'Copyright: ALHARAM')
    print(Fore.RESET,'Description: The Biggest Automated Tool To Get All Subdomains of a WebSite Domain.')
    time.sleep(1)

# URL parser function
def url_parser(url):
    try:
        host = urlparse(url).hostname
    except Exception as e:
        print('[*] Invalid domain, try again...')
        sys.exit(1)
    return host

# Write subdomains to file
def write_subs_to_file(subdomain, output_file):
    with open(output_file, 'a') as fp:
        fp.write(subdomain + '\n')

# Main function
def main():
    banner()
    subdomains = []
    args = parse_args()
    target = url_parser(args.domain)
    output = args.output
    download_progress()

    # Fetching subdomains from crt.sh
    req = requests.get(f'https://crt.sh/?q=%.{target}&output=json')
    if req.status_code != 200:
        sys.exit(1)
    for (key, value) in enumerate(req.json()):
        subdomain = value['name_value']
        if "none" not in subdomain.lower():  # Exclude entries containing "none"
            subdomains.append(subdomain)

    subs = sorted(set(subdomains))

    # Printing and saving subdomains
    for s in subs:
        print(f'{s}')
        if output is not None:
            write_subs_to_file(s, output)

    # Running subdomain enumeration tools after fetching subdomains
    run_subdomain_tools(args.domain, output)

    print("\n[*] HackSubs is complete, all subdomains have been found.")

if __name__=='__main__':
    main()
