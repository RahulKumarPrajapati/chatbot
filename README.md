# chatbot

# Setup
## Server side
    1. Create and enter in python virtual environment using command
        --> For windows:
            python3 -m venv env\chatbot
            env\chatbot\Scripts\activate
        --> For linux:
            python3 -m venv env/chatbot
            source env/chatbot/bin/activate
    2. Before installing requirements check if you have CMAKE and Microsoft Visual C++ Build Tools installed. These are required 
        to install llama-cpp-python. Go to https://python.langchain.com/v0.1/docs/integrations/llms/llamacpp/ for installations
        related guide for CPU and GPU(whatever you are using)
    3. pip install -r requirements.txt
    4. Model download
        - Run the command in the parent folder
        - Command --> huggingface-cli download TheBloke/Mistral-7B-Instruct-v0.2-GGUF mistral-7b-instruct-v0.2.Q5_K_M.gguf  --local-dir models/mistral --local-dir-use-symlinks False
        - Or you can run -->  curl -L --continue-at - -O https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.2-GGUF/resolve/main/mistral-7b-instruct-v0.2.Q5_K_M.gguf
        - Or download directly from https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.2-GGUF/resolve/main/mistral-7b-instruct-v0.2.Q5_K_M.gguf and past in your models/mistral directory.
    5. If you are a linux user change the models path th chatService.py file
        - Above command will create folder models/mistral/ and download the Mistral-7B-Instruct-v0.2-GGUF model in that folder.
    6. cd server && fastapi dev app.py

## Client side
    1. cd client
    2. npm install
    3. npm start