"""All prompts used by the TrendPilot agent.

Small local models (3-4B) work best with short, specific prompts,
explicit length limits and an exact output format.

v2 (after error analysis): added tech context, "one post only", no invented
facts / placeholders, no extra notes, and strict two-line formats.
"""

CONTEXT = ("Context: the author is an AI / machine-learning / programming student or engineer. "
           "The word 'model' always means a machine-learning model.\n")

PLAN = """You are a content strategy agent. Topic: {topic}. Platform: {platform}. Tone: {tone}.
Write a numbered plan of at most 8 short steps to produce a viral content package. Output only the plan."""

IDEAS = CONTEXT + """Generate 5 different viral content angles for {platform} about: {topic}.
Tone: {tone}. Avoid repeating these past topics/styles: {past}
Each angle: one line, specific, no generic advice. Number them 1-5."""

SELECT = """Pick the single most engaging angle from this list and output ONLY that angle, no extra text:
{ideas}"""

AUDIENCE = CONTEXT + """Who is the ideal target audience for a {platform} post about: {topic}?
Answer in ONE short sentence. No extra text."""

CAPTION = CONTEXT + """Write ONE {platform} post about: {topic}. Angle: {idea}. Tone: {tone}.
Rules:
- Strong first-line hook, clear, specific, end with a question or call to action.
- Length: LinkedIn max 180 words, X max 280 characters, Instagram max 120 words.
- Write ONLY for {platform}. Do NOT write versions for other platforms.
- Do NOT invent numbers, results, company names or project details. Do NOT use [bracket] placeholders.
- Do NOT add notes, explanations or questions to me after the post.
{feedback}
Use EXACTLY this format and stop after the caption:
HOOK: <one sentence>
CAPTION: <full post>"""

HASHTAGS = CONTEXT + """Give 8 different relevant hashtags for a {platform} post about: {topic}.
Do not repeat a hashtag. Output only the hashtags separated by spaces. No explanations."""

REEL = CONTEXT + """Write a 30-second video script for {platform} about: {topic}. Angle: {idea}. Tone: {tone}.
Format exactly (plain text, no < > brackets, no notes after the script, no emojis, every scene has a Voiceover line):
Scene 1: <visual>
Voiceover: "<line>"
Scene 2: <visual>
Voiceover: "<line>"
Scene 3: <visual>
Voiceover: "<line>"
Scene 4: <visual>
Voiceover: "<line>"
Closing line: "<one spoken sentence, not hashtags>"
Maximum 80 words of voiceover total. Do not invent facts."""

TITLE = CONTEXT + """For a {platform} piece about: {topic}, write exactly two lines and nothing else:
TITLE: <catchy title under 10 words>
THUMBNAIL TEXT: <max 4 words>
Do not give options. Do not add an introduction."""

REVIEW = """You are a strict content reviewer for {platform}. Review this content.
HOOK: {hook}
CAPTION: {caption}
HASHTAGS: {hashtags}
Check: hook strength, clarity, length for {platform}, tone, hashtag relevance, {platform}-readiness.
Be strict: give 8 or more only if there are no real problems.
Reply with ONLY these two parts and nothing else (no intro, no closing sentence):
SCORE: <whole number 1-10>
COMMENTS: <max 3 short improvement suggestions>"""
