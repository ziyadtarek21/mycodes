from pytube import YouTube
from pytube.extract import playlist_id
link=input("please enter the video url: ")
video = YouTube(link)
#print(f"the video title is:\n{video.title}\n-----------")
#print(f"the video description is:\n{video.description}\n-----------")
#print(f"the video views are:\n{video.views}\n-----------")
#print(f"the video dureation is:\n{video.length/60}minutes\n-----------")
#print(f"the video rating is:\n{video.rating}\n-----------")
#print(video.streams)

#for stream in video.streams.filter(progressive=True):
 #print(stream)
print(video.streams.get_highest_resolution())
video.streams.get_highest_resolution().download(output_path="D:\youtube")
def finish():
    print("download completed")

video.register_on_complete_callback(finish())    

