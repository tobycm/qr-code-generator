"""
Main module file
"""

# from PIL import Image, ImageDraw, ImageOps
from PIL import Image

from qrcode import QRCode, ERROR_CORRECT_H
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer

def generate_qr_code(input_data) -> Image:
    """
    Generate and return a qr code in PILImage form.
    """

    qr = QRCode(
        version = None,
        error_correction = ERROR_CORRECT_H,
        box_size = 10,
        border = 5
    )
    qr.add_data(input_data)
    qr.make(fit = True)

    qr_code = qr.make_image(image_factory = StyledPilImage, module_drawer = RoundedModuleDrawer())

    # mask = Image.new("L", (qr_code.pixel_size, qr_code.pixel_size), 0)
    # draw = ImageDraw.Draw(mask)
    # draw.ellipse((qr_code.pixel_size, qr_code.pixel_size) + (150, 150), fill=255)
    # mask = ImageOps.fit(mask, (qr_code.pixel_size, qr_code.pixel_size), centering = (0.5, 0.5))

    # qr_code.putalpha(mask)

    return qr_code
