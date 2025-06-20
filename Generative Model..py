import g4f
from g4f.client import Client 
import gradio as gr 
 
client= Client() 
 
def generate_writing_prompt(user_input): 
    response = client.chat.completions.create(
        model=g4f.models.default,  
        messages=[{"role": "user", "content": user_input}]
    ) 
    return response.choices[0].message.content  # Ensure response is returned


interface=gr.Interface( 
    fn=generate_writing_prompt, 
    inputs=gr.Textbox(lines=3, placeholder="Enter a genre, tone, or initial plot point..."), 
    outputs="text", 
    title="Creative Writing Assistant          ", 
    description="Unleash your creativity! Get inspired with unique story ideas, prompts, and plot twists.", 
    theme="hugging face", 
    examples=[ 
        ["A story about a lost civilization discovering technology."], 
        ["Compose a poem about the changing seasons."], 
        ["A suspense thriller set in an abandoned mansion."], 
    ] 
) 
 
# Launch the interface 
if __name__=="__main__": 
    interface.launch()