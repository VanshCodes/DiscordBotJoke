import requests,random
import json,pyjokes


def jokes(f=r"https://official-joke-api.appspot.com/random_ten"):
    
    data = requests.get(f)
    tt = json.loads(data.text)
    return tt

def get():
    a = jokes()
##
##    print(a)
##    print(type(a))
    for i in (a):
        types = i["type"]
        setup = i["setup"]
        punchline = i["punchline"]
        # print()/
        # print()
        # print(, "\n")
        return f"{types}\n{setup}\n{punchline}\n" 
        # break
    
def get_random_joke():
    
    a = random.randint(0,2)
    print("Random Value:,",a)
    if a == 0:
        return get()        
	#print("\n")
	
    if a == 1:
        return (pyjokes.get_joke())
    if a == 3:
        return pyjokes.chucknorris()
	#print("\n")
    if a == 2:
        return ("Don't Have Time")
	#print("\n")
	
##f = 
# if __name__ == maiif __name__ == main::

if __name__ == "__main__":    
    print(get_random_joke())
    import time
    def run():
        a = int(input())
        for i in range(a):
            print(get_random_joke())
            time.sleep(2)
    run()
