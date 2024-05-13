# DESCRIPTION

HackSubs is an automated tool that made to get all subdomains from crt.sh,sublist3r,subfinder and assetfinder
to save time in BugHunting 

## INSTALLATION

git clone https://github.com/ALHARAMM/HackSubs.git

cd HackSubs
pip install requirements.txt
python3 HackSubs.py

## Usage
HackSubs.py [-h] -d DOMAIN [-o OUTPUT] [-a ALLSUBDOMAINS]

options:
  -h, --help            show this help message and exit
  -d DOMAIN, --domain DOMAIN
                        Target Domain.
  -o OUTPUT, --output OUTPUT
                        Output to File.
  -a ALLSUBDOMAINS, --allsubdomains ALLSUBDOMAINS
                        All Subdomains of This Domain.

python3 HackSubs.py -d https://domain.com -a https://domain.com -o output.txt

Then Enjoy :)

