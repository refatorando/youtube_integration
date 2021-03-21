from youtube_client import YoutubeClient
import time, thumb

def run():
    yt = YoutubeClient()

    while True:
        video_id = "W9Zh0nhqR3Y"
        comments = yt.video_comments(video_id)
        final_img = thumb.create_thumbnail(comments)
        yt.set_thumbnail(video_id, final_img)
        time.sleep(15)

if __name__ == '__main__':
    run()