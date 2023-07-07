import json
from django.views.generic import View
from data_status import data_status_creative
from ..models import Creative, Category
from .random_str import *
from django.core.files.base import ContentFile
import base64
from PIL import Image
from io import BytesIO
from ..resize_image import *



class CreativeView(View):

    def get(self, request):
        crs = Creative.objects.all()
        data = []
        for cr in crs:
            # Get the URL of the image with `?width` and `height` parameters
            image_url = cr.image.url + f"?width={cr.width}&height={cr.height}"
            
            data.append({
                'external_id': cr.external_id,
                'name' : cr.name,
                'campaign_id': cr.campaign.id,
                'image_url': image_url
            })
        
        return data_status_creative(data)


    
    
    def post(self, request):
        data = json.loads(request.body)


        # Create a new Creative object using the data in the request body
        creative = Creative.objects.create(
            external_id=data['external_id'],
            name=data['name'],
            campaign_id=data['campaign']['id'],
            url=data.get('url', ''),
            width=data.get('width'),
            height=data.get('height')
        )

        # Save the image file from base64-encoded data
        image_url = save_image_from_base64(data, creative)
        if image_url:
            creative.url = 'http://192.168.0.49:8000/' + image_url
            creative.save()


        # Add categories to the creative
        category_codes = data['categories']
        for code in category_codes:
            try:
                code = code['code']
                category = Category.objects.get(code=code)
                creative.category.add(category)
            except Category.DoesNotExist:
                print("Shame")
        
        
        resized_img = resize_image(creative.image.path, creative.width, creative.height, fill_color='#FFFFFF')
        resized_img.save(creative.image.path, format='png')

        # Create the response data to return
        data = {
            'id': creative.id, 
            'external_id': creative.external_id,
            'name': creative.name,
            'categories': [{"id": category.id, 'code': category.code} for category in creative.category.all()],
            'campaign': {'id': creative.campaign.id},
            'heigth': creative.height,
            'width': creative.width,
            'url' : "https://theprivatetherapyclinic.co.uk/wp-content/uploads/2018/12/Weaponisation-768x384.jpg",
        }

        return data_status_creative(data)





def save_image_from_base64(data, creative):
    try:
        if 'file' not in data:
            print("Error: `data` dictionary does not contain `file` key.")
            return None
        
        # Decode base64-encoded image data and open as a Pillow image object
        img_data = base64.b64decode(data['file'])
        img = Image.open(BytesIO(img_data))

        # Generate unique filename and save image to a ContentFile object
        image_name = random_str(10) + ".png"
        img_file = ContentFile(img_data, name=image_name)

        # Set the image attribute of the creative object
        creative.image = img_file

        # Save the creative object to persist the image file
        creative.save()

        # Return the URL of the saved image
        return creative.image.url

    except IOError:
        print("Error: `img_data` is not a valid image file.")

    except Exception as e:
        print(f"Error: {str(e)}")

        print('creative.image:', creative.image)
        print('creative.image.path:', creative.image.path)