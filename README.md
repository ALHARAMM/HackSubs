# DESCRIPTION

HackSubs is an automated tool that made to get all subdomains from crt.sh,sublist3r,subfinder and assetfinder
to save time in BugHunting 

## INSTALLATION

git clone https://github.com/ALHARAMM/HackSubs.git
cd HackSubs
1. Install Python Dependencies
pip install requirements.txt
2. Install External Tools
apt install sublist3r
apt install subfinder
apt install assetfinder
## Usage
python3 HackSubs.py
HackSubs.py [-h] -d DOMAIN [-o OUTPUT]

options:
  -h, --help            show this help message and exit
  -d DOMAIN, --domain DOMAIN
                        Target Domain.
  -o OUTPUT, --output OUTPUT
                        Output to File.
python3 HackSubs.py -d example.com -o output.txt

Then Enjoy :)

