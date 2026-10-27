from agents import (
    build_reader_agent,
    build_search_agent,
    writer_chain,
    critic_chain,
)


def run_research_pipeline(topic: str) -> dict:
    state = {}

    # ==========================================
    # STEP 1: SEARCH AGENT
    # ==========================================
    print("\n" + "=" * 50)
    print("STEP 1 - Search agent is working...")
    print("=" * 50)

    try:
        search_agent = build_search_agent()

        search_result = search_agent.invoke({
            "messages": [
                (
                    "user",
                    f"Find recent, reliable, and detailed information about: {topic}"
                )
            ]
        })

        state["search_results"] = search_result["messages"][-1].content

        print("\nSearch results:\n")
        print(state["search_results"])

    except Exception as e:
        print(f"\nSearch agent failed: {e}")
        state["error"] = "Search agent failed"
        return state

    # ==========================================
    # STEP 2: READER AGENT
    # ==========================================
    print("\n" + "=" * 50)
    print("STEP 2 - Reader agent is scraping resources...")
    print("=" * 50)

    try:
        reader_agent = build_reader_agent()

        reader_result = reader_agent.invoke({
            "messages": [
                (
                    "user",
                    f"Based on the following search results about '{topic}', "
                    f"select the most relevant URL and scrape it for detailed "
                    f"information.\n\n"
                    f"Search Results:\n{state['search_results'][:800]}"
                )
            ]
        })

        state["scraped_content"] = reader_result["messages"][-1].content

        print("\nScraped content:\n")
        print(state["scraped_content"])

    except Exception as e:
        print(f"\nReader agent failed: {e}")
        state["error"] = "Reader agent failed"
        return state

    # ==========================================
    # PREPARE RESEARCH
    # ==========================================
    research_combined = (
        f"SEARCH RESULTS:\n"
        f"{state['search_results']}\n\n"
        f"DETAILED SCRAPED CONTENT:\n"
        f"{state['scraped_content']}"
    )

    # ==========================================
    # STEP 3: WRITER CHAIN
    # ==========================================
    print("\n" + "=" * 50)
    print("STEP 3 - Writer is drafting the report...")
    print("=" * 50)

    try:
        state["report"] = writer_chain.invoke({
            "topic": topic,
            "research": research_combined,
        })

        print("\nFinal Report:\n")
        print(state["report"])

    except Exception as e:
        print(f"\nWriter failed: {e}")
        print("Search and scraping completed, but report generation failed.")
        state["error"] = "Writer failed"
        return state

    # ==========================================
    # STEP 4: CRITIC CHAIN
    # ==========================================
    print("\n" + "=" * 50)
    print("STEP 4 - Critic is reviewing the report...")
    print("=" * 50)

    try:
        state["feedback"] = critic_chain.invoke({
            "report": state["report"],
        })

        print("\nCritic feedback:\n")
        print(state["feedback"])

    except Exception as e:
        print(f"\nCritic failed: {e}")
        print("The report was generated, but the review failed.")
        state["error"] = "Critic failed"

    # ==========================================
    # RETURN FINAL STATE
    # ==========================================
    return state


# ==========================================
# MAIN PROGRAM
# ==========================================
if __name__ == "__main__":
    topic = input("\nEnter a research topic: ").strip()

    if topic:
        result = run_research_pipeline(topic)

        print("\n" + "=" * 50)
        print("PIPELINE EXECUTION SUMMARY")
        print("=" * 50)

        if "report" in result:
            print("Report generated successfully.")

        if "feedback" in result:
            print("Critic review completed.")

        if "error" in result:
            print(f"Status: {result['error']}")

    else:
        print("Please enter a valid research topic.")