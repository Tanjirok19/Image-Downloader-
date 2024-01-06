import os
import requests
import tkinter as tk
from tkinter import Entry, messagebox
from urllib.parse import urlparse
from PIL import Image
from io import BytesIO

def download_image(url):
    try:
        # Make a request to the image URL
        response = requests.get(url)
        response.raise_for_status()

        # Check if the URL points to an image
        content_type = response.headers.get('content-type')
        if content_type and content_type.startswith('image'):
            # Create a directory to save the image
            save_path = os.path.join(os.getcwd(), "downloaded_images")
            os.makedirs(save_path, exist_ok=True)

            # Get the image filename from the URL
            parsed_url = urlparse(url)
            image_filename = os.path.basename(parsed_url.path)
            save_location = os.path.join(save_path, image_filename)

            # Save the image
            with open(save_location, "wb") as f:
                f.write(response.content)

            # Open the downloaded image using PIL to confirm it's a valid image
            Image.open(BytesIO(response.content)).show()

            messagebox.showinfo("Download Complete", f"Image downloaded successfully to {save_location}")
        else:
            messagebox.showerror("Error", "The provided URL does not point to an image.")

    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Create the main window
root = tk.Tk()
root.title("Image Downloader")

# Create GUI components
label = tk.Label(root, text="Enter Image URL:" , font=('Arial',10))
entry = Entry(root, width=30)
download_button = tk.Button(root, text="Download Image",font=('Arial',10 ), command=lambda: download_image(entry.get()))


# Place GUI components in the window
label.pack(pady=10)
entry.pack(pady=10)
download_button.pack(pady=20)

# Run the Tkinter event loop
root.mainloop()
