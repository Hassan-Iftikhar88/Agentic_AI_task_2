PLAN = """You are a content strategy agent. Topic: {topic}. Platform: {platform}. Tone: {tone}.
Write a numbered plan of exactly 8 short steps that the agent will follow to produce a content package.
Each step is one action such as understand, generate, write, review or save.
Do not list content formats, memes, hashtags or posts. Do not use symbols such as * or **.
Example of the style:
1. Understand the topic and goal.
2. Generate content angles.
3. Pick the best angle.
4. Write the caption.
5. Generate hashtags.
6. Write the video script.
7. Review and improve the draft.
8. Save the final result.
Output only the numbered plan."""

IDEAS = """Context: the user is a student or engineer in AI and machine learning. Words like 'model' mean a machine learning model, never a fashion model.
Generate 5 different viral content angles for {platform} about: {topic}.
Tone: {tone}. Avoid repeating these past topics/styles: {past}
Each angle: one line, specific, no generic advice, no emojis, no invented numbers. Number them 1-5."""

SELECT = """Pick the single most engaging angle from this list and output ONLY that angle, with no number, no emojis and no extra text:
{ideas}"""

AUDIENCE = """Context: the user is a student or engineer in AI and machine learning.
Who is the ideal target audience for a {platform} post about: {topic}?
Answer in ONE short sentence. No emojis. No extra text."""

CAPTION = """Context: the user is a student or engineer in AI and machine learning. Words like 'model' mean a machine learning model, never a fashion model.
Write ONE {platform} post about: {topic}. Angle: {idea}. Tone: {tone}.
Rules: strong first-line hook, clear and specific, platform-appropriate length (LinkedIn max 180 words, X max 280 characters, Instagram max 120 words), end with a short question or call to action.
If the tone is funny or meme style, use a relatable developer joke with a setup and a punchline.
Do not use emojis. Do not use hashtags in the post. Do not use markdown symbols such as * or **.
Do not invent numbers, names, results or personal stories. Do not use [placeholders].
Do not write versions for other platforms. Do not add notes or ask the user anything.
{feedback}
Use EXACTLY this format:
HOOK: <one sentence>
CAPTION: <full post>"""

HASHTAGS = """Give 8 relevant, different hashtags for a {platform} post about: {topic}.
The topic is about AI and machine learning.
Output only the hashtags separated by spaces. No explanations. No emojis."""

REEL = """Context: the user is a student or engineer in AI and machine learning. Words like 'model' mean a machine learning model, never a fashion model.
Write a 30-second video script for {platform} about: {topic}. Angle: {idea}. Tone: {tone}.
Every scene must have both a visual and a voiceover. Do not use emojis. Do not use angle brackets or markdown symbols.
Do not invent numbers, names, results or personal stories.
Format exactly:
Scene 1: (what is shown)
Voiceover: (one short spoken line)
Scene 2: (what is shown)
Voiceover: (one short spoken line)
Scene 3: (what is shown)
Voiceover: (one short spoken line)
Scene 4: (what is shown)
Voiceover: (one short spoken line)
Closing line: (one short spoken line)
Maximum 80 words of voiceover total. Output only the script."""

TITLE = """Context: the user is a student or engineer in AI and machine learning.
For a {platform} piece about: {topic}, write exactly two lines and nothing else:
TITLE: (catchy title, under 10 words)
THUMBNAIL TEXT: (maximum 4 words)
No emojis. No markdown symbols. No extra options or notes."""

REVIEW = """You are a strict content reviewer for {platform}. Review ONLY the content below.
HOOK: {hook}
CAPTION: {caption}
HASHTAGS: {hashtags}
Check: hook strength, clarity, length, tone, hashtag relevance, {platform}-readiness.
Only refer to words that appear in the content above. Do not quote text that is not there.
Reply EXACTLY in this format and nothing else:
SCORE: (one whole number from 1 to 10)
COMMENTS: (maximum 3 short improvement suggestions)"""
