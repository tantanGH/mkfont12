
from PIL import Image, ImageDraw, ImageFont

import argparse

def save_font(font_name, out_file):

  font = ImageFont.truetype(font_name, 12)

  with open(out_file, "wb") as f:

    for i in range(256):
      try:
        utf8_str = i.to_bytes(1,'big').decode('cp932')
        #print(utf8_str)
        img = Image.new("1", (8, 12))
        draw = ImageDraw.Draw(img)
        draw.fontmode = "1"
        draw.text((0, 0), utf8_str, "white", font=font)
        font_data = img.tobytes()
        resize = None
        for x in [7,6]:
          overflow = False
          for y in range(12):
            if font_data[y] & (1 << (7-x)):
              overflow = True
              break
          if overflow:
            resize = x
        if resize == None:
          f.write(font_data)
        else:
          f.write(img.resize((resize,12)).tobytes())
      except UnicodeDecodeError:
        f.write(bytes([0] * 12))      

    for i in range(15+32+47):
      for j in range(94):
        jis_bytes = b"\x1b$B" + (0x2121 + i * 0x100 + j).to_bytes(2,'big') + b"\x1b(B"
        try:
          utf8_str = jis_bytes.decode('iso2022_jp')
          #print(utf8_str)
          img = Image.new("1", (12, 12))
          draw = ImageDraw.Draw(img)
          draw.fontmode = "1"
          draw.text((0, 0), utf8_str, "white", font=font)
          f.write(img.tobytes())
        except UnicodeDecodeError:
          #print(f"skip ... {jis_bytes}")
          f.write(bytes([0] * 24))

def main():
    # command line parameters
    parser = argparse.ArgumentParser()
    parser.add_argument("font_name",help="local font name")
    parser.add_argument("out_file",help="utput font data filename")
    args = parser.parse_args()

    # execute conversion in script mode
    save_font(args.font_name, args.out_file)

if __name__ == "__main__":
    main()