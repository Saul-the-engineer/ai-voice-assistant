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
