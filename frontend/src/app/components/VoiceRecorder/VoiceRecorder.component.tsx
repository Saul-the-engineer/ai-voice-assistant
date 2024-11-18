import { AudioRecorder, useAudioRecorder } from "react-audio-voice-recorder";

export interface VoiceRecorderProps{
    onAudioRecordingComplete: (audioData: Blob) => void;
}

// This button will only be visible when the recording is not in progress
// When recording is finished, send the audio data to the parent component
const VoiceRecorder = ({onAudioRecordingComplete}:VoiceRecorderProps)=>{
    const recorderControls = useAudioRecorder();
    return (
        <div>
          <AudioRecorder
            onRecordingComplete={onAudioRecordingComplete}
            recorderControls={recorderControls}
          />
          {recorderControls.isRecording && (
            <button onClick={recorderControls.stopRecording}>Stop recording</button>
          )}
        </div>
    )
}


export default VoiceRecorder
