import asyncio
from outsetapy import OutsetaApiClient
import os

OUTSETA_SUBDOMAIN = os.getenv("OUTSETA_SUBDOMAIN")
OUTSETA_API_KEY = os.getenv("OUTSETA_API_KEY")
OUTSETA_API_SECRET = os.getenv("OUTSETA_API_SECRET")

outseta = OutsetaApiClient(
    subdomain=OUTSETA_SUBDOMAIN,
    apiKey=OUTSETA_API_KEY,
    secretKey=OUTSETA_API_SECRET,
)


async def main():
    print("Accounts:")
    accounts = await outseta.crm.accounts.get_all()
    for account in accounts:
        print(account.Uid)
    print()

    print("Invoices:")
    invoices = await outseta.billing.invoices.get_all()
    for invoice in invoices:
        print(invoice)
    print()

    print("Activities:")
    activities = await outseta.crm.activities.get_all()
    for activity in activities:
        print(activity.Uid)
    print()

    print("Plans:")
    plans = await outseta.billing.plans.get_all()
    for plan in plans:
        print(plan.Uid)
    print()

    # print('Subscriptions:')
    # subscriptions = await outseta.billing.subscriptions.get_all()
    # for subscription in subscriptions:
    # 	print(subscription.Uid)
    # print()

    print("Tickets:")
    tickets = await outseta.support.cases.get_all()
    for ticket in tickets:
        print(ticket)
    print()


asyncio.run(main())
