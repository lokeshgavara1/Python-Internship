'''
#YOUTUBE VIDEO DOWNLOADER WITH URL:
#pip install pytube

import pytube
link=input("enter your URL")
yt=pytube.YouTube(link)
yt.streams.first().download()
print("download",link)
'''

#CONVERTING IMAGE TO PDF
from fpdf import pdf
pdf=FPDF()
list_of_images=["1.jpg","2.jpg"]
for i in list_of_images:#list of images with filename
    pdf.add_page()
    pdf.image(i,x,y,w,h)

pad.output("yourfile.pdf","F")
