supported_apps = ['WhatsApp', 'Tinder']
supported_extensions = ['.jpg', '.png', '.jpeg']

# select app by uncommenting any one, or pass using cmd argument
# app = 'WhatsApp'
app = 'Tinder'

# user config GENERAL
source_images_path = 'S:\Media\\2018-\Oneplus 6\Screenshots'

# user config TINDER
tinderblue = (33, 185, 252)

# user config WHATSAPP
whatsappgreen = [(7, 94, 85), (35, 45, 54)]


# set range of rows in column to scan for app specific color
def heightrange(img):
    if app == 'Tinder':
        return (30, img.height - 100)
    elif app == 'WhatsApp':
        return (10, int(img.height / 3))


# check if any value in rowcolors matches the signature color of the app
def checkifappss(rowcolors, img):
    if app == 'WhatsApp':
        if whatsappgreen[0] in rowcolors or whatsappgreen[1] in rowcolors:
            return True
    elif app == 'Tinder':
        if tinderblue in rowcolors and img.getpixel((5, 180)) == (255, 255, 255):
            return True
    return False
