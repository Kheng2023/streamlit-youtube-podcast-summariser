from google import genai
from google.genai import types
import streamlit as st
from youtube_transcript_api import YouTubeTranscriptApi

# App Title & Description
st.set_page_config(page_title="YouTube Podcast Summarizer", page_icon="▶️", layout="wide")
st.title("🎙️ YouTube Podcast Summarizer")
st.write("Generate a structured summary of YouTube podcast episodes with AI.")
st.markdown("""
### 🔑 **Important Instructions**
- **Enter your Gemini API key** in the sidebar.  
  *(Mobile users: Tap the `>` button in the top-left to access the sidebar.)*
  
- **Improving Transcript Retrieval Success**:
  1. Choose a **YouTube video with official subtitles**.
  2. **Turn on Closed Captions (CC)** before copying the link.
  3. Ensure the video URL contains `'watch'`.
  4. Some videos **without official transcripts** may work over time.
""")
# Sidebar Settings
with st.sidebar:
    st.title("⚙️ Settings")
    st.write("Enter your Gemini API Key:")
    api_key = st.text_input("Gemini API Key", key="chatbot_api_key", type="password")
    st.caption("[🔑 Get Gemini API key](https://ai.google.dev/gemini-api/docs/api-key)")
    st.caption("[📂 View Source Code](https://github.com/Kheng2023/podcast-summarizer)")
    st.divider()

# System Instruction for AI Summarization
system_instruction = """You are given a YouTube podcast transcript. Your task is to summarize the podcast in markdown format:
**Topic 1: Topic name**
1. Key Point 1
2. Key Point 2

**Topic 2: Topic name**
1. Key Point 1
2. Key Point 2
3. Key Point 3

Keep the summary concise and structured.
If summarization isn't possible, state so explicitly."""

genai_config = types.GenerateContentConfig(
    system_instruction=system_instruction,
    temperature=0.7,
    top_p=0.9,
)

# Input: YouTube Video Link
youtube_link = st.text_input("🔗 Enter a YouTube URL", placeholder="https://www.youtube.com/watch?v=12345abcde")

# Function to Fetch Transcript
def fetch_transcript(video_id):
    try:
        transcript_data = YouTubeTranscriptApi.get_transcript(video_id)
        transcript_text = ' '.join([line['text'] for line in transcript_data])
        return transcript_text, None
    except Exception as e:
        return None, str(e)

# Function to Generate Summary
def summarize_podcast(transcript):
    try:
        client = genai.Client(api_key=api_key)
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            config=genai_config,
            contents=transcript
        )
        return response.text, None
    except Exception as e:
        return None, str(e)

# Summarization Process
if st.button("📄 Summarize Podcast"):
    if not api_key:
        st.error("❌ Please enter your Gemini API key in the sidebar.")
        st.stop()
    
    st.info("⏳ Fetching transcript...")
    
    video_id = youtube_link.split('=')[-1]
    transcript, error = fetch_transcript(video_id)
    
    if not transcript:
        st.error(f"⚠️ Could not fetch transcript: {error}")
        st.stop()
    
    st.success("✅ Transcript fetched successfully!")
    
    st.info("✍️ Generating summary...")
    
    summary, error = summarize_podcast(transcript)
    
    if not summary:
        st.error(f"⚠️ Error during summarization: {error}")
        st.stop()
    
    st.success("✅ Podcast summarized successfully!")
    
    with st.expander("📌 **Click to view summary**"):
        st.markdown(summary)
    
    st.download_button(
        label="📥 Download Summary",
        data=summary,
        file_name="podcast_summary.md",
        mime="text/markdown"
    )
