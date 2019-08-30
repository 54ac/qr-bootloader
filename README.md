
## The QR Code Bootloader
### What is this?
This is a bootloader whose sole function is to display a fully functioning ASCII QR code on a white background.

### What is this written in?
Assembly (NASM).

### What's the point?
None, really. Reawakening the basic knowledge of assembly laying dormant somewhere in my brain for eons.

### How do I use this?
1. Replace `qr_string db` with your own QR code (use the [ASCII QR Code Converter](https://github.com/rowrawer/qr-ascii) (optional),
2. Compile using NASM (or whatever works, I suppose),
3. Use it as the boot sector on a CD, USB drive, SD card, floppy disk, etc.
4. Boot from said media,
5. Scan QR code (optional).

---

### Future plans and things to do
- [ ] Become a famous musician,
- [ ] Record an album,
- [ ] Include this as the boot sector on the CD release of the album by using mixed mode discs:
	- [ ] The data track would contain the boot sector, but no files (which is still compatible with the El Torito bootable CD spec),
	- [ ] The audio track would contain the actual album.
- [ ] Use the QR code shown by the bootloader to provide additional content (e.g. songs).
