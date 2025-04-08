import qrcode
import customtkinter as ctk
from tkinter import filedialog, messagebox

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
            messagebox.showinfo("Success", f"QR Code saved as {file_name}")
        except Exception as e:
            messagebox.showerror("Error", f"Error creating QR code: {e}")

class QRCodeApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("QR Code Generator")
        self.geometry("400x400")

        # Input field for text
        self.label = ctk.CTkLabel(self, text="Enter text for QR Code:")
        self.label.pack(pady=10)
        self.text_input = ctk.CTkEntry(self, width=300)
        self.text_input.pack(pady=10)

        # Input fields for colors
        self.fg_label = ctk.CTkLabel(self, text="Foreground color:")
        self.fg_label.pack(pady=5)
        self.fg_input = ctk.CTkEntry(self, width=200)
        self.fg_input.pack(pady=5)

        self.bg_label = ctk.CTkLabel(self, text="Background color:")
        self.bg_label.pack(pady=5)
        self.bg_input = ctk.CTkEntry(self, width=200)
        self.bg_input.pack(pady=5)

        # Generate button
        self.generate_button = ctk.CTkButton(self, text="Generate QR Code", command=self.generate_qr)
        self.generate_button.pack(pady=20)

        # QRCode instance
        self.qr_generator = QRCODE(size=30, padding=2)

    def generate_qr(self):
        user_input = self.text_input.get()
        fg_color = self.fg_input.get() or "black"
        bg_color = self.bg_input.get() or "white"

        file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
        if not file_path:
            return

        self.qr_generator.create_qr(user_input, file_path, fg_color, bg_color)

if __name__ == "__main__":
    app = QRCodeApp()
    app.mainloop()
