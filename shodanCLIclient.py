#shodanCLIclient
#v0.0.1
from time import sleep
import shodan
from rich.panel import Panel
from rich.align import Align
from rich import print
import rich
from rich import print
from rich.console import Console
console = Console()


logo = """

   _____ __              __            ________    ____     ___            __ 
  / ___// /_  ____  ____/ /___ _____  / ____/ /   /  _/____/ (_)__  ____  / /_
  \\__ \\/ __ \\/ __ \\/ __  / __ `/ __ \\/ /   / /    / // ___/ / / _ \\/ __ \\/ __/
 ___/ / / / / /_/ / /_/ / /_/ / / / / /___/ /____/ // /__/ / /  __/ / / / /_  
/____/_/ /_/\\____/\\__,_/\\__,_/_/ /_/\\____/_____/___/\\___/_/_/\\___/_/ /_/\\__/  

"""
print(Align(Panel.fit(logo, style="#950000", title="ShodanCLIclient", subtitle="by 0x7b"), align='center'))
console.print("PRESS ENTER TO CONTINUE", style="#7313F0", justify="center")
input()
console.print("ENTER YOU API KEY", style="#7313F0", justify="center")
SHODAN_API_KEY = input("{$}->")

api = shodan.Shodan(SHODAN_API_KEY)
console.print("enter a search query".upper(), style="#15D200", justify="center")
query = input()
def search_result():
	try:
	        # Search Shodan
	        results = api.search(query)
	        if results['total'] > 0:

	        	console.print('[+]Results found: {}'.format(results['total']), style="#15D200")
	        else:
	        	console.print('[-]No result found, try changing your search query')
	        migga = input("")
	        for result in results['matches']:
	                print('IP: {}'.format(result['ip_str']))
	                print(result['data'])
	                print('')
	                sleep(0.1)
	except shodan.APIError:
	        print('Error')

while True:
	search_result()
