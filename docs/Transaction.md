

# Transaction

The canonical, curated public view of a transaction (same shape from create, get and list). Internal fields (capability tokens, client_ip, address_index, derivation/db internals) are deliberately NOT exposed. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**transactionId** | **String** |  |  |
|**status** | **TransactionStatus** |  |  |
|**exception** | **TransactionException** |  |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) |  |  [optional] |
|**crypto** | **CryptoSymbol** |  |  |
|**depositAddress** | **String** |  |  [optional] |
|**amountCrypto** | **BigDecimal** |  |  [optional] |
|**amountFiat** | **BigDecimal** |  |  |
|**amountUsd** | **BigDecimal** |  |  |
|**amountPaid** | **BigDecimal** |  |  [optional] |
|**amountRemaining** | **BigDecimal** |  |  [optional] |
|**currencyFiat** | **FiatCurrency** |  |  |
|**fiatToUsdRate** | **BigDecimal** |  |  [optional] |
|**exchangeRate** | **BigDecimal** | USD per unit of crypto, locked at creation. |  [optional] |
|**confirmationsRequired** | **Integer** |  |  [optional] |
|**paymentUrl** | **URI** |  |  [optional] |
|**orderId** | **String** |  |  [optional] |
|**customerEmail** | **String** |  |  [optional] |
|**items** | [**List&lt;LineItem&gt;**](LineItem.md) |  |  [optional] |
|**payments** | [**List&lt;PaymentSplit&gt;**](PaymentSplit.md) | On-chain payments detected toward this transaction. |  [optional] |
|**metadata** | **Map&lt;String, String&gt;** | Free-form key/value (≤20 keys, string values ≤500 chars, ≤4 KB total). |  [optional] |
|**successUrl** | **String** |  |  [optional] |
|**cancelUrl** | **String** |  |  [optional] |
|**createdAt** | **OffsetDateTime** |  |  |
|**updatedAt** | **OffsetDateTime** |  |  [optional] |
|**expiresAt** | **OffsetDateTime** |  |  |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| BASIC | &quot;basic&quot; |
| DETAILED | &quot;detailed&quot; |



