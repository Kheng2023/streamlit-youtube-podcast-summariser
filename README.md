# 📦 Streamlit App: YouTube Podcast Summarizer  

This is a **Streamlit-powered** version of my original **YouTube Podcast Summarizer** script. I created a **simple user interface (UI)** to make it accessible for **non-coders**, while maintaining its powerful functionality. The app is **deployed for free** on the **Streamlit Community Cloud**.  

---

## 🚀 Demo App  

🎥 **Watch the app in action!** → [YouTube Demo](https://youtu.be/FR1GI0wqvqY)  

Ever listened to a podcast, got inspired by the insights shared, but then realized you can't remember anything afterward? I’ve found myself **replaying parts of an episode** just to take notes.  

That’s why I built this app! It helps you **recall key points** from any YouTube podcast **without replaying the entire episode**.  

Try the app here:  

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://youtube-podcast-summarizer.streamlit.app/)  

---

## 🎯 About This Application  

This **Streamlit web app** allows users to **summarize YouTube podcasts** effortlessly. It fetches transcripts using the **YouTube Transcript API** and generates concise summaries using **Google's Gemini API**.  

### **Key Features**  
✅ **Easy YouTube URL Input** – Just paste a **YouTube video link** to get started.  
✅ **AI-Powered Summarization** – Uses **Google Gemini** for accurate and structured summaries.  
✅ **Automated Transcript Retrieval** – Fetches transcripts directly from YouTube.  
✅ **Organized Summary Output** – Displays summaries in a **clean, scrollable format**.  
✅ **Settings Sidebar** – Securely enter your **Gemini API key** within the app.  

---

## 🛠️ Getting Started  

### **Prerequisites**  

🔹 **Python 3.6+** installed on your system  
🔹 **Google Gemini API key** (Get yours **[here](https://ai.google.dev/)**)  

### **Installation**  

1️⃣ **Clone the repository**  

```bash
git clone https://github.com/Kheng2023/streamlit-youtube-podcast-summariser.git
cd streamlit-youtube-podcast-summariser
```

2️⃣ **Install dependencies**  

```bash
pip install -r requirements.txt
```

3️⃣ **Set your Gemini API Key**  

Before running the app, **export your Gemini API key** (replace `your_api_key` with your actual key):  

```bash
export GEMINI_API_KEY="your_api_key"
```

4️⃣ **Run the Streamlit app**  

```bash
streamlit run streamlit_app.py
```

5️⃣ **Enter your Gemini API key** in the **settings sidebar** when prompted.  

---

## ❗ Troubleshooting  

🔹 **Issue:** The app sometimes fails to fetch a transcript.  
**Possible Reasons:**  
- The **YouTube video does not have subtitles** available.  
- Some **auto-generated captions** may not be accessible via the API.  
- The **provided YouTube link is incorrect** (make sure it’s the full URL, not a shortened "share" link).
- 
---

## 📚 Further Reading  

📌 **[Streamlit Documentation](https://docs.streamlit.io/)** – Learn more about building web apps.  
📌 **[YouTube Transcript API](https://github.com/jdepoix/youtube-transcript-api)** – Fetching YouTube transcripts.  
📌 **[Google Gemini API Docs](https://ai.google.dev/gemini-api/docs/)** – Learn how Gemini AI works.  

---

## 🤝 Contributing  

💡 **Contributions are welcome!** 🚀  
If you have suggestions, **submit a pull request** or **open an issue** to report bugs or improvements.  

---

## ⚖️ License  

This project is licensed under the **MIT License** – see the [LICENSE](LICENSE) file for details.  

---
