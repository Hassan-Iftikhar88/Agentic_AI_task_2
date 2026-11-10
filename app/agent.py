from app import tools, memory, prompts


def run_agent(topic, platform, tone, output_type="Post + Reel Script", max_revisions=1):
    tools.TOOL_LOG.clear()

    tools.log_tool("Memory Tool")
    past = memory.recent_summary()

    plan = tools.clean_text(tools.ask_ollama(
        prompts.PLAN.format(topic=topic, platform=platform, tone=tone), max_tokens=300))
    print("\n--- AGENT PLAN ---\n" + plan + "\n")

    ideas = tools.trend_idea_generator(topic, platform, tone, past)
    idea = tools.clean_text(tools.ask_ollama(
        prompts.SELECT.format(ideas=ideas), temperature=0.2, max_tokens=100))
    audience = tools.audience_finder(topic, platform)

    hook, caption = tools.caption_writer(topic, platform, tone, idea)
    hashtags = tools.hashtag_generator(topic, platform)
    wants_script = any(w in output_type.lower() for w in ["reel", "script", "video"])
    reel = tools.reel_script_generator(topic, platform, tone, idea) if wants_script else ""
    title = tools.title_thumbnail_generator(topic, platform)

    best = None
    for i in range(max_revisions + 1):
        score, review = tools.content_reviewer(platform, hook, caption, hashtags)
        if best is None or score > best["score"]:
            best = {"score": score, "review": review, "hook": hook, "caption": caption}
        else:
            print(f"Revision scored {score}/10, not better than {best['score']}/10. "
                  "Keeping the earlier draft.")
        if score >= 8 or i == max_revisions:
            break
        print(f"Score {score}/10, revising...")
        hook, caption = tools.caption_writer(topic, platform, tone, idea, feedback=review)
    hook, caption = best["hook"], best["caption"]
    review, score = best["review"], best["score"]

    result = {"topic": topic, "platform": platform, "tone": tone, "plan": plan,
              "idea": idea, "audience": audience, "hook": hook, "caption": caption,
              "hashtags": hashtags, "reel_script": reel, "title": title,
              "review": review, "score": score}

    result["saved_file"] = tools.file_saver(result)
    memory.remember(topic, platform, tone, idea)
    result["tools_used"] = list(tools.TOOL_LOG)
    return result
