import { getAIReplyOutput } from "@/app/services/aivoiceassistant.service"
import {useState} from "react"
import {v4} from "uuid";


const useVoiceAssistant = ()=>{
    // Front end is waiting for the AI to process the user's voice input
    const [isWaitingAIOutput,setIsWaitingAIOutput] = useState<boolean>(false)
    const [lastAIReplyURL,setLastAIReplyURL] = useState<string|undefined>(undefined)
    // Generate a unique user id for each user session
    const [userId,_] = useState<string>(v4())

    const handleUserVoiceRecorded = async(userAudioData:Blob)=>{
        setIsWaitingAIOutput(true)
        const result = await getAIReplyOutput(userAudioData, userId)
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
