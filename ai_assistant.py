import torch
import sounddevice as sd
from transformers import VitsModel, AutoTokenizer
from together import Together
from config import TOGETHER_API_KEY, SYSTEM_PROMPT

class AIConversation:
    def __init__(self):
        # Initialize Together AI client
        self.client = Together(api_key=TOGETHER_API_KEY)
        
        # Initialize TTS model
        self.tokenizer = AutoTokenizer.from_pretrained("facebook/mms-tts-eng")
        self.tts_model = VitsModel.from_pretrained("facebook/mms-tts-eng")

    def generate_text(self, user_input):
        """Use Together API with streaming"""
        try:
            response = self.client.chat.completions.create(
                model="meta-llama/Llama-2-7b-chat-hf",
                messages=[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": user_input}
                ],
                temperature=0.7,
                top_p=0.9,
                max_tokens=500,
                stream=True
            )
            
            # Stream the response
            full_response = []
            print("AI: ", end="", flush=True)
            for chunk in response:
                if chunk.choices[0].delta.content:
                    token = chunk.choices[0].delta.content
                    print(token, end="", flush=True)
                    full_response.append(token)
            
            return "".join(full_response).strip()
        
        except Exception as e:
            raise Exception(f"API Error: {str(e)}")

    def text_to_speech(self, text):
        """Convert text to speech and play directly"""
        try:
            inputs = self.tokenizer(text, return_tensors="pt")
            with torch.no_grad():
                output = self.tts_model(**inputs).waveform
            
            # Convert to numpy array and play
            audio_np = output.numpy().T
            sd.play(audio_np, samplerate=self.tts_model.config.sampling_rate)
            sd.wait()
            
        except Exception as e:
            print(f"TTS Error: {str(e)}")

    def chat(self):
        print("Starting conversation... (type 'quit' to exit)")
        try:
            while True:
                user_input = input("\nYou: ")
                if user_input.lower() == 'quit':
                    break
                
                # Generate and process response
                response = self.generate_text(user_input)
                self.text_to_speech(response)
                
        except KeyboardInterrupt:
            print("\nConversation ended.")
        finally:
            sd.stop()

if __name__ == "__main__":
    assistant = AIConversation()
    assistant.chat()