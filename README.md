# 📦 Streamlit App: YouTube Podcast Summarizer

UI developed using Streamlit, leveraging the YouTube Transcript API and Google's Gemini API, to create a YouTube Podcast Summarizer.

## Demo App

Try out the app here!:

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://youtube-podcast-summarizer.streamlit.app/)

## About This Application

This Streamlit application allows users to quickly summarize YouTube podcast transcripts. It fetches transcripts using the YouTube Transcript API and generates concise summaries using Google's Gemini API. The application is designed to be user-friendly and provides a clean interface for easy access to podcast summaries.

**Key Features:**

* **Easy YouTube URL Input:** Simply paste a YouTube video URL to get started.
* **Gemini-Powered Summarization:** Leverages the power of Google's Gemini API for accurate and concise summaries.
* **Transcript Retrieval:** Automatically fetches video transcripts using the YouTube Transcript API.
* **Clear and Organized Output:** Presents summaries in a structured, scrollable format.
* **Settings Sidebar:** Allows users to configure their Gemini API key securely.

## Getting Started

**Prerequisites:**

* Python 3.6+
* A Google Gemini API key (obtainable from [Google AI Studio](https://ai.google.dev/))

**Installation:**

1.  Clone the repository:

    ```bash
    git clone [your-repository-url]
    cd [your-repository-directory]
    ```

2.  Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3.  Run the Streamlit application:

    ```bash
    streamlit run app.py
    ```

4.  Enter your Gemini API key in the settings sidebar.

## Further Reading

**Resources:**

* **Streamlit Documentation:** [https://docs.streamlit.io/](https://docs.streamlit.io/)
    * Learn more about building web apps with Streamlit.
* **YouTube Transcript API:** [https://github.com/jdepoix/youtube-transcript-api](https://github.com/jdepoix/youtube-transcript-api)
    * Explore the documentation for retrieving YouTube transcripts.
* **Google Gemini API:** [https://ai.google.dev/gemini-api/docs/](https://ai.google.dev/gemini-api/docs/)
    * Learn how to use Google's Gemini API.
* **Example youtube video to test the summarizer:**
    * add a youtube video link here.

## Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues to suggest improvements or report bugs.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
