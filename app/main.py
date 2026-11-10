import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import streamlit as st
from app.agent import run_agent
from app import tools

st.set_page_config(page_title="TrendPilot", page_icon="🚀")
st.title("🚀 TrendPilot: Local Viral Content Agent")
st.caption(f"Running locally with Ollama model: {tools.MODEL}")

topic = st.text_input("Topic", "YOLOv8 helmet detection project")
platform = st.selectbox("Platform", ["LinkedIn", "Instagram", "X/Twitter", "YouTube Shorts", "Facebook"])
tone = st.text_input("Tone", "Professional but exciting")
output_type = st.selectbox("Output type", ["Post", "Post + Reel Script", "Reel Script"])

if st.button("Generate"):
    with st.spinner("Agent is working... (can take 1-3 minutes on a laptop)"):
        try:
            st.session_state["r"] = run_agent(topic, platform, tone, output_type)
        except Exception as e:
            st.error(str(e))

r = st.session_state.get("r")
if r:
    st.success(f"Saved to {r['saved_file']}")
    st.write("**Tools called:**", " → ".join(r["tools_used"]))
    st.subheader("Content Idea"); st.write(r["idea"])
    st.subheader("Target Audience"); st.write(r["audience"])
    st.subheader("Hook"); st.write(r["hook"])
    st.subheader("Caption"); st.write(r["caption"])
    st.subheader("Hashtags"); st.write(" ".join(r["hashtags"]))
    if r["reel_script"]:
        st.subheader("Reel Script"); st.text(r["reel_script"])
    st.subheader("Title & Thumbnail"); st.write(r["title"])
    st.subheader("Review"); st.write(r["review"])
    saved = Path(tools.BASE) / r["saved_file"]
    st.download_button("Save result (.md)", saved.read_text(encoding="utf-8"),
                       file_name=saved.name)
