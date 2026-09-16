import qrcode
import os

plants = {
    "Grevillea robusta": "https://en.wikipedia.org/wiki/Grevillea_robusta",
}

# Create folder for QR codes
os.makedirs("qr_codes", exist_ok=True)

# Generate QR codes
for index, (plant, link) in enumerate(plants.items(), start=1):
    img = qrcode.make(link)

    filename = f"qr_codes/{index:03d}_{plant.replace(' ', '_')}.png"

    img.save(filename)

    print(f"Generated: {filename}")

print(f"\nDone! Generated {len(plants)} unique QR codes.")