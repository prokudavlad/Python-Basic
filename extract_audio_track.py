import ffmpeg

input_file = "video.mp4"  # path to the output video file
output_file = "audio.mp3"  # path to save the audio file

stream = ffmpeg.input(video.mp4)
audio = stream.audio
output = ffmpeg.output(audio, audio.mp3)
ffmpeg.run(output)