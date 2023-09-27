import whisper
import os

# transcribe new lectures
filenames = os.listdir('data/new')

print(filenames)

for filename in filenames:

    print(filename)

    model = whisper.load_model("base.en")
    result = model.transcribe(f"data/{filename}")
    #print(result["text"])

    with open(f"logs/{filename}.log", "w") as f:
        f.write(result["text"])
