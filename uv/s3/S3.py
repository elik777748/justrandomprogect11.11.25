# import requests

# url = "https://1xg7ah.leapcellobj.com/mybucket-7yvx-zzqh-omz36vxy/Знімок екрана 2025-12-12 211107.jpg"
# response = requests.get(url=url)
# # print(response.content)
# # with open("uv/s3/202025-12-12%20211107.jpg", mode="bw") as file:
# #     file.write(response.content)
# # дозапис у текстовий файл
# with open("uv/s3/202025-12-12%20211107.jpg", "ab") as file:
#     file.write(b"iuhnjbkhjgvfytuyhiujklm nhbjgftyyuhijoklmnjhyguhi....")

# # читання текстового файлу
# with open("uv/s3/202025-12-12%20211107.jpg", "rb") as file:
#     print(file.read())


import boto3

BUCKET_NAME = "group11112025"

s3 = boto3.client(
    service_name="s3",
    region_name="EEUR",
    endpoint_url="https://8721af4803f2c3c631a90d8b64d397b7.r2.cloudflarestorage.com",
    aws_access_key_id="2ae25d402a48e45a66e8400661cb1e8f",
    aws_secret_access_key="32d65a0b27b9fb3789484262804a790c877a1257d96831a197f2cb182b616bdd"
)

target_filename = "images/Yelisey.jpg"
s3.upload_file("uv/s3/Yelisey.jpg", BUCKET_NAME, target_filename)