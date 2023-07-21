import argparse
import dns.resolver
import sys

def print_banner():
    banner = r'''
   / __\ /\ \ \__ _ _ __ ___   ___/ _\_ __   ___   ___  _ __  
 / /   /  \/ / _` | '_ ` _ \ / _ \ \| '_ \ / _ \ / _ \| '_ \ 
/ /___/ /\  / (_| | | | | | |  __/\ \ | | | (_) | (_) | |_) |
\____/\_\ \/ \__,_|_| |_| |_|\___\__/_| |_|\___/ \___/| .__/ 
                                                      |_|                                                                         
Author: 
┳┓┓┏┏┓
┃┃┃┃┏┛
┛┗┗┛┗┛
'''
    print("\033[1;36m" + banner + "\033[0m")


def print_help():
    help_text = '''
CNAME Tracker - Retrieve CNAME of a domain

Usage: python cname_tracker.py [-d DOMAIN] [-l FILE] [-H]

Options:
  -d, --domain DOMAIN  Retrieve CNAME of a single domain
  -l, --list FILE      Retrieve CNAME for multiple domains listed in a file
  -H, --helpmsg        Show help message
  '''
    print(help_text)


def get_cname(domain):
    resolver = dns.resolver.Resolver()
    resolver.nameservers = ['8.8.8.8']  # Use Google Public DNS as the resolver
    try:
        answer = resolver.resolve(domain, 'CNAME')
        cname = answer[0].target.to_text()
        return cname
    except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN, dns.resolver.NoNameservers, dns.resolver.Timeout):
        return None


def process_single_domain(domain):
    cname = get_cname(domain)
    if cname:
        print("\033[1;32m[+]\033[0m CNAME for \033[1m{}\033[0m: {}".format(domain, cname))
    else:
        print("\033[1;31m[-]\033[0m Failed to retrieve CNAME for \033[1m{}\033[0m".format(domain))


def process_multiple_domains(file):
    try:
        with open(file, 'r') as f:
            domains = f.readlines()
    except FileNotFoundError:
        print("\033[1;31m[-]\033[0m File not found: \033[1m{}\033[0m".format(file))
        sys.exit(1)

    for domain in domains:
        domain = domain.strip()
        cname = get_cname(domain)
        if cname:
            print("\033[1;32m[+]\033[0m CNAME for \033[1m{}\033[0m: {}".format(domain, cname))
        else:
            print("\033[1;31m[-]\033[0m Failed to retrieve CNAME for \033[1m{}\033[0m".format(domain))


def main():
    try:
        parser = argparse.ArgumentParser(prog='CNAME Tracker', description='Retrieve CNAME of a domain')
        parser.add_argument('-d', '--domain', metavar='DOMAIN', help='Retrieve CNAME of a single domain')
        parser.add_argument('-l', '--list', metavar='FILE', help='Retrieve CNAME for multiple domains listed in a file')
        parser.add_argument('-H', '--helpmsg', action='store_true', help='Show help message')

        args = parser.parse_args()

        if args.helpmsg:
            print_banner()
            print_help()
            sys.exit()

        if args.domain:
            print_banner()
            process_single_domain(args.domain)

        if args.list:
            print_banner()
            process_multiple_domains(args.list)
    except KeyboardInterrupt:
        print("\n Keyboard Interrupt\n")

if __name__ == '__main__':
    main()
