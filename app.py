from elevenlabs import generate, play, voices, save
from keys import my_api_key

voices_available =voices()


while True:
    content = input("Enter a text of 50 characters:")

    if len(content)<=50:
        hello=generate(
        api_key=my_api_key,
        text=content,
        voice=voices_available[5],
        model="eleven_multilingual_v2",
        output_format= "mp3_44100_128"
    )
        play(audio=hello)

        to_save = input("do you want to save the audio? Enter Y for yes and N for no: ").lower()
        if to_save == "y":
            path = input('enter file path: ')
            save(hello, filename=path)
        else:
            break
    else:
        print("Your input exceeds the maximum character length")
        content=""
    break