
import gradio as gr
from msclap import CLAP

clap_model = CLAP(version = 'clapcap', use_cuda=False)

def clap_inference(mic=None, file=None):

    if mic is not None:
        audio = mic
    elif file is not None:
        audio = file
    else:
        return "You must either provide a mic recording or a file"

    # Generate captions for the recording
    captions = clap_model.generate_caption([audio], 
                                           resample=True, 
                                           beam_size=5, 
                                           entry_length=67, 
                                           temperature=0.01)

    return captions[0]

def create_app():

    with gr.Blocks() as demo:
        gr.Markdown(
            """
            # DCASE demo for automatic audio captioning
            """
        )
        gr.Interface(
            fn=clap_inference,
            inputs=[
                gr.Audio(sources="microphone", type="filepath"),
                gr.Audio(sources="upload", type="filepath"),
            ],
            outputs="text",
        )

    return demo

def main():
    
    app = create_app()
    app.launch(debug=True)

    
if __name__ == "__main__":
    main()

