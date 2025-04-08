import qrcode

class QRCODE:
    def __init__(self):
        self.qr = qrcode.QRCode(box_size= size, border= padding)
    
    def creating_qr(self,file_name: str,fg: str,bg: str):

        print("!!!WRITE ANYTHING YOU WANT AND GET THE QR CODE!!!")
        user_input: str = input("Enter anything you want")
        
        try:
            self.qr.add_data(user_input)
            qr_image = self.qr.make_image(fill_color=fg, back_color=bg)
            qr_image.save(file_name)
            
            print(f'Successfully created QR code and saved as {file_name}')
        except Exception as e:
            print(f'Error creating QR code: {e}')
            
            
def main():
    myqr = QRCODE(size = 30, padding = 2)
    myqr.creating_qr("sample.png",
                     fg='black',
                     bg='white')
    
if __name__ == "__main__":
    main()
            