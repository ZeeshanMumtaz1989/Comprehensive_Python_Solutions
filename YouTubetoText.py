"""
Author: Zeeshan Mumtaz
Date: Feb 24, 2024
Description: Using this script the complete transcription of the YouTube Video
can be saved in a txt file.

"""


from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter


# retrieve the available transcripts
transcript_list = YouTubeTranscriptApi.list_transcripts('amJ-ev8Ial8')


# iterate over all available transcripts
for transcript in transcript_list:
    new_list = transcript.fetch()
    print(type(new_list))
  
    new_val = [m['text'] for m in new_list if 'text' in m]
    complete_text = ' '.join(new_val)

    with open('Extracted_Content.txt', 'w', encoding='utf-8') as file:
        file.write(complete_text)


    # with open('Extracted_Content.txt', 'w') as file:
    #     file.write(complete_text)

    file.close()

    