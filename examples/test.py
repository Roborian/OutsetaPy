import asyncio
from outsetapy import OutsetaApiClient

outseta = OutsetaApiClient(
    subdomain="roborian",
    apiKey="25daa814-3889-4134-a026-88a1e4ea721c",
    secretKey="ff39ad05edaea3571e33410d1c5b6ee9",
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
