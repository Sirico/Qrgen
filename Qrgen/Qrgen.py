# import modules
import qrcode
from PIL import Image
import PySimpleGUI as sg

sg.theme('DarkAmber')  # Theme
# All the stuff inside your window.
layout = [[sg.Text('Enter Data              '), sg.InputText()],
          [sg.Text('Enter Filename        '), sg.InputText()],
          [sg.Text('Enter Bgcolour        '), sg.InputText()],
          [sg.Text('Enter Fgcolour        '), sg.InputText()],
          [sg.Text('Enter Logo Location'), sg.InputText()],
          [sg.Button('Submit')], ]


# Create the Window
window = sg.Window('QR Code Generator', layout).Finalize()
# window.Maximize()

#Text Fields write to varibles
values: object
button,values=window.Read()
link = values [0]
filename = values[1]
bgcolour =  values [2]
fgcolour = values [3]
Logo = values [4]

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event in (None, 'Submit'):  # if user closes window or clicks submit
        break

window.close()
######## Code below stays ##################
# user inputs
#link = input("What is the url you want to use?")
#filename = input('name the file ')
#bgcolour = input('enter background colour ')
#fgcolour = input('enter foreground colour ')
#Logo = input('copy image location')

# taking image which user wants
# in the QR code center
Logo_link = Logo

logo = Image.open(Logo_link)

# taking base width
basewidth = 100

# adjust image size
wpercent = (basewidth / float(logo.size[0]))
hsize = int((float(logo.size[1]) * float(wpercent)))
logo = logo.resize((basewidth, hsize), Image.ANTIALIAS)
QRcode = qrcode.QRCode(
    error_correction=qrcode.constants.ERROR_CORRECT_H
)

# taking url or text
url = link

# addingg URL or text to QRcode
QRcode.add_data(url)

# generating QR code
QRcode.make()

# taking forground color name from user
QRcolor = fgcolour

# adding color to QR code
QRimg = QRcode.make_image(
    fill_color=QRcolor, back_color=bgcolour).convert('RGB')

# set size of QR code
pos = ((QRimg.size[0] - logo.size[0]) // 2,
       (QRimg.size[1] - logo.size[1]) // 2)
QRimg.paste(logo, pos)

# save the QR code generated
QRimg.save(filename + ".png")
sg.Popup('QR Generated!!')

