import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from gui.widgets import URLFrame, TypeFrame, QualityFrame, SubtitleFrame, LocationFrame, PlaylistRangeFrame, DownloadButton
from utils.downloader import download_video
import threading

class YTDownloaderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("YouTube Downloader")
        self.root.geometry('800x600')

        # Initialize frames
        self.url_frame = URLFrame(root)
        self.type_frame = TypeFrame(root, self.toggle_playlist_range)
        self.quality_frame = QualityFrame(root)
        self.subtitle_frame = SubtitleFrame(root)
        self.location_frame = LocationFrame(root)
        self.playlist_range_frame = PlaylistRangeFrame(root)
        self.download_button = DownloadButton(root, self.download_video)

        # Layout frames
        self.url_frame.grid(row=0, column=0, padx=10, pady=5, columnspan=2)
        self.type_frame.grid(row=1, column=0, padx=10, pady=5, columnspan=2)
        self.quality_frame.grid(row=2, column=0, padx=10, pady=5, columnspan=2)
        self.subtitle_frame.grid(row=3, column=0, padx=10, pady=5, columnspan=2)
        self.location_frame.grid(row=4, column=0, padx=10, pady=5, columnspan=2)
        self.playlist_range_frame.grid(row=5, column=0, padx=10, pady=5, columnspan=3)
        self.download_button.grid(row=6, column=0, padx=10, pady=10, columnspan=2)

        # Add progress bar
        self.progress = ttk.Progressbar(root, orient="horizontal", length=400, mode="determinate")
        self.progress.grid(row=7, column=0, padx=10, pady=5, columnspan=3)

        # Initial toggle of playlist range based on default selection
        self.toggle_playlist_range()

    def toggle_playlist_range(self):
        self.playlist_range_frame.toggle(self.type_frame.type_var.get() == "Playlist")

    def download_video(self):
        url = self.url_frame.get_url()
        download_type = self.type_frame.get_download_type()
        quality = self.quality_frame.get_quality()
        subtitle_option, subtitle_lang = self.subtitle_frame.get_subtitle_options()
        location = self.location_frame.get_location()
        playlist_start, playlist_end = self.playlist_range_frame.get_range()

        if not url:
            messagebox.showerror("Error", "Please enter a YouTube URL.")
            return
        if not location:
            messagebox.showerror("Error", "Please select a save location.")
            return

        # Run download in a separate thread to keep the GUI responsive
        threading.Thread(target=self.run_download, args=(url, download_type, quality, subtitle_option, subtitle_lang, location, playlist_start, playlist_end)).start()

    def run_download(self, url, download_type, quality, subtitle_option, subtitle_lang, location, playlist_start, playlist_end):
        # Download the video using utility function
        try:
            download_video(url, download_type, quality, subtitle_option, subtitle_lang, location, playlist_start, playlist_end, self.update_progress)
            messagebox.showinfo("Success", "Download completed successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"Download failed: {e}")

    def update_progress(self, progress):
        self.progress["value"] = progress
        self.root.update_idletasks()
