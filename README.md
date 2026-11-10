# TrendPilot: A Local Agentic AI Assistant Using Ollama

TrendPilot is a local AI agent that takes a topic, platform, tone and output type, and produces a complete viral content package: content idea, target audience, hook, caption, hashtags, reel script, title and thumbnail text, and review comments. Everything runs on my own machine through Ollama, with no paid API.

**Model:** Gemma 3:4B via Ollama (`gemma3:4b`)
**Stack:** Python, Ollama, Requests, Streamlit, JSON memory, Markdown file saving, GitHub

## Agent workflow

```
User gives topic
      ↓
Agent understands the goal (reads memory of past topics)
      ↓
Agent creates a plan
      ↓
Agent uses tools (ideas, audience, caption, hashtags, reel script, title)
      ↓
Content Reviewer scores the post; if score < 8 the Caption Writer revises it once
(the agent keeps whichever draft scored higher)
      ↓
File Saver stores the result as Markdown
      ↓
Agent returns the final answer
```

## Tools implemented

| Tool | What it does |
|---|---|
| Memory Tool | Stores and reads previous topics, platforms and tones (`outputs/saved_results/memory.json`) |
| Trend Idea Generator | Creates 5 viral content angles for the topic |
| Audience Finder | Names the target audience |
| Caption Writer | Writes the hook and post caption, also used for revisions |
| Hashtag Generator | Produces 8 relevant hashtags |
| Reel Script Generator | Writes a 30-second, 4-scene video script |
| Title & Thumbnail Generator | Creates a title and thumbnail text |
| Content Reviewer | Scores the content 1-10 and gives improvement tips |
| File Saver | Saves the result to `outputs/generated_posts/` and `outputs/generated_scripts/` |

## Setup

1. Install Ollama from https://ollama.com/download
2. `ollama pull gemma3:4b`
3. Create a virtual environment and install dependencies:
   ```
   python -m venv venv
   venv\Scripts\activate
   pip install -r requirements.txt
   ```

## How to run

CLI demo:
```
python demo.py
```
Streamlit demo:
```
streamlit run app/main.py
```
Run the 10 test cases:
```
python tests/run_tests.py
```

## Example

**Input:** Topic: YOLOv8 helmet detection project, Platform: LinkedIn, Tone: Professional but exciting, Output: Post + Reel Script

**Output:** see `outputs/generated_posts/` for saved examples.

Screenshots: `screenshots/ollama_running.png`, `screenshots/demo_output.png`, `screenshots/saved_file_output.png`

Before and after the prompt and code fixes (same input, test 6): `screenshots/before_fix_test6_v2.png` and `screenshots/after_fix_test6_v2.png`

## Test results

10 test cases are recorded in `tests/test_cases.md`, covering LinkedIn, Instagram, X/Twitter and YouTube Shorts, with tones from professional to meme style.

- All 10 were re-run after the prompt and code fixes, so every result comes from one version of the agent.
- 5 of 10 were useful as drafts (tests 1, 2, 3, 6, 10) and 5 were not (tests 4, 5, 7, 8, 9).
- Tests 4 to 10 went through one review-and-revise round. Tests 1 to 3 scored 8/10 on the first try.
- The best results were the funny Python post with its reel script (test 3) and the production-failure post (test 6). The weakest were vague topics, where the model invented details, and humor on X and LinkedIn.
- The model's own review score (7 to 8 out of 10) was not a reliable measure of quality, because it gave 8/10 to posts with unrelated titles.
## Project history

- `app/old/` keeps the first versions of the prompts and tools, from before the fixes described in the error analysis.
- `outputs/saved_results/before_fix/` and `tests/test_cases_before_fix.md` hold the outputs from the first version, for comparison with the final version.

## Error analysis

| Test Case | Problem Found | Possible Reason | Fix Applied / Suggested |
|---|---|---|---|
| 4, 7 (also 3, 5) | Title does not match the post. "Predicting Customer Churn with ML" appears in two different tests. | The title tool only receives the topic and platform, not the chosen idea or caption. | Not fixed. Pass the idea and hook to the title tool. |
| 1, 4, 7, 8, 10 | Invented facts, numbers and stories, for example 10-15% and 95% accuracy in test 8. | Vague topics give the model no real details, and the rule against inventing is only a soft instruction. | Partly fixed. The rule removed placeholders but not invented claims. Suggest an input for real project details and a code check for invented numbers. |
| 4, 9 (also 8) | Posts over the platform length limit. X posts were far over 280 characters. | The model cannot count characters and the limit is only in the prompt. | Not fixed. Add a length check in code and regenerate or trim. |
| 5, 9 | Humor is confusing or makes no technical sense. | A small 4B model is weak at humor. | Partly fixed. The setup-and-punchline rule helped tests 3 and 6. Suggest example jokes in the prompt or a larger model. |
| 5, 7, 9 | Review gave 8/10 to weak posts, and criticised the tone the user asked for (test 5). | The reviewer only sees the hook, caption and hashtags, and a small model reviews generically. | Partly fixed. The reviewer now only quotes existing text. Suggest rule-based checks and a larger model. |
| Plan step | The plan lists steps the agent never does, such as scheduling the post. | The plan is written by the model, not built from the real tool list. | Partly fixed. An example plan stopped the meme-format lists. Suggest building the plan from the actual tools. |
| 8 | Closing line wrapped in brackets. | The model copied the placeholder style from the prompt. | Not fixed. Minor. Change the placeholder wording. |
| First demo run | Extra versions, "Would you like me to...", markdown symbols, cut-off titles, a fashion-model post (test 6). | Prompts had no format, length or context rules. | Fixed. Strict formats, "ONE post only", tech context and a cleanup function. None appear in the 10 new outputs. |

## Future improvements

- Optional project-details input, so the agent uses real facts instead of inventing them
- Pass the idea and hook to the title and hashtag tools
- Code checks for platform length (LinkedIn vs X) and for invented numbers, with automatic regeneration
- Build the plan from the real tool list
- User feedback loop ("make it shorter")
- SQLite memory
- Web search tool for real trends
- Try a larger local model for review and humor
- Multi-agent / LangGraph workflow
