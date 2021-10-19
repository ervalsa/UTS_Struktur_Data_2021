from queue import Queue
import time
import requests

# link Image
# 1. https://images.unsplash.com/photo-1516117172878-fd2c41f4a759
# 2. https://images.unsplash.com/photo-1532009324734-20a7a5813719
# 3. https://images.unsplash.com/photo-1524429656589-6633a470097c
# 4. https://images.unsplash.com/photo-1530224264768-7ff8c1789d79
# 5. https://images.unsplash.com/photo-1564135624576-c5c88640f235

queue = Queue()
time1 = time.perf_counter()

img_endpoint = input("""Masukkan Link Gambar (Pisahkan dengan spasi jika lebih dari satu) >>> """).split()
for x in img_endpoint:
    queue.put(x)


# fungi untuk download image
def download_image(img_url):
    print("Sedang mendownload gambar ...")
    img_bytes = requests.get(img_url).content
    img_name = img_url.split("/")[3]
    img_name = f"{img_name}.jpg"

    with open(img_name, "wb") as img_file:
        img_file.write(img_bytes)
        print(f"{img_name} telah selesai di download ...")


for i in range(1, queue.qsize() + 1):
    print(" ")
    print("|||====================|||")
    img_endpoint = queue.get()

    print(f"Gambar {i} yang sedang di download adalah {img_endpoint}")
    print(f"Dalam antrian download : {queue.qsize()} gambar")

    download_image(img_endpoint)

    time2 = time.perf_counter()
    print(f"Selesai dalam {round(time2 - time1, 2)} detik")

    print(" ")
    print("|||====================|||")

    if queue.empty():
        print("=== Download Selesai ===")