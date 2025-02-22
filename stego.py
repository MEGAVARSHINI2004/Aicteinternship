from PIL import Image

def text_to_binary(text):
    """Convert text to binary with an end delimiter."""
    return ''.join(format(ord(char), '08b') for char in text) + '1111111111111110'  # Delimiter

def binary_to_text(binary):
    """Convert binary back to text until delimiter is found."""
    binary_chars = [binary[i:i+8] for i in range(0, len(binary), 8)]
    message = ""
    for char in binary_chars:
        if char == "11111111":  # Stop at the delimiter
            break
        message += chr(int(char, 2))
    return message

def encode_text(image_path, secret_text, output_path):
    """Encodes a secret text into an image using LSB steganography."""
    
    image = Image.open(image_path).convert("RGB")
    pixels = image.load()
    
    binary_text = text_to_binary(secret_text)
    
    width, height = image.size
    data_index = 0  

    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]

            if data_index < len(binary_text):  
                r = (r & 0xFE) | int(binary_text[data_index])  
                data_index += 1

            if data_index < len(binary_text):  
                g = (g & 0xFE) | int(binary_text[data_index])  
                data_index += 1

            if data_index < len(binary_text):  
                b = (b & 0xFE) | int(binary_text[data_index])  
                data_index += 1
            
            pixels[x, y] = (r, g, b)  

            if data_index >= len(binary_text):  
                break
        if data_index >= len(binary_text):
            break

    if not output_path.lower().endswith(('.png', '.jpg', '.jpeg')):
        output_path += ".png"

    image.save(output_path)  
    print(f"✅ Secret text encoded and saved as: {output_path}")

def decode_text(image_path):
    """Decodes the hidden text from an image."""
    
    image = Image.open(image_path).convert("RGB")
    pixels = image.load()

    width, height = image.size
    binary_text = ""

    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]

            binary_text += str(r & 1)  
            binary_text += str(g & 1)  
            binary_text += str(b & 1)  

    hidden_message = binary_to_text(binary_text)

    print(f"✅ Decoded Message: {hidden_message}")
    return hidden_message

# Example Usage
if __name__ == "__main__":
    original_image = r"C:\Users\megav\OneDrive\Desktop\IBM internship\program\dog.png"  # Ensure the image exists
    secret_message = "Heyy this is MEGAVARSHINI project"
    output_image = r"C:\Users\megav\OneDrive\Desktop\IBM internship\program\dogsteg.png"

    # Encode text into the image
    encode_text(original_image, secret_message, output_image)

    # Decode text from the encoded image
    decode_text(output_image)



