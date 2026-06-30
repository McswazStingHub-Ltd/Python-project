import qrcode
from datetime import datetime

print("=" * 40)
print("Professional QR Code Generator")
print("=" * 40)

data = input("Enter text or URL: ").strip()

if not data:
    print("Error: You must enter some text.")
    exit()

filename = f"qr_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)

qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save(filename)

print("\nQR Code created successfully!")
print(f"Saved as: {filename}")
