from pytube import YouTube
link = "https://www.youtube.com/watch?v=HtMF973tXIY"
my_video = YouTube(link)
#print(my_video.title)
#print(my_video.thumbnail_url)
videos=my_video.streams.all()
x=list(enumerate(videos))
for i in x:
    print(i)
strm=int(input("Enter index n0:"))
videos[strm].download()
print('Successfully')
  