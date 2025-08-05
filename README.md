# 🧠 Chotu – Your Personal AI Assistant
Chotu is a Python-based AI assistant inspired by Jarvis, designed to perform a variety of intelligent tasks, including:

🔍 Web Search – Get answers instantly from the internet

🌤️ Weather Updates – Check real-time weather conditions

📷 Vision via Webcam (Web App) – Analyze real-time video to answer visual questions like "How many fingers am I holding?"

🗣️ Speech Recognition & Interaction – Talk to Chotu using your voice

💬 Interactive Chat (Web App) – Text-based conversations through an intuitive web interface

The assistant is powered by LiveKit for real-time audio/video communication and includes integrated tools for weather checking and web searching. With webcam access in the web app, Chotu can see and respond to real-world visual queries, making it a more immersive and practical AI companion.


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
