from enum import Enum

class ActivityType(Enum):
  Custom = 10
  Note = 50
  Email = 51
  PhoneCall = 52
  Meeting = 53
  AccountCreated = 100
  AccountUpdated = 101
  AccountAddPerson = 102
  AccountStageUpdated = 103
  AccountDeleted = 104
  AccountBillingInformationUpdated = 105
  PersonCreated = 200
  PersonUpdated = 201
  PersonDeleted = 202
  PersonLogin = 203
  PersonListSubscribed = 204
  PersonListUnsubscribed = 205
  PersonSegmentAdded = 206
  PersonSegmentRemoved = 207
  PersonEmailOpened = 208
  PersonEmailClicked = 209
  PersonEmailBounce = 210
  PersonEmailSpan = 211
  PersonSupportTicketCreated = 212
  PersonSupportTicketUpdated = 213
  DealCreated = 300
  DealUpdated = 301
  DealAddPerson = 302
  DealAddAccount = 303
