
import streamlit as st

from agents import (
    build_reader_agent,
    build_search_agent,
    writer_chain,
    critic_chain,
)

# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="NEXUS AI | Research Studio",
    page_icon="✦",
    layout="wide",
)

# ---------------- DESIGN ----------------

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

:root {
    --yellow: #FFD600;
    --black: #080808;
    --card: #111111;
    --border: #292929;
    --muted: #929292;
}

.stApp {
    background-color: var(--black);
    background-image: radial-gradient(#292929 0.7px, transparent 0.7px);
    background-size: 19px 19px;
    color: white;
    font-family: 'Inter', sans-serif;
}

[data-testid="stHeader"] {
    background: rgba(8,8,8,0.95);
}

.block-container {
    max-width: 1200px;
    padding-top: 2rem;
    padding-bottom: 4rem;
}

#MainMenu, footer {
    visibility: hidden;
}

h1, h2, h3, p, label {
    color: white;
}

.brand {
    font-size: 21px;
    font-weight: 800;
    letter-spacing: -1px;
}

.brand span {
    color: var(--yellow);
}

.eyebrow {
    color: var(--yellow);
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 3px;
    text-transform: uppercase;
    margin-bottom: 22px;
}

.hero {
    font-size: clamp(42px, 6vw, 72px);
    font-weight: 800;
    letter-spacing: -4px;
    line-height: 1.05;
    text-align: center;
    margin-top: 30px;
}

.hero span {
    color: var(--yellow);
    text-shadow: 0 0 35px rgba(255,214,0,0.18);
}

.subtitle {
    color: #A4A4A4;
    text-align: center;
    font-size: 15px;
    line-height: 1.8;
    margin-top: 20px;
    margin-bottom: 35px;
}

.panel {
    background: rgba(17,17,17,0.94);
    border: 1px solid #303030;
    border-radius: 18px;
    padding: 24px;
    margin-top: 20px;
    box-shadow: 0 10px 45px rgba(0,0,0,0.25);
}

.panel-title {
    color: var(--yellow);
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 2px;
    margin-bottom: 14px;
}

.stTextInput input {
    background: #090909 !important;
    color: white !important;
    border: 1px solid #373737 !important;
    border-radius: 10px !important;
    min-height: 52px;
}

.stTextInput input:focus {
    border-color: var(--yellow) !important;
    box-shadow: 0 0 0 1px var(--yellow) !important;
}

.stTextInput input::placeholder {
    color: #777777 !important;
}

.stButton > button {
    background: var(--yellow) !important;
    color: #080808 !important;
    border: none !important;
    border-radius: 9px !important;
    font-weight: 800 !important;
    min-height: 48px;
    transition: 0.2s ease;
}

.stButton > button:hover {
    background: #FFE64D !important;
    box-shadow: 0 0 24px rgba(255,214,0,0.2);
    transform: translateY(-1px);
}

.section-title {
    font-size: 24px;
    font-weight: 700;
    letter-spacing: -1px;
    margin-top: 38px;
    margin-bottom: 5px;
}

.section-subtitle {
    color: var(--muted);
    font-size: 13px;
    margin-bottom: 22px;
}

.agent {
    background: rgba(17,17,17,0.96);
    border: 1px solid #303030;
    border-radius: 13px;
    padding: 18px 14px;
    min-height: 150px;
}

.agent-number {
    color: var(--yellow);
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 2px;
}

.agent-name {
    font-size: 15px;
    font-weight: 700;
    margin-top: 15px;
    margin-bottom: 8px;
}

.agent-description {
    font-size: 12px;
    color: #999999;
    line-height: 1.6;
}

.stTabs [data-baseweb="tab-list"] {
    gap: 12px;
    border-bottom: 1px solid #292929;
}

.stTabs [data-baseweb="tab"] {
    color: #999999;
}

.stTabs [aria-selected="true"] {
    color: var(--yellow) !important;
    border-bottom-color: var(--yellow) !important;
}

