import os,sys,datetime
print("    __  ___                                ")
print("   /  |/  /___ _____  ___  ________  _____ ")
print("  / /|_/ / __ `/ __ \/ _ \/ ___/ _ \/ ___/ ")
print(" / /  / / /_/ / / / /  __(__  )  __/ /__   ")
print("/_/  /_/\__,_/_/ /_/\___/____/\___/\___/   ")
print("                       https://manesec.com ")

# if file exits
if (os.path.exists('mane.txt')):
    os.remove('mane.txt')

files = open('mane.txt','a+')
files.writelines("    __  ___                               "+'\n') 
files.writelines("   /  |/  /___ _____  ___  ________  _____"+'\n') 
files.writelines("  / /|_/ / __ `/ __ \/ _ \/ ___/ _ \/ ___/"+'\n') 
files.writelines(" / /  / / /_/ / / / /  __(__  )  __/ /__  "+'\n') 
files.writelines("/_/  /_/\__,_/_/ /_/\___/____/\___/\___/  "+'\n') 
files.writelines("                       https://manesec.com"+'\n') 
files.writelines("    Mane Macau PT Fetcher v1.0.1 Alpha    "+'\n')
files.writelines("	                                        "+'\n')
files.writelines("喵: 主要收集兼职信息，安卓可以考虑用第三方APP"+'\n')
files.writelines("喵: 资料从网上通过爬虫收集，未经过验证是否可靠"+'\n')
files.writelines("喵: 请注意信息来源还有发布时间，请三思而后行！"+'\n')
files.writelines("喵: 请勿过度疲劳，另外要谨慎对待交押金和身份证"+'\n')
files.writelines("喵: 签约时合同要仔细阅读，注意看有没有霸王条约"+'\n')
files.writelines("喵: 切记注意安全，切记注意安全，切记注意安全！"+'\n')
files.writelines('\n')
files.writelines('  Fetch Time :' + str(datetime.datetime.now()))
files.writelines('\n')
files.writelines('\n')
files.close()

# facebook mptjs
if True :
    import module.facebook_mptjs as facebook_mptjs
    facebook_mptjs.run(True)
    facebook_mptjs.run_vister(False)

# hellojob
if True:
    import module.hellojob as hellojob
    hellojob.Run(False)

if True:
    import module.macauhr as macauhr
    macauhr.Run()

if True:
    import module.suncareer as suncareer
    suncareer.Run(True)

# um PTJ
if True:
    import module.um as um
    um.run(True)