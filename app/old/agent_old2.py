"""TrendPilot agent: memory -> plan -> tools -> review/improve -> save -> return."""
from app import tools, memory, prompts


def run_agent(topic, platform, tone, output_type="Post + Reel Script", max_revisions=1):
    tools.TOOL_LOG.clear()

    # 1. Memory: what did the user ask before?
    tools.log_tool("Memory Tool")
    past = memory.recent_summary()

    # 2. Plan
    plan = tools.ask_ollama(
        prompts.PLAN.format(topic=topic, platform=platform, tone=tone), max_tokens=300)
    print("\n--- AGENT PLAN ---\n" + plan + "\n")

    # 3. Ideas -> pick the best one
    ideas = tools.trend_idea_generator(topic, platform, tone, past)
    idea = tools.ask_ollama(prompts.SELECT.format(ideas=ideas), temperature=0.2, max_tokens=100)
    audience = tools.audience_finder(topic, platform)

    # 4. Generate content
    hook, caption = tools.caption_writer(topic, platform, tone, idea)
    hashtags = tools.hashtag_generator(topic, platform)
    wants_script = any(w in output_type.lower() for w in ["reel", "script", "video"])
    reel = tools.reel_script_generator(topic, platform, tone, idea) if wants_script else ""
    title = tools.title_thumbnail_generator(topic, platform)

    # 5. Review and improve loop
    for i in range(max_revisions + 1):
        score, review = tools.content_reviewer(platform, hook, caption, hashtags)
        if score >= 8 or i == max_revisions:
            break
        print(f"Score {score}/10, revising...")
        hook, caption = tools.caption_writer(topic, platform, tone, idea, feedback=review)

    result = {"topic": topic, "platform": platform, "tone": tone, "plan": plan,
              "idea": idea, "audience": audience, "hook": hook, "caption": caption,
              "hashtags": hashtags, "reel_script": reel, "title": title,
              "review": review, "score": score}

    # 6. Save and remember
    result["saved_file"] = tools.file_saver(result)
    memory.remember(topic, platform, tone, idea)
    result["tools_used"] = list(tools.TOOL_LOG)
    return result
