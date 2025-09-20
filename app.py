import gradio as gr
from tutor_client import TutorClient
from storage import Storage

tutor = TutorClient()
storage = Storage()

def handle_question(user_question, level):
    final_response = ""
    for partial in tutor.ask(user_question, level):
        final_response = partial
        yield partial
    # Save logs after final response
    storage.save_question(user_question)
    storage.save_response(final_response)
    storage.save_qna(user_question, final_response)

with gr.Blocks(title="AI Tutor") as demo:
    gr.Markdown("## 📘 AI Tutor\nAsk any question and choose how deeply you'd like it explained.")

    with gr.Row():
        question = gr.Textbox(
            lines=3,
            placeholder="Ask AI Tutor anything...",
            label="Your Question",
            scale=3
        )
        level = gr.Slider(
            minimum=1, maximum=6, step=1,
            label="Explanation Level", value=3, scale=1
        )

    answer = gr.Markdown(label="AI Tutor's Answer", elem_id="answer_box", height=400)
    submit_btn = gr.Button("Get Answer")
    submit_btn.click(fn=handle_question, inputs=[question, level], outputs=answer)

demo.launch(share=True)
