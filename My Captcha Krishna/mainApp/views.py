from django.shortcuts import render
from captcha.image import ImageCaptcha
import random

def home(request):
    img = ImageCaptcha(width = 280, height = 90)
    mynum = str(random.randrange(111111,999999))
    Cap_data = img.generate(mynum)
    img.write(mynum, 'Sample_Cap_1.png')
    if request.method == "POST":
        userinput = str(request.POST.get("user_inputinput"))
        if(mynum == userinput):
            res = "Captacha match successfully"
        else:
            res = "Captcha don't match successfully"
        print(mynum, userinput)
        print(res)
        return render(request,"index.html",{"res": res})
    
    print(mynum)
    return render(request,"index.html")