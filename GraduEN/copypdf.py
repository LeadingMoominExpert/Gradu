#copy final pdf file into a new renamed one
import os
import shutil
cwd = os.getcwd() + "\\"

try:
    shutil.copy2(cwd + "ThesisTammero.pdf", cwd + "Tammero_Tuomas_opinnayte.pdf")
    print("File copied successfully")
except:
    print("Copying pdf file unsuccessful")
