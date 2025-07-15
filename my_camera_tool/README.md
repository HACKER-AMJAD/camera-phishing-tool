# Camera & Audio/Video Capture Tool (Termux/PHP)

## Overview
This project provides a discreet, browser-based camera and audio/video capture tool designed for **educational purposes and authorized penetration testing scenarios**. It simulates a benign web application (e.g., a photo editor or video call interface) to demonstrate how modern web browsers handle media permissions and data submission.

## Features
-   **Web-Based Interface:** A user-friendly (and deceptive) web interface (`index.html`) disguised as a common online service.
-   **Camera & Microphone Access:** Requests permissions for the device's camera and microphone, triggering standard browser prompts.
-   **Image Capture:** Captures a single still image (PNG) from the device's camera.
-   **Audio/Video Recording:** Records a short segment of audio and video (WebM format) from the device's microphone and camera.
-   **PHP Backend:** A simple PHP script (`save_data.php`) running on Termux handles receiving and storing the captured images and video/audio files securely on the local device.
-   **Automatic Redirection:** After data capture, the user is automatically redirected to a legitimate website to maintain the illusion and prevent suspicion.
-   **Local Hosting:** Designed to run locally on an Android device using Termux, requiring no external web hosting.

## How it Works
1.  The user opens the crafted web page in their browser.
2.  Upon clicking a deceptive button (e.g., "Capture New Photo" in a photo editor UI), the browser requests camera and microphone permissions.
3.  Once granted, the tool captures a photo and a short video/audio clip.
4.  The captured data is sent via `POST` request to the PHP backend running on Termux.
5.  The PHP script saves the `PNG` image and `WebM` video/audio file to a designated local directory (`captured_data/`).
6.  The browser redirects the user to a pre-defined legitimate website.

## Setup & Usage (on Termux)
1.  **Prerequisites:** Ensure Termux is installed and updated. `php` and `git` are required.
2.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/HACKER-AMJAD/camera-phishing-tool.git](https://github.com/HACKER-AMJAD/camera-phishing-tool.git)
    cd camera-phishing-tool
    ```
3.  **Run the Server:**
    ```bash
    ./run_tool.sh
    ```
    This will start the PHP development server.
4.  **Access the Tool:** Open your browser and navigate to `http://localhost:8080`.
5.  **Retrieve Data:** Captured files are stored in `~/my_camera_tool/captured_data/`. To transfer them to your Android's `Download` folder (accessible by gallery apps), use the following commands:
    ```bash
    cp ~/my_camera_tool/captured_data/*.png ~/storage/shared/Download/
    cp ~/my_camera_tool/captured_data/*.webm ~/storage/shared/Download/
    ```
    *Optional Shortcut for convenience:* You can create a custom shell function (e.g., `todl`) in your `~/.bashrc` file to simplify the copying process. For example:
    ```bash
    # Add to ~/.bashrc
    todl() {
        SOURCE_DIR="$HOME/my_camera_tool/captured_data"
        DEST_DIR="$HOME/storage/shared/Download"
        mkdir -p "$DEST_DIR" 2>/dev/null
        cp "$SOURCE_DIR/$1" "$DEST_DIR/"
        echo "Copied '$1' to '$DEST_DIR/'"
    }
    # Then source ~/.bashrc or restart Termux. Use: todl <filename>
    ```

## Disclaimer
This tool is intended **strictly for ethical and educational purposes**, to understand web security vulnerabilities and browser permissions. Unauthorized use for malicious activities is illegal and unethical. The developer is not responsible for any misuse.

