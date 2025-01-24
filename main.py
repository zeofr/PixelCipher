import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog
from PIL import Image

def encode_message(image_path, message):
    image = Image.open(image_path)
    if image.mode != 'RGB':
        image = image.convert('RGB')
    
    encoded_image = image.copy()
    width, height = image.size
    pixels = encoded_image.load()

    message_length = len(message)
    max_message_length = (width * height * 3) // 8 - 4
    if message_length > max_message_length:
        raise ValueError("Message is too long to fit in the selected image.")

    binary_message = ''.join([format(ord(char), '08b') for char in message])
    binary_message_length = format(message_length, '032b')
    binary_data = binary_message_length + binary_message

    data_index = 0
    for y in range(height):
        for x in range(width):
            if data_index >= len(binary_data):
                break
            r, g, b = pixels[x, y]
            if data_index < len(binary_data):
                r = (r & ~1) | int(binary_data[data_index])
                data_index += 1
            if data_index < len(binary_data):
                g = (g & ~1) | int(binary_data[data_index])
                data_index += 1
            if data_index < len(binary_data):
                b = (b & ~1) | int(binary_data[data_index])
                data_index += 1
            pixels[x, y] = (r, g, b)

    return encoded_image

def decode_message(image_path):
    image = Image.open(image_path)
    if image.mode != 'RGB':
        image = image.convert('RGB')

    width, height = image.size
    pixels = image.load()

    binary_message_length = ''
    data_index = 0
    for y in range(height):
        for x in range(width):
            if data_index >= 32:
                break
            r, g, b = pixels[x, y]
            binary_message_length += str(r & 1)
            data_index += 1
            if data_index < 32:
                binary_message_length += str(g & 1)
                data_index += 1
            if data_index < 32:
                binary_message_length += str(b & 1)
                data_index += 1
        if data_index >= 32:
            break

    message_length = int(binary_message_length, 2)

    binary_message = ''
    data_index = 0
    for y in range(height):
        for x in range(width):
            if data_index >= (message_length * 8) + 32:
                break
            r, g, b = pixels[x, y]
            if data_index >= 32:
                binary_message += str(r & 1)
            data_index += 1
            if data_index >= 32 and data_index < (message_length * 8) + 32:
                binary_message += str(g & 1)
            data_index += 1
            if data_index >= 32 and data_index < (message_length * 8) + 32:
                binary_message += str(b & 1)
            data_index += 1
        if data_index >= (message_length * 8) + 32:
            break

    message = ''
    for i in range(0, len(binary_message), 8):
        byte = binary_message[i:i+8]
        if len(byte) == 8:
            message += chr(int(byte, 2))

    return message

def encode_image():
    image_path = filedialog.askopenfilename(title="Select Image", filetypes=[("Image Files", ".png;.bmp")])
    if not image_path:
        return

    message = simpledialog.askstring("Input", "Enter the message to encode:")
    if not message:
        return

    try:
        encoded_image = encode_message(image_path, message)
        save_path = filedialog.asksaveasfilename(title="Save Encoded Image", defaultextension=".png", filetypes=[("PNG Files", "*.png")])
        if save_path:
            encoded_image.save(save_path)
            messagebox.showinfo("Success", "Image encoded and saved successfully!")
    except ValueError as e:
        messagebox.showerror("Error", str(e))

def decode_image():
    image_path = filedialog.askopenfilename(title="Select Image", filetypes=[("Image Files", ".png;.bmp")])
    if not image_path:
        return

    try:
        message = decode_message(image_path)
        messagebox.showinfo("Decoded Message", message)
    except Exception as e:
        messagebox.showerror("Error", "Failed to decode message: " + str(e))

def main():
    root = tk.Tk()
    root.title("Steganographic Encoder/Decoder")
    root.geometry("400x300")
    root.config(bg="#2e2e2e")

    custom_font = ("Courier", 14)

    # Create buttons using pack with padding
    encode_button = tk.Button(root, text="Encode Image", command=encode_image, width=20, height=2, font=custom_font, bg="#333", fg="#00ff00", relief="flat")
    encode_button.pack(pady=20)

    decode_button = tk.Button(root, text="Decode Image", command=decode_image, width=20, height=2, font=custom_font, bg="#333", fg="#00ff00", relief="flat")
    decode_button.pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    main()
