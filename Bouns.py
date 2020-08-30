import requests,sys,time
from colorama import Fore, Back, Style 



    
class Checker():
    def __init__(self):
        try:
            em_file = sys.argv[1]
        except IndexError:


            print(Fore.RED + '███╗   ███╗██████╗     ██████╗ ██╗      █████╗  ██████╗██╗  ██╗')
            print(Fore.RED + '████╗ ████║██╔══██╗    ██╔══██╗██║     ██╔══██╗██╔════╝██║ ██╔╝')
            print(Fore.RED + '██╔████╔██║██████╔╝    ██████╔╝██║     ███████║██║     █████╔╝ ')
            print(Fore.RED + '██║╚██╔╝██║██╔══██╗    ██╔══██╗██║     ██╔══██║██║     ██╔═██╗ ')
            print(Fore.RED + '██║ ╚═╝ ██║██║  ██║    ██████╔╝███████╗██║  ██║╚██████╗██║  ██╗')
            print(Fore.RED + '╚═╝     ╚═╝╚═╝  ╚═╝    ╚═════╝ ╚══════╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝')

             
            print(Fore.BLUE + 'Mahmoud Mohamed') 
            print(Fore.BLACK + '==================')
            print(Fore.BLUE + 'fb.me/mr.black.eg0')
            print(Fore.BLACK + '==================')
            print(Fore.BLUE + 'Bouns Checker')
            print(Fore.BLACK + '==================')
            em_file = input(Fore.RED + '[!]Give me File Path[!] : ')
        self.emails = [x for x in open(em_file).read().splitlines() if x]
        self.gate1()

    def gate1(self):
        for email in self.emails:
            em = email
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'Accept-Language': 'en-GB,en;q=0.5',
                'Referer': 'https://verifyemailaddress.com/result',
                'Content-Type': 'application/x-www-form-urlencoded',
                'Origin': 'https://verifyemailaddress.com',
                'Connection': 'keep-alive',
                'Upgrade-Insecure-Requests': '1',
                'Sec-Fetch-Dest': 'document',
                'Sec-Fetch-Mode': 'navigate',
                'Sec-Fetch-Site': 'same-origin',
                'Sec-Fetch-User': '?1',
            }

            data = {
              'email': email,
              'x': '115',
              'y': '14'
            }

            r = requests.post('https://verifyemailaddress.com/result', headers=headers, data=data)
            #print(swatch_width)

            if 'is valid' in r.text:
                print(Fore.GREEN + "[+]Valid[+] => {}".format(email))
                time.sleep(1)
                f=open("Valid.txt","a")
                f.write("[+]Valid[+] => {}\n".format(email))
                f.close
            elif 'is not valid' in r.text:
                print(Fore.RED + "[-]Not Valid[-] => {}".format(email))
            elif 'Connecting to' in r.text:
                print(Fore.RED + "[-]DIED[-] => {}".format(email))
            elif 'No MX resource records found' in r.text:
                print(Fore.RED + "[-]Invaild Doamin[-] => {}".format(email))
            else:
                print(Fore.YELLOW +"[!]unknown Error[!] => {}".format(email))
                
                    




if __name__ == '__main__':
    Checker()
input("[!]Done and save resule in [Valid.txt] Press Enter To exit..[!]")

