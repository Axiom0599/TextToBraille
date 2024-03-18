def braille_converter(text):
  braille_alphabets = {
      "a": "⠁",
      "b": "⠃",
      "c": "⠉",
      "d": "⠙",
      "e": "⠑",
      "f": "⠋",
      "g": "⠛",
      "h": "⠓",
      "i": "⠊",
      "j": "⠚",
      "k": "⠅",
      "l": "⠇",
      "m": "⠍",
      "n": "⠝",
      "o": "⠕",
      "p": "⠏",
      "q": "⠟",
      "r": "⠗",
      "s": "⠎",
      "t": "⠞",
      "u": "⠥",
      "v": "⠧",
      "w": "⠺",
      "x": "⠭",
      "y": "⠽",
      "z": "⠾",
  }

  braille_text = ""
  for letter in text:
    braille_text += braille_alphabets[letter]

  return braille_text


text = str(input("Enter a text"))
braille_text = braille_converter(text)

print(braille_text)