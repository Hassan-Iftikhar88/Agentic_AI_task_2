"""All prompts used by the TrendPilot agent.

Small local models (3-4B) work best with short, specific prompts,
explicit length limits and an exact output format.
"""

PLAN = """You are a content strategy agent. Topic: {topic}. Platform: {platform}. Tone: {tone}.
Write a numbered plan of at most 8 short steps to produce a viral content package. Output only the plan."""

IDEAS = """Generate 5 different viral content angles for {platform} about: {topic}.
Tone: {tone}. Avoid repeating these past topics/styles: {past}
Each angle: one line, specific, no generic advice. Number them 1-5."""

SELECT = """Pick the single most engaging angle from this list and output ONLY that angle, no extra text:
{ideas}"""

AUDIENCE = """Who is the ideal target audience for a {platform} post about: {topic}?
Answer in ONE short sentence. No extra text."""

CAPTION = """Write a {platform} post about: {topic}. Angle: {idea}. Tone: {tone}.
Rules: strong first-line hook, clear, specific, platform-appropriate length (LinkedIn max 180 words, X max 280 characters, Instagram max 120 words), end with a question or call to action.
{feedback}
Use EXACTLY this format:
HOOK: <one sentence>
CAPTION: <full post>"""

HASHTAGS = """Give 8 relevant hashtags for a {platform} post about: {topic}.
Output only the hashtags separated by spaces. No explanations."""

REEL = """Write a 30-second video script for {platform} about: {topic}. Angle: {idea}. Tone: {tone}.
Format exactly:
Scene 1: <visual>
Voiceover: "<line>"
(Scene 1 to 4)
Closing line: "<line>"
Maximum 80 words of voiceover total."""

TITLE = """For a {platform} piece about: {topic}, write:
TITLE: <catchy title under 10 words>
THUMBNAIL TEXT: <max 4 words>"""

REVIEW = """You are a strict content reviewer for {platform}. Review this content.
HOOK: {hook}
CAPTION: {caption}
HASHTAGS: {hashtags}
Check: hook strength, clarity, length, tone, hashtag relevance, {platform}-readiness.
Reply EXACTLY:
SCORE: <number 1-10>
COMMENTS: <max 3 short improvement suggestions>"""
