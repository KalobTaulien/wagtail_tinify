# Wagtail TinyPNG
A custom Wagtail Image Model and function for compressing images on upload through the admin with TinyPNG.

> The benefit to using this package is your source image is minified without losing quality. And all of your wagtail image renditions will be smaller because of this as well.

## Installation
1. `pip install wagtail-tinify`
2. Add `wagtail_tinify` to your `INSTALLED_APPS`
3. Run `python3 manage.py migrate wagtail_tinify`
4. In your `settings.py` file, add `WAGTAILIMAGES_IMAGE_MODEL = 'wagtail_tinify.CustomImage'`
5. Add yout [TinyPNG Developer API Key](https://tinypng.com/developers) to `settings.py` with `TINIFY_API_KEY = "your_api_key_here"`
6. Overwrite the wagtail multiple image add function in your urls. 
 * `from wagtail_tinify.views import add`
 * Put this above your `wagtailadmin_urls`: `url(r"^admin/images/multiple/add/", add)`
7. Test by uploading a file in the Wagtail admin. It will take a bit longer than usual because it will run every image through TinyPNG.

## Todos
- Add proper TinyPNG exception handling