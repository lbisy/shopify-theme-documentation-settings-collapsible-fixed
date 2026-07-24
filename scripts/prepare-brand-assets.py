from pathlib import Path

from PIL import Image, ImageDraw


ROOT = Path(__file__).resolve().parents[1]
BRAND_DIR = ROOT / "docs" / "public" / "brand"
SOURCE = BRAND_DIR / "esen-logo-transparent.png"


def contain(image: Image.Image, size: tuple[int, int], padding: int) -> Image.Image:
    canvas = Image.new("RGBA", size, (0, 0, 0, 0))
    available = (size[0] - padding * 2, size[1] - padding * 2)
    fitted = image.copy()
    fitted.thumbnail(available, Image.Resampling.LANCZOS)
    position = ((size[0] - fitted.width) // 2, (size[1] - fitted.height) // 2)
    canvas.alpha_composite(fitted, position)
    return canvas


source = Image.open(SOURCE).convert("RGBA")
full_bbox = source.getbbox()
if full_bbox is None:
    raise RuntimeError("The source logo is empty.")

full_logo = source.crop(full_bbox)
full_logo = contain(full_logo, (640, 360), 24)
full_logo.save(BRAND_DIR / "esen-logo.png", optimize=True)

upper_region = source.crop((0, 0, source.width, int(source.height * 0.55)))
mark_bbox = upper_region.getbbox()
if mark_bbox is None:
    raise RuntimeError("The Esen mark could not be detected.")

mark = upper_region.crop(mark_bbox)
tile = Image.new("RGBA", (256, 256), (0, 0, 0, 0))
mask = Image.new("L", tile.size, 0)
ImageDraw.Draw(mask).rounded_rectangle((4, 4, 251, 251), radius=48, fill=255)
white_tile = Image.new("RGBA", tile.size, (255, 255, 255, 255))
tile.alpha_composite(Image.composite(white_tile, tile, mask))
tile.alpha_composite(contain(mark, tile.size, 34))
tile.save(BRAND_DIR / "esen-mark.png", optimize=True)

tile.resize((180, 180), Image.Resampling.LANCZOS).save(
    BRAND_DIR / "apple-touch-icon.png",
    optimize=True,
)
tile.save(
    BRAND_DIR / "favicon.ico",
    sizes=[(16, 16), (32, 32), (48, 48)],
)

print("Created Esen navigation logo and favicon assets.")
