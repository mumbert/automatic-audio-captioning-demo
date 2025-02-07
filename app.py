import gradio as gr
import app_clap
import app_dcase

def main():

    demo = gr.TabbedInterface([app_dcase.create_app(), app_clap.create_app()], 
                            ["DCASE demo", "CLAP demo"])

    demo.launch()

if __name__ == "__main__":
    main()