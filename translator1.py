from googletrans import Translator

translator = Translator()

text = input("Enter text: ")

result = translator.translate(text, dest="ta")

print("Translated Text:")
print(result.text)