[data-testid="stStatusWidget"] {
    background: #111111;
    border: 1px solid #292929;
    border-radius: 12px;
}

[data-testid="stExpander"] {
    background: #111111;
    border: 1px solid #292929;
    border-radius: 10px;
}

hr {
    border-color: #292929 !important;
}

.footer {
    text-align: center;
    color: #666666;
    font-size: 11px;
    letter-spacing: 1px;
    margin-top: 40px;
}
</style>
""", unsafe_allow_html=True)


# ---------------- SIDEBAR ----------------

with st.sidebar:
    st.markdown(
        '<div class="brand">NEXUS<span>AI.</span></div>',
        unsafe_allow_html=True,
    )

    st.caption("MULTI-AGENT RESEARCH STUDIO")

    st.divider()

    st.markdown("### Workspace")
    st.markdown("✦  Research Studio")
    st.markdown("⌕  Web Search")
    st.markdown("▤  Research Reports")

    st.divider()

    st.markdown("### Your AI Team")
    st.markdown("🔍  Search Agent")
    st.markdown("📚  Reader Agent")
    st.markdown("✍️  Writer Agent")
    st.markdown("🧠  Critic Agent")

    st.divider()

    st.caption("Powered by your existing Gemini pipeline.")


# ---------------- HERO ----------------

st.markdown(
    '<div class="eyebrow" style="text-align:center;">'
    'YOUR PERSONAL AI RESEARCH TEAM</div>',
    unsafe_allow_html=True,
)

st.markdown(
    '<div class="hero">Research at the<br>'
    '<span>speed of AI.</span></div>',
    unsafe_allow_html=True,
)

st.markdown("""
<div class="subtitle">
Turn questions into detailed research reports.<br>
Watch your AI agents search, read, write and review.
</div>
""", unsafe_allow_html=True)


# ---------------- RESEARCH INPUT ----------------

st.markdown('<div class="panel">', unsafe_allow_html=True)

st.markdown(
    '<div class="panel-title">✦ &nbsp; START A NEW RESEARCH</div>',
    unsafe_allow_html=True,
)

topic = st.text_input(
    "Research topic",
    placeholder="What would you like to discover today?",
    label_visibility="collapsed",
)

st.markdown(
    '<p style="color:#777;font-size:12px;">'
    'Try: AI trends in 2026 · Future of robotics · Quantum computing'
    '</p>',
    unsafe_allow_html=True,
)

start = st.button("✦  START RESEARCH", use_container_width=True)

st.markdown('</div>', unsafe_allow_html=True)


# ---------------- AGENT CARDS ----------------

st.markdown(
    '<div class="section-title">Your AI research team</div>',
    unsafe_allow_html=True,
)

st.markdown(
    '<div class="section-subtitle">'
    'Four stages. One intelligent workflow.'
    '</div>',
    unsafe_allow_html=True,
)

agents = [
    ("01", "SEARCH AGENT", "Finds relevant information and sources."),
    ("02", "READER AGENT", "Reads web pages and extracts details."),
    ("03", "WRITER AGENT", "Creates your research report."),
    ("04", "CRITIC AGENT", "Reviews the report and gives feedback."),
]

columns = st.columns(4)

for col, (number, name, description) in zip(columns, agents):
    with col:
        st.markdown(f"""
        <div class="agent">
            <div class="agent-number">STAGE {number}</div>
            <div class="agent-name">{name}</div>
            <div class="agent-description">{description}</div>
        </div>
        """, unsafe_allow_html=True)


# ---------------- RESEARCH WORKFLOW ----------------

if start:
    if not topic.strip():
        st.warning("Please enter a research topic.")
    else:
        state = {}

        st.markdown(
            '<div class="section-title">Research workflow</div>',
            unsafe_allow_html=True,
        )

        st.markdown(
            '<div class="section-subtitle">'
            'Follow each stage as your AI team works.'
            '</div>',
            unsafe_allow_html=True,
        )

        # Stage 1: Search
        try:
            with st.status(
                "STAGE 1/4 — Searching the web...",
                expanded=True,
            ) as status:

                search_agent = build_search_agent()

                search_result = search_agent.invoke({
                    "messages": [
                        (
                            "user",
                            f"Find recent, reliable and detailed information about: {topic}",
                        )
                    ]
                })

                state["search_results"] = (
                    search_result["messages"][-1].content
                )

                st.write("Search agent completed its research.")
                status.update(
                    label="✅ STAGE 1/4 — Search completed",
                    state="complete",
                    expanded=False,
                )

        except Exception as e:
            st.error(f"Stage 1 failed: {e}")
            st.stop()

        # Stage 2: Reader
        try:
            with st.status(
                "STAGE 2/4 — Reading web sources...",
                expanded=True,
            ) as status:

                reader_agent = build_reader_agent()

                reader_result = reader_agent.invoke({
                    "messages": [
                        (
                            "user",
                            f"Based on the following search results about '{topic}', "
                            f"pick the most relevant URL and scrape it for deeper content.\n\n"
                            f"Search Results:\n{state['search_results'][:800]}",
                        )
                    ]
                })

                state["scraped_content"] = (
                    reader_result["messages"][-1].content
                )

                st.write("Reader agent completed source extraction.")
                status.update(
                    label="✅ STAGE 2/4 — Reading completed",
                    state="complete",
                    expanded=False,
                )

        except Exception as e:
            st.error(f"Stage 2 failed: {e}")
            st.stop()

        # Stage 3: Writer
        try:
            with st.status(
                "STAGE 3/4 — Writing the report...",
                expanded=True,
            ) as status:

                research = (
                    f"SEARCH RESULTS:\n{state['search_results']}\n\n"
                    f"DETAILED SCRAPED CONTENT:\n{state['scraped_content']}"
                )

                state["report"] = writer_chain.invoke({
                    "topic": topic,
                    "research": research,
                })

                st.write("Writer created the report.")
                status.update(
                    label="✅ STAGE 3/4 — Report completed",
                    state="complete",
                    expanded=False,
                )

        except Exception as e:
            st.error(f"Stage 3 failed: {e}")
            st.stop()

        # Stage 4: Critic
        try:
            with st.status(
                "STAGE 4/4 — Reviewing the report...",
                expanded=True,
            ) as status:

                state["feedback"] = critic_chain.invoke({
                    "report": state["report"],
                })

                st.write("Critic completed its review.")
                status.update(
                    label="✅ STAGE 4/4 — Review completed",
                    state="complete",
                    expanded=False,
                )

        except Exception as e:
            st.error(f"Stage 4 failed: {e}")
            st.stop()

        # Store results in the session
        st.session_state["research_result"] = {
            "topic": topic,
            **state,
        }

        st.success("All four research stages completed!")


# ---------------- DISPLAY RESULTS ----------------

if "research_result" in st.session_state:
    result = st.session_state["research_result"]

    st.markdown("---")

    st.markdown(
        '<div class="eyebrow">YOUR RESEARCH OUTPUT</div>',
        unsafe_allow_html=True,
    )

    st.subheader(result["topic"])

    report_tab, search_tab, reader_tab, critic_tab = st.tabs([
        "✦ Final Report",
        "⌕ Search Results",
        "▤ Scraped Content",
        "🧠 Critic Feedback",
    ])

    with report_tab:
        st.markdown(result["report"])

        st.download_button(
            "↓  DOWNLOAD REPORT",
            data=result["report"],
            file_name="research_report.md",
            mime="text/markdown",
        )

    with search_tab:
        st.markdown(result["search_results"])

    with reader_tab:
        st.markdown(result["scraped_content"])

    with critic_tab:
        st.markdown(result["feedback"])


# ---------------- FOOTER ----------------

st.markdown("""
<div class="footer">
NEXUS AI &nbsp; · &nbsp; INTELLIGENCE THROUGH COLLABORATION
</div>
""", unsafe_allow_html=True)
