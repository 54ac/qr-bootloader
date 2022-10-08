"""convert qr codes into codepage 437 ascii - uses asciiqr.com"""

import argparse
import requests
from requests.exceptions import HTTPError
from bs4 import BeautifulSoup

PARSER = argparse.ArgumentParser(description="convert qr codes into codepage 437 ascii - uses asciiqr.com")
PARSER.add_argument("--hex", help="print output as hex values", action="store_true")
PARSER.add_argument("-n", "--nasm", help="print output as a nasm-ready string of hex values", action="store_true")
PARSER.add_argument("-o", "--out", metavar="FILE", help="print output to specified file")
PARSER.add_argument("-s", "--strip", help="remove newlines", action="store_true")
PARSER.add_argument("--skip-cr", help="do not add carriage return (when -s is not used)", action="store_true")
PARSER.add_argument("-u", "--url", help="treat input as a url to an existing qr code", action="store_true")
PARSER.add_argument("--utf8", help="convert to utf-8 instead of codepage 437", action="store_true")
PARSER.add_argument("input", help="string to be converted into an ascii qr code")
ARGS = PARSER.parse_args()

# used by website to discern type of input
if ARGS.url:
    MODE = "i"
else:
    MODE = "t"

if ARGS.utf8:
    CP = "utf-8"
    STRIPHEX = b"\xc2\xa0\x0a\xc2\xa0"
else:
    CP = "cp437"
    STRIPHEX = b"\xff\x0a\xff"

if ARGS.skip_cr:
    CR = b"\x0a"
else:
    CR = b"\x0d\x0a"

try:
    RESPONSE = requests.get(f"http://asciiqr.com/index.php?{MODE}=&t={ARGS.input}")

    RESPONSE.raise_for_status()
except HTTPError as http_err:
    print(f"http error: {http_err}")
except Exception as err:
    print(f"other error: {err}")
else:
    SOUP = BeautifulSoup(RESPONSE.text, "html.parser")
    CODE = SOUP.find("div", id="QRAscii")
    if not CODE:
        raise Exception("soup error: no qr code data found")
    CODE = CODE.get_text().strip().encode(CP)

# removes unnecessary characters before and after newline and adds carriage returns
if ARGS.strip:
    CODE = CODE.replace(STRIPHEX, b"")
else:
    CODE = CODE.replace(STRIPHEX, CR)

if ARGS.hex or ARGS.nasm:
    if ARGS.nasm:
        # beautifies output
        CODE = "0x" + ", 0x".join(f"{b:02x}".upper() for b in CODE) + ", 0x00"
    else:
        CODE = CODE.hex()
    if ARGS.out:
        F = open(ARGS.out, "w+")
        F.write(CODE)
    else:
        print(CODE)
else:
    if ARGS.out:
        # binary file instead of text file for writing bytes directly
        F = open(ARGS.out, "wb")
        F.write(CODE)
    else:
        print(CODE.decode(CP))
