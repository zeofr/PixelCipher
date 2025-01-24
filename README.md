# PixelCipher

A simple graphical user interface (GUI) tool to encode and decode hidden messages within images using steganography. This project uses Python's `tkinter` library for the GUI, the `Pillow` library for image manipulation, and supports `.png` and `.bmp` image files.


The code hides messages in images by modifying the least significant bits (LSBs) of pixel values to store binary data. During decoding, it reads these bits to reconstruct the hidden message.

## Features
- **Encode Message:** Hide a text message within an image.
- **Decode Message:** Extract the hidden text message from an encoded image.
- User-friendly GUI built with `tkinter`.

---

## Getting Started

Follow these instructions to set up the project on your local machine.

### Prerequisites
Ensure you have Python 3.x installed. If not, download and install it from [python.org](https://www.python.org/).

I would also suggest suggest setting up a python environement just to keep things clean.

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/zeofr/PixelCipher.git
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```


---

## Usage

1. **Run the application:**
   ```bash
   python main.py
   ```

2. **Encode a message into an image:**
   - Click on the `Encode Image` button.
   - Select an image file (`.png` or `.bmp`).
   - Enter the message you want to hide.
   - Save the encoded image.

3. **Decode a message from an image:**
   - Click on the `Decode Image` button.
   - Select the encoded image file.
   - View the hidden message in a popup window.

---

## Project Structure
```
.
├── LICENSE              # MIT License
├── main.py              # Main script with the GUI application
├── requirements.txt     # List of dependencies
└── README.md            # Project documentation
```

---

## Notes
- The image must have enough capacity to store the message. If the message is too long, the application will notify you.
- Only `.png` and `.bmp` files are supported to ensure lossless image quality.

---

## Example

### Encoding a Message:
1. Select an image (e.g., `example.png`).
2. Input a message like `Maki Zenin best`.
3. Save the resulting encoded image as `encoded_example.png`.

### Decoding a Message:
1. Select the encoded image (`encoded_example.png`).
2. View the hidden message (`Maki Zenin best`).
