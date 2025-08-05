# 🧠 Chotu - Your Personal AI Assistant

This is a Python-based AI assistant inspired by *Jarvis*, capable of:

- 🔍 Searching the web  
- 🌤️ Weather checking
- 📷 Vision through camera (Web app)
- 🗣️ Speech
- 📝 Chat (Web app)

This agent uses LiveKit and have implemented tools such as Weather checking and Web searchng.\
The Web app allows the assistant to monitor the user via Web cam and answer any questions \
involving realtime web footage (such as-How many fingers am i holding?)

1. Create the Virtual Envrionment first!
   Use commands:
   <pre><code>python -m venv venv</code></pre>
2. Activate it
   Use commands:
   <pre><code>./venv/Scripts/activate</code></pre>
3. Install all the required libraries in the requirements.txt file
   Use commands:
   <pre><code>pip install -r .\requirements.txt</code></pre>
   <pre><code>python agent.py download-files</code></pre>
4. In the .ENV - File you should paste your API-Keys(Google and LiveKit) and your LiveKit Secret, LiveKit URL.
5. Make sure that your LiveKit Account is set-up correctly. 
6. To run the agent, use commands:
   <pre><code>python ./agent.py console</code></pre>
7. To run the agent in Web app and access vision through camera
   Go to https://agents-playground.livekit.io and
   Use commands:
   <pre><code>python ./agent.py dev</code></pre>
