import shutil

stockage = shutil.disk_usage("/")

print(f"{stockage[0]/ 1000000000}, {stockage [1]/ 1000000000}, {stockage [2]/ 1000000000}")
