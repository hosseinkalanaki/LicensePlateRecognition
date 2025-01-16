import tkinter as tk
from tkinter import filedialog, messagebox
import Session006 as s
import time

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        # Frame for uploading files
        self.upload_frame = tk.Frame(self)
        self.upload_frame.pack(fill="both", expand=True, padx=10, pady=10)

        self.file_frame = tk.Frame(self.upload_frame)
        self.file_frame.pack()

        self.file_label = tk.Label(self.file_frame, text="File:")
        self.file_label.pack(side="left")

        self.file_entry = tk.Entry(self.file_frame, width=30)
        self.file_entry.pack(side="left")

        self.button_frame = tk.Frame(self.upload_frame)
        self.button_frame.pack(pady=10)

        self.browse_button = tk.Button(self.button_frame, text="Browse", command=self.select_file)
        self.browse_button.pack(side="left", padx=5)

        self.start_button = tk.Button(self.button_frame, text="Start", command=self.start_process)
        self.start_button.pack(side="left", padx=5)

    def select_file(self):
        filename = filedialog.askopenfilename(title="Select File")
        self.file_entry.delete(0, tk.END)
        self.file_entry.insert(0, filename)

    def start_process(self):
        file = self.file_entry.get()

        if not file:
            messagebox.showerror("Error", "Please select a file.")
            return

        processor = FileProcessor(file)
        processor.process()

class FileProcessor:
    def __init__(self, file):
        self.file = file

    def process(self):
        start_time = time.time()
        print(f"Processing started at {time.strftime('%Y-%m-%d %H:%M:%S')}")
        s.session006().track_createHeatmap(self.file)
        end_time = time.time()
        print(f"Processing finished at {time.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Processing time: {end_time - start_time} seconds")

root = tk.Tk()
root.title("File Uploader")
root.geometry("400x200")
app = Application(master=root)
app.mainloop()