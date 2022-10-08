
## The QR Code Bootloader
### What is this?
This is a bootloader whose sole function is to display a fully functioning ASCII QR code on a white background. Includes a short Python script which uses [asciiqr.com](http://asciiqr.com/) to convert text strings or existing QR codes into code page 437 (or UTF-8) strings or hex values.

### What is this written in?
Assembly (NASM) and Python.

### What's the point?
None, really. Reawakening the basic knowledge of assembly laying dormant somewhere in my brain for eons.

### How do I use this?
1. Replace `qr_string db` with your own QR code using ascii.py (optional),
2. Compile using NASM (or whatever works, I suppose),
3. Use it as the boot sector on a CD, USB drive, SD card, floppy disk, etc.
4. Boot from said media,
5. Scan QR code (optional).

---

### Full output of python ascii.py -h:
```
usage: ascii.py [-h] [--hex] [-n] [-o FILE] [-s] [--skip-cr] [-u] [--utf8] input

convert qr codes into codepage 437 ascii - uses asciiqr.com

positional arguments:
  input                string to be converted into an ascii qr code

optional arguments:
  -h, --help           show this help message and exit
  --hex                print output as hex values
  -n, --nasm           print output as a nasm-ready string of hex values
  -o FILE, --out FILE  print output to specified file
  -s, --strip          remove newlines
  --skip-cr            do not add carriage return (when -s is not used)
  -u, --url            treat input as a url to an existing qr code
  --utf8               convert to utf-8 instead of codepage 437
```

---

### Future plans and things to do
- [ ] Become a famous musician,
- [ ] Record an album,
- [ ] Include this as the boot sector on the CD release of the album by using mixed mode discs:
	- [ ] The data track would contain the boot sector, but no files (which is still compatible with the El Torito bootable CD spec),
	- [ ] The audio track would contain the actual album.
- [ ] Use the QR code shown by the bootloader to provide additional content (e.g. songs).
