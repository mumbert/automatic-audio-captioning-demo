import gradio as gr
import app_clap

def main():


    demo = gr.TabbedInterface([app_clap.create_app()], 
                            ["Non Real Time ASR demo"])

    demo.launch()

if __name__ == "__main__":
    main()