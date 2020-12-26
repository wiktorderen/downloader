from pytube import YouTube
from win10toast import ToastNotifier

def downloader():
    try:
        url = input("Give the URL of the YouTube video: ")
        yt = YouTube(url)
        videos = yt.streams.all()
        i = 1
        for v in videos:
            print(str(i) + "." + " " + str(v))
            i += 1
        vdo_number = int(input("Enter the number of video to download: "))
        video = videos[vdo_number - 1]
        video.download('C:\\Users\\Wikto\\Downloads')
        print("Your file is downloaded")
        notify = ToastNotifier()
        notify.show_toast("Your file is downloaded", duration=5)

    except Exception:
        print("Error")

downloader()