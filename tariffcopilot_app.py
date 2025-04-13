
import streamlit as st
import openai

st.set_page_config(page_title="TariffCopilot", layout="centered")

st.title("🛃 TariffCopilot")
st.subheader("Your GenAI Assistant for Global Trade Compliance")

st.markdown("""
Use natural language to:
- 🔍 Classify your product with an HS code
- 💰 Estimate duties/tariffs by country
- 🌐 Optimize for Free Trade Agreements (FTAs)
- 📄 Generate customs documents
""")

# Input prompt
user_input = st.text_area("Describe your product or ask a question:", placeholder="e.g., Classify Bluetooth speaker shipped from China to Germany")

# Submit button
if st.button("Ask TariffCopilot"):
    if user_input.strip() == "":
        st.warning("Please enter a description or question.")
    else:
        st.info("🔧 Demo mode: This is where the GenAI response would appear based on your query.")
        # Uncomment and configure below if you have OpenAI API access
        # openai.api_key = st.secrets["OPENAI_API_KEY"]
        # response = openai.ChatCompletion.create(
        #     model="gpt-4",
        #     messages=[{"role": "user", "content": user_input}]
        # )
        # st.success(response['choices'][0]['message']['content'])

st.markdown("---")
st.caption("TariffCopilot is an early-stage GenAI assistant built to simplify global trade compliance.")
