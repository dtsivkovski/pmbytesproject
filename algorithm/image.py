import numpy
import base64
from io import BytesIO
from PIL import Image, ImageFilter, ImageDraw
import PIL.ImageOps


# image (PNG, JPG) to base64 conversion (string), learn about base64 on wikipedia https://en.wikipedia.org/wiki/Base64
def image_base64(img, img_type):
    with BytesIO() as buffer:
        img.save(buffer, img_type)
        return base64.b64encode(buffer.getvalue()).decode()


# formatter preps base64 string for inclusion, ie <img src=[this return value] ... />
def image_formatter(img, img_type):
    return "data:image/" + img_type + ";base64," + image_base64(img, img_type)


# color_data prepares a series of images for data analysis
def image_data(path="static/img/", img_list=None):  # path of static images is defaulted
    if img_list is None:  # color_dict is defined with defaults
        img_list = [
            {'source': "Andrew Haimerl", 'label': "unsplash.com", 'file': "citysmall.jpg", 'processing': "drawn"},
            {'source': "Toa Heftiba", 'label': "unsplash.com", 'file': "lanterns.jpg", 'processing': "inverted"},
            {'source': "White", 'label': "unsplash.com", 'file': "bluecity.jpg", 'processing': "gaussian"},
            {'source': "Zishan Khan", 'label': "unsplash.com", 'file': "rgbleds.jpg", 'processing': "none"},
        ]
    # gather analysis data and meta data for each image, adding attributes to each row in table
    for img_dict in img_list:
        img_dict['path'] = '/' + path  # path for HTML access (frontend)
        file = path + img_dict['file']  # file with path for local access (backend)
        processing = img_dict['processing']
        # Python Image Library operations
        if processing == "gaussian":
            # GAUSSIAN BLUR IMAGE OPERATION
            origImage = Image.open(file)
            gaussImage = origImage.filter(ImageFilter.GaussianBlur(5))
            gaussImage.save("static/TestImages/gaussian/" + img_dict['file'])
            gaussFile = "static/TestImages/gaussian/" + img_dict['file']
            img_reference = Image.open(gaussFile)
        elif processing == "drawn":
            # CIRCLE DRAWING IMAGE OPERATION
            origImage = Image.open(file)
            d1 = ImageDraw.Draw(origImage)
            d1.ellipse((14, 18, 150, 150), fill=(255, 0, 0))
            origImage.save("static/TestImages/drawn/" + img_dict['file'])
            drawnFile = "static/TestImages/drawn/" + img_dict['file']
            img_reference = Image.open(drawnFile)
        elif processing == "inverted":
            # INVERTED COLOR IMAGE OPERATION
            origImage = Image.open(file)
            invert = PIL.ImageOps.invert(origImage)
            invert.save("static/TestImages/inverted/" + img_dict['file'])
            invertFile = "static/TestImages/inverted/" + img_dict['file']
            img_reference = Image.open(invertFile)
        else:
            # IMAGE REFERENCE IF NO PROCESSING TYPE
            img_reference = Image.open(file)
        img_data = img_reference.getdata()  # Reference https://www.geeksforgeeks.org/python-pil-image-getdata/
        img_dict['format'] = img_reference.format
        img_dict['mode'] = img_reference.mode
        img_dict['size'] = img_reference.size
        # Conversion of original Image to Base64
        img_dict['base64'] = image_formatter(img_reference, img_dict['format'])
        # Numpy array usage
        img_dict['data'] = numpy.array(img_data)
        img_dict['hex_array'] = []
        img_dict['binary_array'] = []
        img_dict['gray_data'] = []
        # 'data' is a list of RGB data, the list is traversed and hex and binary lists are calculated and formatted
        for pixel in img_dict['data']:
            # hexadecimal conversions
            hex_value = hex(pixel[0])[-2:] + hex(pixel[1])[-2:] + hex(pixel[2])[-2:]
            hex_value = hex_value.replace("x", "0")
            img_dict['hex_array'].append("#" + hex_value)
            # binary conversions
            bin_value = bin(pixel[0])[2:].zfill(8) + " " + bin(pixel[1])[2:].zfill(8) + " " + bin(pixel[2])[2:].zfill(8)
            img_dict['binary_array'].append(bin_value)
            # create gray scale of image, ref: https://www.geeksforgeeks.org/convert-a-numpy-array-to-an-image/
            average = (pixel[0] + pixel[1] + pixel[2]) // 3
            if len(pixel) > 3:
                img_dict['gray_data'].append((average, average, average, pixel[3]))
            else:
                img_dict['gray_data'].append((average, average, average))
        img_reference.putdata(img_dict['gray_data'])
        img_dict['base64_gray'] = image_formatter(img_reference, img_dict['format'])
        img_dict['hex_array_gray'] = []
        img_dict['binary_array_gray'] = []
        # 'data' = RGB data, 'gray_data' is grayscale data
        for pixel in img_dict['gray_data']:
            # hexadecimal
            hex_value = hex(pixel[0])[-2:] + hex(pixel[1])[-2:] + hex(pixel[2])[-2:]
            hex_value = hex_value.replace("x", "0")
            img_dict['hex_array_gray'].append("#" + hex_value)
            # binary
            bin_value = bin(pixel[0])[2:].zfill(8) + " " + bin(pixel[1])[2:].zfill(8) + " " + bin(pixel[2])[2:].zfill(8)
            img_dict['binary_array_gray'].append(bin_value)
    return img_list  #


# run this as standalone tester to see data printed in terminal
#   if __name__ == "__main__":
#     local_path = "../static/img/"
#     img_test = [
#         {'source': "iconsdb.com", 'label': "Blue square", 'file': "blue-square-16.png"},
#     ]
#     items = image_data(local_path, img_test)  # path of local run
#     for row in items:
#         # print some details about the image so you can validate that it looks like it is working
#         # meta data
#         print("---- meta data -----")
#         print(row['label'])
#         print(row['format'])
#         print(row['mode'])
#         print(row['size'])
#         # data
#         print("----  data  -----")
#         print(row['data'])
#         print("----  gray data  -----")
#         print(row['gray_data'])
#         print("----  hex of data  -----")
#         print(row['hex_array'])
#         print("----  bin of data  -----")
#         print(row['binary_array'])
#         # base65
#         print("----  base64  -----")
#         print(row['base64'])
#         # display image
#         print("----  render and write in image  -----")
#         filename = local_path + row['file']
#         image_ref = Image.open(filename)
#         draw = ImageDraw.Draw(image_ref)
#         draw.text((0, 0), "Size is {0} X {1}".format(*row['size']))  # draw in image
#         image_ref.show()
# print()
