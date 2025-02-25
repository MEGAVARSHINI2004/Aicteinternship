# **Secure Data Hiding in Image Using Steganography**

## **Overview**
This project focuses on **image steganography**, a technique for securely embedding hidden messages within digital images. By utilizing **Python and the PIL (Pillow) library**, the system ensures confidential data transmission while maintaining the image's visual integrity. This method is useful for **cybersecurity, secure communication, and digital forensics**.

## **Features**
- **Text Hiding & Extraction** – Encrypts and embeds secret messages in images.
- **Secure & Undetectable** – Uses pixel manipulation techniques to hide data without noticeable changes.
- **Encryption for Extra Security** – Adds an additional layer of security before embedding data.
- **User-Friendly Interface** – Simple command-line interaction for encoding and decoding.
- **Support for Multiple Image Formats** – Works with PNG, JPEG, and BMP files.

## **Technologies Used**
- **Programming Language:** Python
- **Libraries:** Pillow (PIL), OS, NumPy
- **Platform:** Windows/Linux

## **Installation**
1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/steganography-project.git
   ```
2. Navigate to the project folder:
   ```sh
   cd steganography-project
   ```
3. Install required dependencies:
   ```sh
   pip install pillow numpy
   ```
4. Run the script:
   ```sh
   python stegano.py
   ```

## **Usage**
### **Encoding a Message into an Image**
```sh
python stegano.py encode input_image.png "Your Secret Message" output_image.png
```
- `input_image.png` – The original image
- `"Your Secret Message"` – The text to be hidden
- `output_image.png` – The output image with the hidden message

### **Decoding a Message from an Image**
```sh
python stegano.py decode output_image.png
```
- `output_image.png` – The encoded image from which to extract the hidden message

## **Future Scope**
- **AI-based steganalysis resistance** to improve security.
- **Support for file hiding** (e.g., PDF, audio, video).
- **Cloud-based steganography** for remote secure data transmission.
- **Integration with real-time messaging platforms**.

## **Contributors**
- **Megavarshini A** – Project Lead & Developer

## **Acknowledgments**
Special thanks to **Edunet foundation collab with IBM Internship Program** for providing the opportunity to explore cybersecurity and steganography techniques.

