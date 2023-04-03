import tkinter as tk
from tkinter import ttk
from api import get_top_tracks_async
# change tkinter icon


# Create GUI window
root = tk.Tk()
root.title('Top Tracks')
root.geometry('400x400')
root.resizable(False, False)
root.iconbitmap('./assets/pngegg.ico')

# Create input label and box
input_label = ttk.Label(root, text='Enter artist name:')
input_label.pack(side=tk.TOP, pady=10)
input_box = ttk.Entry(root, font=('Helvetica', 14))
input_box.pack(side=tk.TOP, padx=10, pady=5)

# Create search button
search_button = ttk.Button(root, text='Search', command=lambda: get_top_tracks_async(
    input_box.get(), results_box, error_label, search_button))
search_button.pack(side=tk.TOP, pady=10)

# Create error label
error_label = ttk.Label(root, foreground='red')
error_label.pack(side=tk.TOP, pady=5)

# Create results label and box
results_label = ttk.Label(root, text='Results:',
                          font=('Helvetica', 16, 'bold'))
results_label.pack(side=tk.TOP, pady=10)
results_box = tk.Text(root, height=10, width=40, font=(
    'Helvetica', 14), state=tk.DISABLED)
results_box.pack(side=tk.TOP, padx=10, pady=5)

# Run GUI loop
root.mainloop()
