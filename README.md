Here's a comprehensive README.md file for your project:

```markdown
# AI Voice Assistant 🤖🎤

A conversational AI assistant combining Together.ai's language models with Hugging Face's text-to-speech capabilities for natural voice interactions.

## Features ✨
- Real-time conversation with streaming responses
- Human-like text-to-speech synthesis
- Configurable system prompts
- Error handling and graceful recovery
- CLI-based interaction

## Technologies Used 🛠️
- **Language Model**: Together.ai (Llama-2-7b-chat)
- **Text-to-Speech**: Facebook MMS-TTS (English)
- **Audio Playback**: SoundDevice
- **Core Framework**: Python 3.11+

## Installation 📦

### Prerequisites
- Python 3.11+
- Together.ai API key
- PortAudio library (for audio playback)

```bash
# Clone the repository
git clone https://github.com/yourusername/ai-voice-assistant.git
cd ai-voice-assistant

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt

# Install PortAudio (Mac/Linux)
brew install portaudio  # Mac
# sudo apt-get install portaudio19-dev  # Ubuntu/Debian
```

## Configuration ⚙️

1. Get your Together.ai API key from [their console](https://api.together.ai/)
2. Create `.env` file:
```ini
TOGETHER_API_KEY=your_api_key_here
```

3. Modify `config.py` to customize system behavior:
```python
SYSTEM_PROMPT = """[INST] <<SYS>>
You are a helpful AI assistant. Respond conversationally and keep answers brief.
<</SYS>>"""
```

## Usage 🚀
```bash
python ai_assistant.py

Starting conversation... (type 'quit' to exit)
You: Hello! 
AI: Hello there! How can I assist you today?
```

**Controls:**
- Type `quit` to exit
- Press `Ctrl+C` to interrupt any response

## Project Structure 📂
```
.
├── ai_assistant.py     # Main application logic
├── config.py           # Configuration and secrets
├── requirements.txt    # Dependency list
└── .env                # Environment variables
```

## Dependencies 📦
```ini
together>=0.2.3
sounddevice>=0.4.6
torch>=2.3.0
transformers>=4.40.0
python-dotenv>=1.0.0
```

## Future Enhancements 🚧
- [ ] Real-time voice input
- [ ] Multilingual support
- [ ] Emotion-aware speech synthesis
- [ ] Web interface
- [ ] Wake word detection

## Troubleshooting 🔧
**No audio output?**
- Verify PortAudio installation
- Check system sound settings
- Try reducing sample rate in `text_to_speech()`

**API Errors?**
- Verify Together.ai API key
- Check credit balance
- Try different model in `generate_text()`

## License 📄
MIT License - See [LICENSE](LICENSE) for details
```

