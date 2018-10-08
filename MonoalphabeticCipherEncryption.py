#Now trying something different. 
#Going to use substitution here. 

#Strings are going to be encrypted via Monoalphabetic Ciphers; replacing letters with others. 
#So the first thing I'm gonna make is a dictionary as the key. 
import random
def key(): 
    key={}
    #so the key is actually going to be a dictionary in which every letter, all the encrypted stuff will be mapped to its appropriate value, the actual letter. 
    a=list('abcdefghijklmnopqrstuvwxyz')
    b=list('abcdefghijklmnopqrstuvwxyz'.upper())
    #first I'm going to randomize the order of the alphabet for both upper and lower cases. 
    
    #lower case 
    l='abcdefghijklmnopqrstuvwxyz'
    for n in range(len(a)): 
        num=random.randint(0,len(l)-1) #generating a random number 
        a[n],a[num]=a[num],a[n] #randomizing the order. 
    #now setting the dictionary keys 
    for element in l: 
        key[a.pop(0)]=element #since a has already been randomized
    
    ###FORMAT OF DICTIONARY -> ENCRYPTED:DECRYPTED 
          
    #upper case 
    #randomizing the letters in string b. 
    for n in range(len(b)): 
        num=random.randint(0,len(l)-1)
        b[n],b[num]=b[num],b[n]
    #now setting the dictionary keys 
    for element in l.upper(): 
        key[b.pop(0)]=element
        
    #still need to add, ints, symbols and spaces!!!! 
    
    #ints - going to use bin() representation of the number 
    for element in range(10): 
        key[bin(element)]=element
    #if a number is 312 per say, I'll have to go through iterate and replace the each number. So 312 would really look like bin(3)+bin(1)+bin(2) 
    
    #SYMBOLS 
    sym='~`!@#$%^&*()-_=+[]{}|\';:"<>?/.,' #a string of all the symbols. 
    sym_lis=list(sym) 
    for n in range(len(sym)): 
        num=random.randint(0,len(sym)-1) 
        sym_lis[n], sym_lis[num] = sym_lis[num], sym_lis[n] #randomizing all the symbols 
    #now modifying the dictionary for the symbols. 
    for n in range(len(sym)): 
        key[sym_lis[n]]=sym[n]
    
    #SPACES - just going to replace the spaces with '/'; but because of symbols '/' is already taken. So instead 
    key['F_Spc']=' '
    
    
    return (key) #Rembmer the format: encrypted letter : actual letter 
#Now the dictionary is done.
key=key() 
print(key) #debugging 
def encrypt(a): #will return a list. 
    #a is going to be a string of basically anything. 
    #here we're going to encrypt the data using the dictionary we created via key().
    x=[]
    for element in a: 
        #iterating through the string. 
        for letter in key: 
            #searching through teh dictionary for that particular value. 
            #print(key[letter],element,key[letter]==element, type(key[letter]), type(element)) #debugging
            if(str(key[letter])==element): 
                #print('enter') #debugging
                x.append(letter)
    return(x)
#Now time to decrypt, assuming a in the argument is already encrypted with dictionary key. 
def decrypt(a): 
    #REMEMBER: FORMAT OF DICTIONARY IS ENCRYPTED:DECRYPTED 
    #an error that you might have to look out for is the '/n'. that is not a key within here so... those will just have to be added normally. 
    b='' 
    gibberish=''
    #for a, I need to delete the gibberish in the for loop. 
    #all right a is gonna be a list of every line in a fucking file.

    for element in a: 
        element=element.strip()
        #taking care of the int case 
        i=[(n,bin(n)) for n in range(0,10)]
        for j in i: 
            if j[1] == element:
                #print(key[str(j[1])]) #debugging
                b=b+str(key[str(j[1])])
                break
        #taking care of everythign else 
        p='abcdefghijklmnopqrstuvwxyz'+'abcdefghijklmnopqrstuvwxyz'.upper()+'~`!@#$%^&*()-_=+[]{}|\';:"<>?/.,'+'F_Spc'
        if(element in p): 
            b=b+key[element]
            
    return(b)

#asks user to set a password for his file. 
def setPassword(): 
    p=input("Please enter password of your choosing: ") 
    return p 
#to add random text to make the encrypted file more confusing to the average user. 
def gibberish(): 
    #generating random string
    length=random.randint(1,100)
    a='asdfghjklqwertyuiopzxcvbnm'+'qwertyuiopasdfghjklzxcvbnm'.upper()+"!@#$%^&*()-_=+][{}\|;:',.></?"
    startTag,endTag='>%^&*<','<%^&*>'
    randstr=''
    for n in range(length+1): 
        for m in range(random.randint(1,60)): 
            randstr=randstr+a[random.randint(0,len(a)-1)]
        randstr=randstr+"\n"
    return startTag+'\n'+randstr+"\n"+endTag

    
###########################################################################################################################################################

#Now time for the main function. 
#Takes in a file (in this case, a). 
#First it sets a password for said file. 
#Then checks to see if password entered == password stored 
#If it they do match, then the file is pulled  up normally. 
#If they don't the file is then overwritten using encryption. 
#If they enter the password again, then the file is written over again, decrypted. 
def main(a): 
    p_stored=setPassword() 
    #Ask user to enter password 
    p_entered=input("Please enter password for file: ") 
    #check to see if passwords match
    #if they do, do nothing... the file should remain as is. 
    
    #if they don't, encrypt it. 
    if(p_stored!=p_entered): 
        #iterating through the file and going to encrypt every line and then open the file again and write it line by line. 
        file=open(a,'r') 
        f=file.readlines() 
        file.close() 
        
        #now iterate through each line and encrypt it; here's another issue, encrypt gives me a list. so. 
        content=[]
        for line in f: 
            content.append(encrypt(line)) 
        #For every line in content, each element will be a list, in this each element will be a line in the file and that list, each of those elements are each characters encrypted. 
        #write to file. 
        file=open(a,'w') 
        for line in content: 
            for char in line: 
                file.write(char)
            file.write("\n")
            #file.write(gibberish())
        file.close() 
        #At this point, the main idea is actually completed! 
        
        #Now for some imporvements. To imporve the encryption, we could, add like just a bunch of gibberish for like every three lines or something. 
        #Just use a random string generator and add start and end tags so I know when the gibberish starts and when the gibberish ends. 
        ###FOR THE GIBBERISH, USE .replace() !!!!!
        #Asking about the password again.. gives us a chance to test decryption! 
        pas=input("Please enter a password for the second time: ") 
        if(pas==p_stored): 
            #decryption! 
            print('content: ' + str(content))
            f=open('result.txt','w')
            for element in content: 
                f.write(decrypt(element)+'\n') 
            f.close()
            print("Open up result.txt to see your file!")
            
        #if its not equal just leave them with the encrypted file. 
        
        #After that, I was thinking about using a database in case you wanted an entire directory of files, like entire folders or use your domain and upload it to 
        #a website. 
        #I feel like a database would be easier to work with, because I think you can use them directly via python. 