from PIL import Image
import os

#1-bit BMP converter to frames (You can turn a video to frames of your the resolution you wanted using ffmpeg)
#This can also be used for only a single frame.

input_dir = "frames"  # Folder with your 1-bit BMPs
output_file = "output/oled_frames.h"

frame_files = sorted(f for f in os.listdir(input_dir) if f.endswith(".bmp"))

with open(output_file, "w") as out:
    out.write("// Auto-generated OLED frame data for SSD1306\n\n")

    for i, filename in enumerate(frame_files):
        path = os.path.join(input_dir, filename)
        img = Image.open(path).convert("1")  # Confirm 1-bit mode

        if img.size != (128, 64):
            raise ValueError(f"{filename} is not 128x64")

        bytes_out = []
        for y in range(64):
            for x in range(0, 128, 8):
                byte = 0
                for bit in range(8):
                    pixel = img.getpixel((x + bit, y))
                    if pixel == 0:  # Black = on pixel
                        byte |= (1 << (7 - bit))
                bytes_out.append(byte)

        out.write(f"const uint8_t frame{i}[] PROGMEM = {{\n")
        for j in range(0, len(bytes_out), 16):
            line = ", ".join(f"0x{b:02X}" for b in bytes_out[j:j+16])
            out.write(f"  {line},\n")
        out.write("};\n\n")

    out.write("const uint8_t* frames[] PROGMEM = {\n")
    for i in range(len(frame_files)):
        out.write(f"  frame{i},\n")
    out.write("};\n\n")
    out.write(f"#define FRAME_COUNT {len(frame_files)}\n")
