import os
import gradio as gr
import anthropic

client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

SYSTEM_PROMPT = """
You are a helpful support assistant for Thoughtful AI.

Use the following knowledge base to answer any questions related to Thoughtful AI. 
If the user's question matches one of these topics, use the provided answer verbatim. 
If it doesn't, use your general knowledge to respond helpfully.

Knowledge Base:
1. What does the eligibility verification agent (EVA) do?
   → EVA automates the process of verifying a patient's eligibility and benefits information in real-time, eliminating manual data entry errors and reducing claim rejections.

2. What does the claims processing agent (CAM) do?
   → CAM streamlines the submission and management of claims, improving accuracy, reducing manual intervention, and accelerating reimbursements.

3. How does the payment posting agent (PHIL) work?
   → PHIL automates the posting of payments to patient accounts, ensuring fast, accurate reconciliation of payments and reducing administrative burden.

4. Tell me about Thoughtful AI's Agents.
   → Thoughtful AI provides a suite of AI-powered automation agents designed to streamline healthcare processes. These include Eligibility Verification (EVA), Claims Processing (CAM), and Payment Posting (PHIL), among others.

5. What are the benefits of using Thoughtful AI's agents?
   → Using Thoughtful AI's Agents can significantly reduce administrative costs, improve operational efficiency, and reduce errors in critical processes like claims management and payment posting.
"""

def thoughtful_agent_claude(user_input, chat_history):
    try:
        cleaned_input = user_input.strip()

        # Guard 1: Reject blank or very short input
        if not cleaned_input or len(cleaned_input) < 3:
            chat_history.append((user_input, "Can you provide more detail?"))
            return chat_history, ""

        # Guard 2: Reject overly long input
        if len(cleaned_input) > 4000:
            chat_history.append((user_input, "That message is a bit too long — try shortening it."))
            return chat_history, ""

        # Prepare chat history for Claude
        messages = []
        for user, assistant in chat_history:
            messages.append({"role": "user", "content": user})
            messages.append({"role": "assistant", "content": assistant})
        messages.append({"role": "user", "content": cleaned_input})

        response = client.messages.create(
            model="claude-opus-4-1-20250805",
            max_tokens=512,
            system=SYSTEM_PROMPT,
            messages=messages
        )

        reply = response.content[0].text.strip()
        chat_history.append((user_input, reply))
        return chat_history, ""

    except Exception as e:
        print("Error:", e)
        chat_history.append((user_input, "Sorry, something went wrong."))
        return chat_history, ""

# Gradio UI
with gr.Blocks() as demo:
    gr.Markdown("## 🤖 Thoughtful AI Support Agent (Claude-powered)")
    chatbot = gr.Chatbot()
    msg = gr.Textbox(placeholder="Ask a question about Thoughtful AI...", show_label=False)
    clear = gr.Button("Clear")

    msg.submit(thoughtful_agent_claude, [msg, chatbot], [chatbot, msg])
    clear.click(lambda: [], None, chatbot)

demo.launch()