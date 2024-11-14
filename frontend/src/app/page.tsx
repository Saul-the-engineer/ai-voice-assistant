import styles from "./page.module.css";
import VoiceAssistant from "./components/VoiceAssistant/VoiceAssistant.component";

export default function Home() {
  return (
    <>
      <main className={styles.page}>
        <VoiceAssistant />
      </main>
    </>
  );
}
