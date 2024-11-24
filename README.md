# AI Voice Assistant
<p align="center">
  <img src="assets/ai-voice-assistant.png" alt="AI Voice Assistant">
</p>

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
  - [Setup Instructions (Recommended)](#setup-instructions-recommended)
    - [Install git-lfs (Git Large File System)](#install-git-lfs-git-large-file-system)
    - [Clone Required Models](#clone-required-models)
    - [Run the Application](#run-the-application)
  - [Local Development](#local-development)
    - [Backend Setup](#backend-setup)
    - [Frontend Setup](#frontend-setup)
    - [or if you prefer using yarn](#or-if-you-prefer-using-yarn)
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
```
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
```

## Requirements

### Backend

- Python >= 3.8
- FFmpeg

### Frontend

- NodeJS >= 18
- Yarn or npm

## Setup Instructions (Recommended)
Follow these steps to set up the environment and get the project running on your machine.

### Clone this repository
```bash
git clone git@github.com:Saul-the-engineer/ai-voice-assistant.git
```

### Install git-lfs (Git Large File System)

Git Large File Storage (LFS) is used to manage large files, such as model weights, which are essential for running this application. Execute the following commands in your terminal:

```bash
sudo apt-get update
sudo apt-get install git-lfs
git lfs install
```

### Clone Required Models
The project requires specific models hosted on Hugging Face. You need to clone these models into the backend/models/ directory. This step will require your Hugging Face credentials:
```bash
cd backend/models/
git clone https://huggingface.co/meta-llama/Llama-3.2-1B-Instruct
```

### Run the Application
To simplify setting up and running the necessary services, the project uses Docker. Make sure Docker and Docker Compose are installed on your system. Then, run the following command to start all services using Docker Compose. This command also navigates you to the root of the project directory before starting the services:
  
  ```bash
cd $(git rev-parse --show-toplevel)
docker-compose up
```
This setup will build and run the containers specified in your docker-compose.yml file, setting up the necessary environment for the AI Voice Assistant.


## Local Development
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
This project's frontend is built with Next.js. Follow these steps to set it up:

Install Node Version Manager (NVM): Manage multiple Node.js versions easily:

```bash
curl https://raw.githubusercontent.com/creationix/nvm/master/install.sh | bash
Install Node.js and Yarn: Use NVM to install Node.js and then install Yarn:
```

```bash
nvm install node # Installs the latest version of node
npm install --global yarn
Install Frontend Dependencies: Navigate to the frontend directory and install required npm packages:
```

```bash
cd frontend
npm install
# Additional specific packages
npm install react-audio-voice-recorder
npm install react-loading
Run the Development Server: Start the frontend development server and open the application in your web browser:
```

```bash
npm run dev
```
### or if you prefer using yarn
```bash
yarn dev
```

Access the application by navigating to http://localhost:3000 in your web browser. The site updates automatically as you edit the files.

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
