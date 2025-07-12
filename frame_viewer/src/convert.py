import re
#Converts the Output of frame.py to js, so the viewer can read.

INPUT_FILE = "oled_frames.h"
OUTPUT_FILE = "oled_frames.js"

def parse_frames(header_text):
    # Regex: match `const uint8_t frameX[] PROGMEM = { ... };`
    pattern = re.compile(
        r'const\s+uint8_t\s+(frame\d+)\s*\[\s*\]\s*PROGMEM\s*=\s*\{(.*?)\};',
        re.DOTALL | re.MULTILINE
    )
    matches = pattern.findall(header_text)

    frames = []
    for frame_name, byte_blob in matches:
        # Remove line breaks and split by comma
        byte_blob = byte_blob.replace('\n', '').replace('\r', '')
        byte_list = [b.strip() for b in byte_blob.split(',') if b.strip()]
        frames.append((frame_name, byte_list))

    return frames

def generate_js(frames):
    js = "const frames = [\n"
    for i, (name, bytes_) in enumerate(frames):
        js += f"  // {name}\n  new Uint8Array([{', '.join(bytes_)}]),\n"
    js += "];\n"
    js += "const FRAME_COUNT = frames.length;\n"
    return js

def main():
    with open(INPUT_FILE, 'r', encoding='utf-8') as f:
        header_text = f.read()

    frames = parse_frames(header_text)

    if not frames:
        print("❌ No frames found. Check your oled_frames.h formatting.")
        return

    print(f"✅ Parsed {len(frames)} frames.")

    js_code = generate_js(frames)

    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write(js_code)

    print(f"✅ JavaScript written to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
