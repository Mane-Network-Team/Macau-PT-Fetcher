import os,sys,datetime
import shutil
print("    __  ___                                ")
print("   /  |/  /___ _____  ___  ________  _____ ")
print("  / /|_/ / __ `/ __ \/ _ \/ ___/ _ \/ ___/ ")
print(" / /  / / /_/ / / / /  __(__  )  __/ /__   ")
print("/_/  /_/\__,_/_/ /_/\___/____/\___/\___/   ")
print("                       https://manesec.com ")

# if file exits
if (os.path.exists('mane.md')):
    os.remove('mane.md')
if (os.path.exists('output.pdf')):
    os.remove('output.pdf')


files = open('mane.md','a+')
with open('data/header.md','r') as header1:
    for header1_line in header1:
        files.writelines(header1_line)
    header1.close()
    
files.writelines('Fetch Time :' + str(datetime.datetime.now()) + '  (已经筛选近30天的信息)\r\n')

with open('data/header2.md','r') as header2:
    for header2_line in header2:
        files.writelines(header2_line)
    header2.close()
files.close()

# PT Module
if True :
    import module.facebook_mptjs as facebook_mptjs
    facebook_mptjs.run(True)
    facebook_mptjs.run_vister(False)

if True:
    import module.cenjobs as cenjobs
    cenjobs.Run(True)

if True:
    import module.fastfindjob as fastfindjob
    fastfindjob.Run(True)

if True:
    import module.hellojob as hellojob
    hellojob.Run(False)

if True:
    import module.macauhr as macauhr
    macauhr.Run()

if True:
    import module.suncareer as suncareer
    suncareer.Run(True)

if True:
    import module.um as um
    um.run(True)

if True:
    import module.mustedu as mustedu
    mustedu.Run(True)

# Output html
if os.path.exists('out'):
    shutil.rmtree('out')
os.system("generate-md --layout github --input mane.md --output out")

# Patch html
import patch_html as patch
patch.run_path()

# google to pdf
os.system("google-chrome --headless --print-to-pdf=output.pdf --no-margins --print-to-pdf-no-header out/mane_patch.html")
