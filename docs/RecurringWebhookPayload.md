

# RecurringWebhookPayload

Recurring payment request event. schedule_id + your own reference identify the customer/order. The period's payment also fires the normal payment.* events. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** |  |  |
|**event** | [**EventEnum**](#EventEnum) |  |  |
|**timestamp** | **OffsetDateTime** |  |  |
|**scheduleId** | **UUID** |  |  |
|**reference** | **String** | Your own customer/order id, as entered on the schedule. |  [optional] |
|**customerEmail** | **String** |  |  [optional] |
|**description** | **String** |  |  [optional] |
|**amountFiat** | **String** | Decimal string. |  [optional] |
|**currencyFiat** | [**CurrencyFiatEnum**](#CurrencyFiatEnum) |  |  [optional] |
|**interval** | [**IntervalEnum**](#IntervalEnum) |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) |  |  |
|**periodNo** | **Integer** | recurring.payment.* only. |  [optional] |
|**transactionId** | **String** | recurring.payment.completed only. |  [optional] |
|**reason** | [**ReasonEnum**](#ReasonEnum) | recurring.stopped only. |  [optional] |



## Enum: EventEnum

| Name | Value |
|---- | -----|
| CONFIRMED | &quot;recurring.confirmed&quot; |
| PAYMENT_COMPLETED | &quot;recurring.payment.completed&quot; |
| PAYMENT_UNPAID | &quot;recurring.payment.unpaid&quot; |
| STOPPED | &quot;recurring.stopped&quot; |



## Enum: CurrencyFiatEnum

| Name | Value |
|---- | -----|
| USD | &quot;USD&quot; |
| PLN | &quot;PLN&quot; |
| EUR | &quot;EUR&quot; |
| GBP | &quot;GBP&quot; |



## Enum: IntervalEnum

| Name | Value |
|---- | -----|
| WEEKLY | &quot;weekly&quot; |
| MONTHLY | &quot;monthly&quot; |
| QUARTERLY | &quot;quarterly&quot; |
| YEARLY | &quot;yearly&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| PENDING_CONFIRMATION | &quot;pending_confirmation&quot; |
| ACTIVE | &quot;active&quot; |
| PAUSED | &quot;paused&quot; |
| CANCELLED | &quot;cancelled&quot; |
| STOPPED_BY_CUSTOMER | &quot;stopped_by_customer&quot; |
| BOUNCED | &quot;bounced&quot; |
| EXPIRED_UNCONFIRMED | &quot;expired_unconfirmed&quot; |



## Enum: ReasonEnum

| Name | Value |
|---- | -----|
| STOPPED_BY_CUSTOMER | &quot;stopped_by_customer&quot; |
| BOUNCED | &quot;bounced&quot; |
| UNCONFIRMED | &quot;unconfirmed&quot; |



