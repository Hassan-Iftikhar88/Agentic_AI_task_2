# TrendPilot: Step by step on Windows

Do the steps in order. Tick each one off. Everything is already written for you in this folder.

## Step 0: You already did
- Installed Ollama and took a screenshot. Check it is saved as `screenshots\ollama_running.png`.
  If not, do Step 1 again and re-take it.

## Step 1: Make sure the model works (2 min)
Open **Command Prompt** and run:
```
ollama pull gemma3:4b
ollama run gemma3:4b
```
Type: `Give me 5 viral LinkedIn post ideas about AI internships.`
Wait for the answer, take the screenshot (Win + Shift + S), save as `screenshots\ollama_running.png`. Type `/bye`.

PC slow or under 8 GB RAM? Use `ollama pull llama3.2:3b` and in `app\tools.py` change
`MODEL = "gemma3:4b"` to `MODEL = "llama3.2:3b"`.

## Step 2: Put the project on your PC
Extract the zip so you have a folder `agentic_ai_task_2`. Open Command Prompt inside it:
```
cd path\to\agentic_ai_task_2
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```
(If `python` is not found, install Python 3.10+ from python.org and tick "Add to PATH".)

## Step 3: Run the CLI demo
Keep the Ollama app running in the background, then:
```
python demo.py
```
Enter: topic `YOLOv8 helmet detection project`, platform `LinkedIn`, tone `Professional but exciting`, output `Post + Reel Script`.
You will see `[Tool Called]: ...` lines. Wait 1-3 minutes.
- **Screenshot 2:** the terminal showing the `[Tool Called]` lines and final output -> `screenshots\demo_output.png`
- Open the saved file from `outputs\generated_posts\` in Notepad or VS Code
- **Screenshot 3:** -> `screenshots\saved_file_output.png`

## Step 4: (Optional) Streamlit demo
```
streamlit run app/main.py
```
A browser page opens. Good for the LinkedIn screen recording.

## Step 5: Run the 10 tests
```
python tests\run_tests.py
```
Takes 15-40 minutes. Leave it running. When done you have 10 files in `outputs\generated_posts\` and `tests\test_cases.md`.
Open each saved file, read it, and in `tests\test_cases.md` replace `TBD` with `Yes` or `No` and add a short note.

## Step 6: Error analysis (needs your real observations)
Find 5+ weak outputs (too generic, too long, not funny, bad hashtags, wrong format). For each:
1. Edit the matching prompt in `app\prompts.py` (add a limit, a rule, or an example).
2. Re-run that topic with `python demo.py`.
3. Write a row in the table: Test Case | Problem Found | Possible Reason | Fix Applied.
Only write problems you really saw. Add 3+ improvements. Paste the table into `README.md` and the report.

## Step 7: README and report
- README: already written. Fill the two italic placeholders (test results, error analysis).
- Report: use `report\REPORT_AND_LINKEDIN_TEMPLATES.md`, write it in Word/Google Docs in your own words, embed the 3 screenshots, export as `report\final_report.pdf`.

## Step 8: GitHub
1. On github.com create a new empty repo named `agentic_ai_task_2`.
2. In Command Prompt inside the project:
```
git init
git add .
git commit -m "AIRI PITB Task 2: TrendPilot agentic AI"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/agentic_ai_task_2.git
git push -u origin main
```
(.gitignore already excludes `venv`.) Open the link in a private window to confirm it works.

## Step 9: LinkedIn post and submit
Use the post in `report\REPORT_AND_LINKEDIN_TEMPLATES.md`, change it to your own words, attach a screenshot or recording, add your GitHub link. Then send the GitHub link to **Omar Farooq**.

## Final checklist
- [ ] 3 screenshots in `screenshots\`
- [ ] 5+ files in `outputs\`
- [ ] `tests\test_cases.md` has 10 rows with Useful? filled in
- [ ] Error table (5+ real cases) and 3+ improvements
- [ ] README, requirements.txt, `report\final_report.pdf`
- [ ] GitHub link opens in a private window
- [ ] LinkedIn post in your own words
- [ ] Link sent to Omar Farooq

## Common errors
| Error | Fix |
|---|---|
| `Cannot reach Ollama at localhost:11434` | Open the Ollama app from the Start menu, or run `ollama serve` in another window |
| `Ollama returned an error ... 404` | Model not pulled: `ollama pull gemma3:4b` |
| `ModuleNotFoundError: app` | Run commands from the project root folder (the one containing `app` and `demo.py`) |
| `'python' is not recognized` | Reinstall Python and tick "Add to PATH" |
| Very slow | Use `llama3.2:3b`, close other programs |
| Script in PowerShell blocked | Run `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` or use Command Prompt |
