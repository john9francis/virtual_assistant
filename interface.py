import speech_recognition

def listen():
  '''
  Uses the microphone to get an audio input and returns it
  as an AudioData object.
  '''
  recognizer = speech_recognition.Recognizer()
  with speech_recognition.Microphone() as source:
    print("Listening...")
    audio = recognizer.listen(source)
    return audio
  

def audio_to_text(audio):
  '''
  Takes in an AudioData object, parses it, and returns
  the audio as a string. 
  '''
  recognizer = speech_recognition.Recognizer()
  try:
    text = recognizer.recognize_google(audio)
    return text
  except:
    return ""
  


def main():

  running = True

  while running:
    # infinitely listen and parse inputs
    audio = listen()
    user_sentence = audio_to_text(audio)

    # if the user says stop, end the loop
    if user_sentence == "stop":
      running = False

    # for now, just print the sentence
    print(user_sentence)




if __name__ == "__main__":
  main()