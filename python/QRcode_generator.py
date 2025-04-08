import qrcode

class QRCODE:
    def __init__(self, size: int, padding: int):
        self.qr = qrcode.QRCode(box_size=size, border=padding)

    def create_qr(self, user_input: str, file_name: str, fg: str, bg: str):
        """
        Generates a QR code with the given input and saves it to a file.
        """
        try:
            self.qr.add_data(user_input)
            qr_image = self.qr.make_image(fill_color=fg, back_color=bg)
            qr_image.save(file_name)
            print(f'Successfully created QR code and saved as {file_name}')
        except Exception as e:
            print(f'Error creating QR code: {e}')

    def run(self):
        """
        Runs the QR code generator interactively.
        """
        print("!!!WRITE ANYTHING YOU WANT AND GET THE QR CODE!!!")
        user_input: str = input("Enter anything you want: ")
        file_name: str = input("Enter the file name to save the QR code: ") + ".png"
        fg: str = input("Enter the foreground color (default: black): ") or "black"
        bg: str = input("Enter the background color (default: white): ") or "white"

        self.create_qr(user_input, file_name, fg, bg)

if __name__ == "__main__":
    qr_generator = QRCODE(size=30, padding=2)
    qr_generator.run()
