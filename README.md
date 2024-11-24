# AI Voice Assistant

![AI Voice Assistant](assets/ai-voice-assistant.png)


This AI Voice Assistant is an open-source project leveraging modern technologies to create a responsive voice-activated chat interface. It utilizes Whisper for speech-to-text, Llama-3.2-1B-Instruct for generating chat responses, and gTTS (Google Text-to-Speech) for text-to-speech capabilities, all packaged within a FastAPI backend.

## System Architecture
The AI Voice Assistant is built using a modular architecture that allows for easy scaling and customization. The system consists of three main components:

1. **Frontend**: The frontend is built using React and Next.js, providing an interactive user interface for voice interaction. It allows users to record audio, send it to the backend for processing, and receive audio responses.
2. **Backend**: The backend is built using FastAPI, a modern Python web framework. It handles the processing of audio inputs, generates chat responses using the Llama-3.2-1B-Instruct model, and returns audio responses to the frontend.
3. **Models**: The system uses Whisper for speech-to-text conversion and Llama-3.2-1B-Instruct for generating chat responses. These models are hosted on the backend and are accessed via API endpoints.



## Table of Contents

- [AI Voice Assistant](#ai-voice-assistant)
  - [System Architecture](#system-architecture)
  - [Table of Contents](#table-of-contents)
  - [Features](#features)
  - [Technologies](#technologies)
  - [Repository Structure](#repository-structure)
  - [Requirements](#requirements)
    - [Backend](#backend)
    - [Frontend](#frontend)
  - [Setup Instructions](#setup-instructions)
    - [Backend Setup](#backend-setup)
    - [Frontend Setup](#frontend-setup)
  - [React and Next.js Setup](#react-and-nextjs-setup)
  - [Getting Started](#getting-started)
  - [Application Structure](#application-structure)
  - [Features](#features-1)
  - [Using the Application](#using-the-application)
  - [Available Scripts](#available-scripts)
  - [API Reference](#api-reference)
    - [Endpoints](#endpoints)
  - [License](#license)

## Features

- Voice command recognition via Whisper model.
- Intelligent conversational responses using the LLaMA 3.2 model.
- Real-time speech output using gTTS.
- Scalable and modular FastAPI backend.
- Interactive UI built with React and NextJS.

## Technologies

- **Backend**: Python, FastAPI
- **Speech-to-Text**: Whisper
- **NLP Model**: LLaMA 3.2
- **Text-to-Speech**: gTTS
- **Frontend**: React, NextJS

## Repository Structure
.
├── assets
├── backend
│   ├── assets
│   ├── htmlcov
│   ├── notebooks
│   ├── src
│   │   ├── app
│   │   │   ├── routers
│   │   │   ├── schemas
│   │   │   ├── services
│   │   │   └── utils
│   │   │       └── chat_utils
│   │   └── test.egg-info
│   ├── test-reports
│   │   └── htmlcov
│   └── tests
│       ├── fixtures
│       └── unit_tests
│           └── services
└── frontend
    ├── public
    └── src
        └── app
            ├── components
            │   ├── AudioPlayer
            │   ├── VoiceAssistant
            │   │   └── VoiceAssistantAvatar
            │   └── VoiceRecorder
            ├── fonts
            └── services

## Requirements

### Backend

- Python >= 3.8
- FFmpeg

### Frontend

- NodeJS >= 18
- Yarn or npm

## Setup Instructions

### Backend Setup

1. Install FFmpeg on your machine. Instructions vary by operating system:
   - **Ubuntu**: `sudo apt install ffmpeg`
   - **macOS**: `brew install ffmpeg`
   - **Windows**: Download from [FFmpeg's official site](https://ffmpeg.org/download.html).

2. Set up the Python environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: `.\venv\Scripts\activate`
   cd backend
   make install
   ```

3. Start the FastAPI server:
   ```bash
   uvicorn backend.src.app.main:create_app --reload
   ```

### Frontend Setup
This is a [Next.js](https://nextjs.org) project bootstrapped with [`create-next-app`](https://nextjs.org/docs/app/api-reference/cli/create-next-app).

## React and Next.js Setup
Before running must install a few things:
1) Node Version Manager (NVM)
```bash
curl https://raw.githubusercontent.com/creationix/nvm/master/install.sh | bash
```
2) yarn
```bash
npm install --global yarn
```
3) react-audio-voice-recorder
```bash
npm install react-audio-voice-recorder
```
4) react-loading
```bash
npm i react-loading
```

## Getting Started
Install the required packages by moving to the frontend directory (./frontend/) and running the following command:
```bash
npm install
```
This will install all the required dependencies for the frontend in a node_modules folder.

Next you can run the development server:

```bash
npm run dev
# or
yarn dev
```

Open [http://localhost:3000](http://localhost:3000) with your browser to see the result.

You can start editing the page by modifying `app/page.tsx`. The page auto-updates as you edit the file.

## Application Structure

- `components/`: Contains the React components for UI elements, including audio controls and display components.
- `app/page.tsx`: The main entry point.

## Features

- **Voice Interaction**: Users can interact with the voice assistant using spoken commands.
- **React Loading**: Provides visual feedback while waiting for responses from the backend.
- **Audio Playback**: Handles the playback of responses from the AI, creating an interactive experience.

## Using the Application

1. **Start Recording**: Click the microphone icon to begin recording your question or command.
2. **Stop Recording**: Click the stop button to end the recording session. The app will then process your input and return an audio response.
3. **Listen**: The response from the AI will automatically play through the browser.

## Available Scripts

In addition to the development server, you can use the following npm scripts:

```bash
npm run build
# Builds the application for production usage.

npm run start
# Runs the built application in production mode.

npm run lint
# Runs ESLint to check for linting errors in the codebase.
```

## API Reference
### Endpoints
```/voice-assistant/audio_interact```
Method: POST
Description: Accepts audio file uploads and returns audio responses after processing.
Content-Type: multipart/form-data
```/voice-assistant/text_interact```
Method: POST
Description: Accepts text input and returns a text response.
Content-Type: application/json
Body: { "text": "Your query here" }

## License
This project is licensed under Apache License 2.0. See the [LICENSE](LICENSE) file for more details.
