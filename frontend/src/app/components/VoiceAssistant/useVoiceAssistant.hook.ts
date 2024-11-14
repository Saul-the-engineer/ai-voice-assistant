import { getAIReplyOutput } from "@/app/services/aivoiceassistant.service"
import {useState} from "react"


const useVoiceAssistant = ()=>{
    // Front end is waiting for the AI to process the user's voice input
    const [isWaitingAIOutput,setIsWaitingAIOutput] = useState<boolean>(false)
    const [lastAIReplyURL,setLastAIReplyURL] = useState<string|undefined>(undefined)

    const handleUserVoiceRecorded = async(userAudioData:Blob)=>{
        setIsWaitingAIOutput(true)
        const result = await getAIReplyOutput(userAudioData)
        setIsWaitingAIOutput(false)
        if(result){
            const url = URL.createObjectURL(result)
            setLastAIReplyURL(url)
        }

    }

    const handleOnAudioPlayEnd = ()=>{
        setLastAIReplyURL(undefined)
    }
    return{
        handleUserVoiceRecorded,
        isWaitingAIOutput,
        lastAIReplyURL,
        handleOnAudioPlayEnd
    }
}


export default useVoiceAssistant