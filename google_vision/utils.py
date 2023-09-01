from datetime import datetime

from importlib.resources import path
import os,io
from google.cloud import vision 
import cv2
import numpy as np

from google_vision_app import settings

os.environ['GOOGLE_APPLICATION_CREDENTIALS']= r'media/visionapiflutter-90130e680dd0.json'

client = vision.ImageAnnotatorClient()

def draw_objects_on_image(img_path, objects):
    image = cv2.imread(img_path)

    for object_ in objects:
        vertices = []
        for vertex in object_.bounding_poly.normalized_vertices:
            x = int(vertex.x * image.shape[1])
            y = int(vertex.y * image.shape[0])
            vertices.append((x, y))
        
        # Çokgen köşeleri çizme
        cv2.polylines(image, [np.array(vertices)], isClosed=True, color=(0, 255, 0), thickness=2)
        
        # Nesne adını ve güven seviyesini yazdırma
        label = f"{object_.name} ({object_.score:.2f})"
        font = cv2.FONT_HERSHEY_SIMPLEX
        font_scale = 0.5
        font_color = (0, 0, 0)
        font_thickness = 2
        font_line_type = cv2.LINE_AA
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(image, label, (vertices[0][0], vertices[0][1] - 10), font, font_scale, font_color, font_thickness, font_line_type)
    
    
    now = datetime.now()
    timestamp = now.strftime("%Y%m%d%H%M%S")
    # Dosya adını oluşturun
    filename = f"{timestamp}.jpg"
    # Dosya yolunu oluşturun
    filepath = os.path.join(settings.MEDIA_ROOT, 'results', filename)
    cv2.imwrite(filepath, image)
    data = f"media/results/{filename}"
    
    return data

def detectObjects(img_path):

    with io.open (img_path, 'rb') as image_file: 
        content = image_file.read()

    image = vision.Image(content=content)

    objects = client.object_localization(image=image).localized_object_annotations

    """
    print(f"Bulunan Nesne Sayısı: {len(objects)}")
    for object_ in objects:
        print(f"\n{object_.name} (Güven Seviyesi: {object_.score})")
        print("Normalleştirilmiş sınırlayıcı çokgen köşeleri: ")
        for vertex in object_.bounding_poly.normalized_vertices:
            print(f" - ({vertex.x}, {vertex.y})")
    """
    return draw_objects_on_image(img_path, objects)

