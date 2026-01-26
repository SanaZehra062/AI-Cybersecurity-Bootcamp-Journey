# This code is for using Azure Speech Service with Python.
import azure.cognitiveservices.speech as speechsdk
speech_key = "enter your key"
service_region = "enter your region"  
speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)
speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)
print("Say something...")
result = speech_recognizer.recognize_once()
print("You said:", result.text)
speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config)
speech_synthesizer.speak_text_async("Hello Sana Zehra, this is Azure Speech Service speaking!").get()