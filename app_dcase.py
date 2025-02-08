##########################################################################
# FAKE: USES CLAP 
##########################################################################
import gradio as gr
from msclap import CLAP
import gdown

clap_model = CLAP(version = 'clapcap', use_cuda=False)

def dcase_inference(mic=None, file=None):
    # FAKE: USES CLAP AT THE MOMENT

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

##########################################################################

# import gradio as gr
# from transformers import pipeline
# import torchaudio
# import torch
# from dcase24t6.nn.hub import baseline_pipeline
# import os
# import gdown

CHECKPOINT_FILE = "epoch_232-step_001864-mode_min-val_loss_3.3752.ckpt"

def download_dcase_model_checkpoint():

    url = "https://drive.google.com/uc?id=1JABWIBlHuLAhYPX5ktbyLniH-YpeRyeT"
    gdown.download(url, CHECKPOINT_FILE, quiet=False)

# def dcase_inference(mic=None, file=None):

#     if mic is not None:
#         audio = mic
#     elif file is not None:
#         audio = file
#     else:
#         return "You must either provide a mic recording or a file"

#     waveform, sample_rate = torchaudio.load(audio)
#     model = baseline_pipeline(CHECKPOINT_FILE)
#     item = {"audio": waveform, "sr": sample_rate} # 44100
#     outputs = model(item)
#     return outputs["candidates"][0]

def create_app():

    with gr.Blocks() as demo:
        gr.Markdown(
            """
            # DCASE demo for automatic audio captioning
            """
        )
        gr.Interface(
            fn=dcase_inference,
            inputs=[
                gr.Audio(sources="microphone", type="filepath"),
                gr.Audio(sources="upload", type="filepath"),
            ],
            outputs="text",
        )

    return demo

download_dcase_model_checkpoint()

def main():
    
    app = create_app()
    app.launch(debug=True)

    
if __name__ == "__main__":
    main()

