import asyncio
from outsetapy import OutsetaApiClient

outseta = OutsetaApiClient(subdomain='roborian',apiKey='25daa814-3889-4134-a026-88a1e4ea721c', secretKey='ff39ad05edaea3571e33410d1c5b6ee9')

async def main():
	accounts = await outseta.crm.accounts.get_all()
	for account in accounts:	
		print(account)
	invoices = await outseta.crm.billing.get_all()
	for invoice in invoices:
		print(invoice)
	
asyncio.run(main())

