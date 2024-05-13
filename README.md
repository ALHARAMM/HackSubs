# DESCRIPTION

HackSubs is an automated tool that made to get all subdomains from crt.sh,sublist3r,subfinder and assetfinder
to save time in BugHunting 

## INSTALLATION

git clone https://github.com/ALHARAMM/HackSubs.git

cd HackSubs
pip install requirements.txt
python3 HackSubs.py

## Usage
HackSubs.py [-h] -d DOMAIN [-o OUTPUT]

options:
  -h, --help            show this help message and exit
  -d DOMAIN, --domain DOMAIN
                        Target Domain.
  -o OUTPUT, --output OUTPUT
                        Output to File.
python3 HackSubs.py -d example.com -o output.txt

Then Enjoy :)

