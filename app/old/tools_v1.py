"""Agent tools. Every tool prints "[Tool Called]: <name>" so the workflow is visible."""
import re
import requests
from datetime import datetime
from pathlib import Path

from app import prompts

MODEL = "gemma3:4b"  # change to "llama3.2:3b" if your PC is slow / low on RAM
OLLAMA_URL = "http://localhost:11434/api/generate"
BASE = Path(__file__).resolve().parent.parent
TOOL_LOG = []


def ask_ollama(prompt, temperature=0.7, max_tokens=600):
    """Send a prompt to the local Ollama server and return the text answer."""
    payload = {
        "model": MODEL,
        "prompt": prompt,
        "stream": False,
        "options": {"temperature": temperature, "num_predict": max_tokens},
    }
    try:
        r = requests.post(OLLAMA_URL, json=payload, timeout=300)
        r.raise_for_status()
    except requests.exceptions.ConnectionError:
        raise RuntimeError(
            "Cannot reach Ollama at localhost:11434. Open the Ollama app "
            "(or run 'ollama serve') and try again."
        )
    except requests.exceptions.HTTPError as e:
        raise RuntimeError(
            f"Ollama returned an error: {e}. Did you run 'ollama pull {MODEL}'?"
        )
    return r.json()["response"].strip()


def log_tool(name):
    print(f"[Tool Called]: {name}")
    TOOL_LOG.append(name)


def trend_idea_generator(topic, platform, tone, past):
    log_tool("Trend Idea Generator")
    return ask_ollama(prompts.IDEAS.format(topic=topic, platform=platform, tone=tone, past=past))


def audience_finder(topic, platform):
    log_tool("Audience Finder")
    return ask_ollama(prompts.AUDIENCE.format(topic=topic, platform=platform),
                      temperature=0.3, max_tokens=60)


def caption_writer(topic, platform, tone, idea, feedback=""):
    log_tool("Caption Writer")
    fb = f"Previous reviewer feedback to fix: {feedback}" if feedback else ""
    text = ask_ollama(prompts.CAPTION.format(
        topic=topic, platform=platform, tone=tone, idea=idea, feedback=fb))
    m = re.search(r"HOOK:\s*(.*?)\s*CAPTION:\s*(.*)", text, re.S | re.I)
    if m:
        return m.group(1).strip(), m.group(2).strip()
    # fallback if the model ignored the format
    return text.split("\n")[0], text


def hashtag_generator(topic, platform):
    log_tool("Hashtag Generator")
    text = ask_ollama(prompts.HASHTAGS.format(topic=topic, platform=platform),
                      temperature=0.4, max_tokens=100)
    tags = re.findall(r"#\w+", text)
    return tags[:8] if tags else ["#AI", "#MachineLearning"]


def reel_script_generator(topic, platform, tone, idea):
    log_tool("Reel Script Generator")
    return ask_ollama(prompts.REEL.format(topic=topic, platform=platform, tone=tone, idea=idea))


def title_thumbnail_generator(topic, platform):
    log_tool("Title & Thumbnail Generator")
    return ask_ollama(prompts.TITLE.format(topic=topic, platform=platform), max_tokens=100)


def content_reviewer(platform, hook, caption, hashtags):
    log_tool("Content Reviewer")
    text = ask_ollama(
        prompts.REVIEW.format(platform=platform, hook=hook, caption=caption,
                              hashtags=" ".join(hashtags)),
        temperature=0.2, max_tokens=200)
    m = re.search(r"SCORE:\s*(\d+)", text)
    score = int(m.group(1)) if m else 7
    return score, text


def file_saver(result):
    """Save the final result as Markdown (post) and a separate script file."""
    log_tool("File Saver")
    slug = re.sub(r"[^a-z0-9]+", "_", result["topic"].lower()).strip("_")[:40]
    plat = re.sub(r"[^a-z0-9]+", "", result["platform"].lower())
    md = f"""# {result['topic']} ({result['platform']})
**Tone:** {result['tone']}
**Date:** {datetime.now():%Y-%m-%d %H:%M}

## Content Idea
{result['idea']}

## Target Audience
{result.get('audience', 'N/A')}

## Hook
{result['hook']}

## Caption
{result['caption']}

## Hashtags
{' '.join(result['hashtags'])}

## Title & Thumbnail
{result['title']}

## Reel Script
{result['reel_script'] or 'N/A'}

## Review
{result['review']}
"""
    post_path = BASE / "outputs" / "generated_posts" / f"{slug}_{plat}.md"
    post_path.parent.mkdir(parents=True, exist_ok=True)
    post_path.write_text(md, encoding="utf-8")
    if result["reel_script"]:
        sp = BASE / "outputs" / "generated_scripts" / f"{slug}_{plat}_script.md"
        sp.parent.mkdir(parents=True, exist_ok=True)
        sp.write_text(result["reel_script"], encoding="utf-8")
    return str(post_path.relative_to(BASE))
