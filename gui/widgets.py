import tkinter as tk
from tkinter import filedialog

class URLFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.url_label = tk.Label(self, text="YouTube URL:")
        self.url_label.grid(row=0, column=0, padx=10, pady=5)
        self.url_entry = tk.Entry(self, width=50)
        self.url_entry.grid(row=0, column=1, padx=10, pady=5)

    def get_url(self):
        return self.url_entry.get()

class TypeFrame(tk.Frame):
    def __init__(self, parent, command):
        super().__init__(parent)
        self.type_label = tk.Label(self, text="Download Type:")
        self.type_label.grid(row=0, column=0, padx=10, pady=5)
        self.type_var = tk.StringVar(value="Single Video")
        self.single_radio = tk.Radiobutton(self, text="Single Video", variable=self.type_var, value="Single Video", command=command)
        self.single_radio.grid(row=0, column=1, padx=120, pady=5, sticky='w')
        self.playlist_radio = tk.Radiobutton(self, text="Playlist", variable=self.type_var, value="Playlist", command=command)
        self.playlist_radio.grid(row=0, column=1, padx=10, pady=5, sticky='e')

    def get_download_type(self):
        return self.type_var.get()

class QualityFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.quality_label = tk.Label(self, text="Video Quality:")
        self.quality_label.grid(row=0, column=0, padx=10, pady=5)
        self.quality_options = ["144p", "240p", "360p", "480p", "720p", "1080p", "1440p", "2160p"]
        self.quality_var = tk.StringVar(value="720p")
        self.quality_menu = tk.OptionMenu(self, self.quality_var, *self.quality_options)
        self.quality_menu.grid(row=0, column=1, padx=10, pady=5)

    def get_quality(self):
        return self.quality_var.get()

class SubtitleFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.subtitle_label = tk.Label(self, text="Subtitles:")
        self.subtitle_label.grid(row=0, column=0, padx=10, pady=5)
        self.subtitle_var = tk.StringVar(value="None")
        self.subtitle_menu = tk.OptionMenu(self, self.subtitle_var, "None", "Embedded", "Separate")
        self.subtitle_menu.grid(row=0, column=1, padx=10, pady=5)

        self.subtitle_lang_label = tk.Label(self, text="Subtitle Language (if applicable):")
        self.subtitle_lang_label.grid(row=1, column=0, padx=10, pady=5)
        self.subtitle_lang_entry = tk.Entry(self, width=20)
        self.subtitle_lang_entry.grid(row=1, column=1, padx=10, pady=5)

    def get_subtitle_options(self):
        return self.subtitle_var.get(), self.subtitle_lang_entry.get()

class LocationFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.location_label = tk.Label(self, text="Save Location:")
        self.location_label.grid(row=0, column=0, padx=10, pady=5)
        self.location_button = tk.Button(self, text="Browse", command=self.browse_location)
        self.location_button.grid(row=0, column=1, padx=10, pady=5, sticky='w')
        self.location_var = tk.StringVar()
        self.location_display = tk.Label(self, textvariable=self.location_var)
        self.location_display.grid(row=0, column=1, padx=10, pady=5, sticky='e')

    def browse_location(self):
        location = filedialog.askdirectory()
        if location:
            self.location_var.set(location)

    def get_location(self):
        return self.location_var.get()

class PlaylistRangeFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.playlist_range_label = tk.Label(self, text="Playlist Range:")
        self.playlist_range_label.grid(row=0, column=0, padx=10, pady=5) 
        self.playlist_start_label = tk.Label(self, text="Start: ") 
        self.playlist_start_label.grid(row=0, column=1, padx=10, pady=5) 
        self.playlist_start_entry = tk.Entry(self, width=5)
        self.playlist_start_entry.grid(row=0, column=2, padx=10, pady=5)
        self.playlist_end_label = tk.Label(self, text="End: ") 
        self.playlist_end_label.grid(row=0, column=3, padx=10, pady=5) 
        self.playlist_end_entry = tk.Entry(self, width=5)
        self.playlist_end_entry.grid(row=0, column=4, padx=10, pady=5) 

    def toggle(self, show):
        if show:
            self.playlist_range_label.grid()
            self.playlist_start_label.grid()
            self.playlist_start_entry.grid()
            self.playlist_end_label.grid() 
            self.playlist_end_entry.grid()
        else:
            self.playlist_range_label.grid_remove()
            self.playlist_start_label.grid_remove() 
            self.playlist_start_entry.grid_remove()
            self.playlist_end_label.grid_remove() 
            self.playlist_end_entry.grid_remove()

    def get_range(self):
        return self.playlist_start_entry.get(), self.playlist_end_entry.get()

class DownloadButton(tk.Frame):
    def __init__(self, parent, command):
        super().__init__(parent)
        self.download_button = tk.Button(self, text="Download", command=command)
        self.download_button.grid(row=0, column=0, padx=10, pady=10)
