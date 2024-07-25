import subprocess

def download_video(url, download_type, quality, subtitle_option, subtitle_lang, location, playlist_start, playlist_end, progress_callback):
    # Build yt-dlp command
    cmd = ["yt-dlp", url, "-f", f"bestvideo[height<={quality}]+bestaudio/best[height<={quality}]", "--newline"]

    if download_type == "Playlist":
        if playlist_start:
            cmd.extend(["--playlist-start", playlist_start])
        if playlist_end:
            cmd.extend(["--playlist-end", playlist_end])

    if subtitle_option == "Embedded":
        cmd.extend(["--write-auto-sub", "--sub-lang", subtitle_lang, "--embed-subs"])
    elif subtitle_option == "Separate":
        cmd.extend(["--write-sub", "--sub-lang", subtitle_lang])

    cmd.extend(["-o", f"{location}/%(title)s.%(ext)s"])

    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    for line in process.stdout:
        print(line)  # For debugging, remove in production
        if "download" in line.lower():
            try:
                progress = float(line.split('%')[0].split()[-1])
                progress_callback(progress)
            except ValueError:
                pass

    process.wait()
    if process.returncode != 0:
        raise subprocess.CalledProcessError(process.returncode, cmd)
