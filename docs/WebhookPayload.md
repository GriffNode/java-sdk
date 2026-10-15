

# WebhookPayload

Payment-event payload. AMOUNTS ARE STRINGS (e.g. \"100.00\", \"0.00109462\") to preserve decimal precision — parse before arithmetic. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**event** | [**EventEnum**](#EventEnum) |  |  |
|**timestamp** | **OffsetDateTime** |  |  |
|**transactionId** | **String** |  |  |
|**status** | **TransactionStatus** |  |  |
|**exception** | **TransactionException** |  |  [optional] |
|**currencyCrypto** | **CryptoSymbol** |  |  [optional] |
|**currencyFiat** | **FiatCurrency** |  |  [optional] |
|**amountFiat** | **String** | Decimal string. |  [optional] |
|**amountUsd** | **String** | Decimal string. |  [optional] |
|**amountCrypto** | **String** | Decimal string. |  [optional] |
|**orderId** | **String** |  |  [optional] |
|**receiptUrl** | **URI** | Present on completed/overpaid. |  [optional] |
|**metadata** | **Map&lt;String, String&gt;** | Free-form key/value (≤20 keys, string values ≤500 chars, ≤4 KB total). |  [optional] |



## Enum: EventEnum

| Name | Value |
|---- | -----|
| CREATED | &quot;payment.created&quot; |
| PENDING | &quot;payment.pending&quot; |
| COMPLETED | &quot;payment.completed&quot; |
| OVERPAID | &quot;payment.overpaid&quot; |
| PARTIAL | &quot;payment.partial&quot; |
| EXPIRED | &quot;payment.expired&quot; |
| FAILED | &quot;payment.failed&quot; |
| PAID_LATE | &quot;payment.paid_late&quot; |
| NEEDS_REVIEW | &quot;payment.needs_review&quot; |



