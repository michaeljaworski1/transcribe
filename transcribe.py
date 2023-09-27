import whisper

filename = input()

model = whisper.load_model("base.en")
result = model.transcribe(f"data/{filename}")
#print(result["text"])

with open(f"logs/{filename}.log", "w") as f:
    f.write(result["text"])
