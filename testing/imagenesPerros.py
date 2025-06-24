import requests

# Cantidad de imágenes que querés traer
cantidad = 10

# URL de la API
url = f"https://dog.ceo/api/breeds/image/random/{cantidad}"

# Hacemos el request
response = requests.get(url)

# Verificamos que la respuesta sea OK
if response.status_code == 200:
    data = response.json()
    imagenes = data['message']
    print("URLs de imágenes de perros:")
    for idx, img_url in enumerate(imagenes, start=1):
        print(f"{idx}. {img_url}")
else:
    print("Error al obtener las imágenes:", response.status_code)


# 1. https://images.dog.ceo/breeds/terrier-australian/n02096294_2118.jpg
# 2. https://images.dog.ceo/breeds/terrier-westhighland/n02098286_5080.jpg
# 3. https://images.dog.ceo/breeds/eskimo/n02109961_4670.jpg
# 4. https://images.dog.ceo/breeds/pitbull/dog-5437227_640.jpg
# 5. https://images.dog.ceo/breeds/african/n02116738_233.jpg
# 6. https://images.dog.ceo/breeds/terrier-kerryblue/n02093859_3140.jpg
# 7. https://images.dog.ceo/breeds/malinois/n02105162_6492.jpg
# 8. https://images.dog.ceo/breeds/hound-plott/hhh-23456.jpg
# 9. https://images.dog.ceo/breeds/spaniel-sussex/n02102480_276.jpg
# 10. https://images.dog.ceo/breeds/pariah-indian/The_Indian_Pariah_Dog.jpg
# 1. https://images.dog.ceo/breeds/pinscher-miniature/n02107312_4929.jpg
# 2. https://images.dog.ceo/breeds/clumber/n02101556_7987.jpg
# 3. https://images.dog.ceo/breeds/dingo/n02115641_12981.jpg
# 4. https://images.dog.ceo/breeds/mastiff-tibetan/n02108551_4421.jpg
# 5. https://images.dog.ceo/breeds/australian-kelpie/IMG_7387.jpg
# 6. https://images.dog.ceo/breeds/komondor/n02105505_4070.jpg
# 7. https://images.dog.ceo/breeds/borzoi/n02090622_8338.jpg
# 8. https://images.dog.ceo/breeds/groenendael/n02105056_5668.jpg
# 9. https://images.dog.ceo/breeds/rajapalayam-indian/Rajapalayam-dog.jpg
# 10. https://images.dog.ceo/breeds/terrier-welsh/lucy.jpg
