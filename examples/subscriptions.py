from outsetapy import OutsetaApiClient
import asyncio
import os
import dotenv

if os.path.exists(".env"):
    dotenv.load_dotenv(".env")

outseta = OutsetaApiClient(
    subdomain=os.getenv("OUTSETA_SUBDOMAIN"),
    apiKey=os.getenv("OUTSETA_API_KEY"),
    secretKey=os.getenv("OUTSETA_SECRET_KEY"),
)


async def main():
    all_users = await outseta.crm.accounts.get_all()
    for user in all_users:
        print(user.Name, user.Uid)
        cur_sub = user.CurrentSubscription
        subscription = await outseta.billing.subscriptions.get(cur_sub["Uid"])
        print(subscription.Uid)
        print("Plan:", subscription.Plan)
    quit()
    all_plans = await outseta.billing.plans
    for plan in all_plans:
        print("Uid", plan.Uid)
        print("Name", plan.Name)
        print("Description", plan.Description)
        print("IsActive", plan.IsActive)

        print("Trial Period Days", plan.TrialPeriodDays)

        print("Setup Fee", plan.SetupFee)
        print("Monthly Rate", plan.MonthlyRate)

        # print('Is Quantity Editable', plan.IsQuantityEditable)
        print("Unit of Measure", plan.UnitOfMeasure)

        # print('Created', plan.Created)
        # print('Updated', plan.Updated)
        # print('Number of Subscriptions', plan.NumberOfSubscriptions)
        # print('Plan Family', plan.PlanFamily)

    # all_subscriptions = await outseta.billing.subscriptions.get_all()
    # for subscription in all_subscriptions:  # ! this is an error that will be fixed in the next commit
    #     print(subscription.Uid)


asyncio.run(main())
