url="https://canvas.instructure.com/api/v1/courses/803405/folders/root"
params={"access_token": "7~Kh0OqHcSsGIdKIiZHBIxFBv0wwpoZinb1vxicmipU6eG7dlJoRGkzJllTOEEUxCX"}
r=requests.get(url, params=params)
rootInfo=r.json()
while