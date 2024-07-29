import qrcode
from tkinter import Tk, Label, Entry, Button, messagebox, Frame
from tkinter import font as tkfont
from PIL import Image, ImageDraw, ImageFont
import os

def generate_qr_codes():
    try:
        start = int(start_entry.get())
        end = int(end_entry.get())
        title = title_entry.get().strip()
        
        if start > end:
            messagebox.showerror("Error", "Starting number must be less than or equal to ending number.")
            return
        
        if not os.path.exists('qr_codes'):
            os.makedirs('qr_codes')

        for i in range(start, end + 1):
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr.add_data(str(i))
            qr.make(fit=True)

            img = qr.make_image(fill='black', back_color='white').convert('RGB')
            
            if title:  # Add title below QR code if provided
                draw = ImageDraw.Draw(img)
                font = ImageFont.load_default()  # Use default font
                text = f"{title} {i}"
                
                # Calculate text size
                text_bbox = draw.textbbox((0, 0), text, font=font)
                text_width = text_bbox[2] - text_bbox[0]
                text_height = text_bbox[3] - text_bbox[1]
                
                # Create a new image with space for the title
                new_img = Image.new('RGB', (img.width, img.height + text_height + 10), 'white')
                new_img.paste(img, (0, 0))
                
                # Draw the title text
                draw = ImageDraw.Draw(new_img)
                draw.text(((new_img.width - text_width) / 2, img.height + 5), text, font=font, fill='black')
                
                img = new_img  # Update img to include title
            else:
                # If no title, keep img as is
                pass
            
            # Save the image
            img.save(f'qr_codes/qr_code_{i}.png')

        messagebox.showinfo("Success", 'QR codes generated and saved in "qr_codes" directory.')
    except ValueError:
        messagebox.showerror("Error", "Please enter valid integers.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Set up the GUI
root = Tk()
root.title("QR Code Generator")
root.geometry("400x250")  # Set a default window size

# Load custom font (optional)
try:
    custom_font = tkfont.Font(family="Helvetica", size=12)
except:
    custom_font = tkfont.Font(size=12)

# Main Frame
main_frame = Frame(root, padx=20, pady=20)
main_frame.pack(expand=True, fill='both')

# Labels and Entries
Label(main_frame, text="Starting Number:", font=custom_font).grid(row=0, column=0, padx=10, pady=10, sticky='e')
start_entry = Entry(main_frame, font=custom_font)
start_entry.grid(row=0, column=1, padx=10, pady=10)

Label(main_frame, text="Ending Number:", font=custom_font).grid(row=1, column=0, padx=10, pady=10, sticky='e')
end_entry = Entry(main_frame, font=custom_font)
end_entry.grid(row=1, column=1, padx=10, pady=10)

Label(main_frame, text="Title (Optional):", font=custom_font).grid(row=2, column=0, padx=10, pady=10, sticky='e')
title_entry = Entry(main_frame, font=custom_font)
title_entry.grid(row=2, column=1, padx=10, pady=10)

# Buttons
generate_button = Button(main_frame, text="Generate QR Codes", font=custom_font, bg='#4CAF50', fg='white', command=generate_qr_codes)
generate_button.grid(row=3, column=0, columnspan=2, pady=20)

root.mainloop()

