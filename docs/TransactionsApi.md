# TransactionsApi

All URIs are relative to *https://api.griffnode.com/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createDetailedTransaction**](TransactionsApi.md#createDetailedTransaction) | **POST** /transactions/create-detailed | Create an itemized transaction (Professional/Enterprise plans) |
| [**createTransaction**](TransactionsApi.md#createTransaction) | **POST** /transactions/create | Create a payment transaction |
| [**getTransaction**](TransactionsApi.md#getTransaction) | **GET** /transactions/{transaction_id} | Retrieve a single transaction |
| [**listTransactions**](TransactionsApi.md#listTransactions) | **GET** /transactions/list | List the merchant&#39;s transactions (newest first) |


<a id="createDetailedTransaction"></a>
# **createDetailedTransaction**
> TransactionEnvelope createDetailedTransaction(createDetailedTransactionRequest, xIdempotencyKey)

Create an itemized transaction (Professional/Enterprise plans)

### Example
```java
// Import classes:
import com.griffnode.sdk.ApiClient;
import com.griffnode.sdk.ApiException;
import com.griffnode.sdk.Configuration;
import com.griffnode.sdk.auth.*;
import com.griffnode.sdk.models.*;
import com.griffnode.sdk.api.TransactionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.griffnode.com/v1");
    
    // Configure HTTP bearer authorization: SecretKey
    HttpBearerAuth SecretKey = (HttpBearerAuth) defaultClient.getAuthentication("SecretKey");
    SecretKey.setBearerToken("BEARER TOKEN");

    TransactionsApi apiInstance = new TransactionsApi(defaultClient);
    CreateDetailedTransactionRequest createDetailedTransactionRequest = new CreateDetailedTransactionRequest(); // CreateDetailedTransactionRequest | 
    String xIdempotencyKey = "xIdempotencyKey_example"; // String | Optional unique key for a create request (e.g. a UUID). A retried create with the same key returns the original transaction instead of creating a duplicate — send it on every create so a network retry can't double-charge the customer. 
    try {
      TransactionEnvelope result = apiInstance.createDetailedTransaction(createDetailedTransactionRequest, xIdempotencyKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransactionsApi#createDetailedTransaction");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **createDetailedTransactionRequest** | [**CreateDetailedTransactionRequest**](CreateDetailedTransactionRequest.md)|  | |
| **xIdempotencyKey** | **String**| Optional unique key for a create request (e.g. a UUID). A retried create with the same key returns the original transaction instead of creating a duplicate — send it on every create so a network retry can&#39;t double-charge the customer.  | [optional] |

### Return type

[**TransactionEnvelope**](TransactionEnvelope.md)

### Authorization

[SecretKey](../README.md#SecretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Transaction created. |  -  |
| **400** | Validation error (INVALID_REQUEST, INVALID_CRYPTO, INVALID_AMOUNT, AMOUNT_TOO_LOW, INVALID_CURRENCY, INVALID_METADATA, WALLET_NOT_CONFIGURED, MISSING_ITEMS, MISSING_ORDER_ID, …). |  -  |
| **401** | Missing or invalid API key (UNAUTHORIZED). |  -  |
| **402** | Merchant platform balance too low for overage fees (INSUFFICIENT_BALANCE). |  -  |
| **403** | Key lacks permission — e.g. a publishable key on a secret-only endpoint, or plan too low (FORBIDDEN, USE_PAY_ENDPOINT, PLAN_UPGRADE_REQUIRED, NO_ACTIVE_PLAN). |  -  |
| **429** | Rate limit or quota exceeded. &#x60;error&#x60; is &#x60;RATE_LIMIT_EXCEEDED&#x60; (per-minute request rate — honour &#x60;Retry-After&#x60;) or &#x60;MONTHLY_LIMIT_REACHED&#x60; (the plan&#39;s monthly transaction quota). Rate-limit headers accompany the &#x60;RATE_LIMIT_EXCEEDED&#x60; case.  |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  * Retry-After -  <br>  |

<a id="createTransaction"></a>
# **createTransaction**
> TransactionEnvelope createTransaction(createTransactionRequest, xIdempotencyKey)

Create a payment transaction

### Example
```java
// Import classes:
import com.griffnode.sdk.ApiClient;
import com.griffnode.sdk.ApiException;
import com.griffnode.sdk.Configuration;
import com.griffnode.sdk.auth.*;
import com.griffnode.sdk.models.*;
import com.griffnode.sdk.api.TransactionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.griffnode.com/v1");
    
    // Configure HTTP bearer authorization: SecretKey
    HttpBearerAuth SecretKey = (HttpBearerAuth) defaultClient.getAuthentication("SecretKey");
    SecretKey.setBearerToken("BEARER TOKEN");

    TransactionsApi apiInstance = new TransactionsApi(defaultClient);
    CreateTransactionRequest createTransactionRequest = new CreateTransactionRequest(); // CreateTransactionRequest | 
    String xIdempotencyKey = "xIdempotencyKey_example"; // String | Optional unique key for a create request (e.g. a UUID). A retried create with the same key returns the original transaction instead of creating a duplicate — send it on every create so a network retry can't double-charge the customer. 
    try {
      TransactionEnvelope result = apiInstance.createTransaction(createTransactionRequest, xIdempotencyKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransactionsApi#createTransaction");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **createTransactionRequest** | [**CreateTransactionRequest**](CreateTransactionRequest.md)|  | |
| **xIdempotencyKey** | **String**| Optional unique key for a create request (e.g. a UUID). A retried create with the same key returns the original transaction instead of creating a duplicate — send it on every create so a network retry can&#39;t double-charge the customer.  | [optional] |

### Return type

[**TransactionEnvelope**](TransactionEnvelope.md)

### Authorization

[SecretKey](../README.md#SecretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Transaction created. |  -  |
| **400** | Validation error (INVALID_REQUEST, INVALID_CRYPTO, INVALID_AMOUNT, AMOUNT_TOO_LOW, INVALID_CURRENCY, INVALID_METADATA, WALLET_NOT_CONFIGURED, MISSING_ITEMS, MISSING_ORDER_ID, …). |  -  |
| **401** | Missing or invalid API key (UNAUTHORIZED). |  -  |
| **402** | Merchant platform balance too low for overage fees (INSUFFICIENT_BALANCE). |  -  |
| **403** | Key lacks permission — e.g. a publishable key on a secret-only endpoint, or plan too low (FORBIDDEN, USE_PAY_ENDPOINT, PLAN_UPGRADE_REQUIRED, NO_ACTIVE_PLAN). |  -  |
| **409** | This client IP already has an active transaction (ACTIVE_TRANSACTION_EXISTS). Body includes an &#x60;existing_transaction&#x60; object. |  -  |
| **429** | Rate limit or quota exceeded. &#x60;error&#x60; is &#x60;RATE_LIMIT_EXCEEDED&#x60; (per-minute request rate — honour &#x60;Retry-After&#x60;) or &#x60;MONTHLY_LIMIT_REACHED&#x60; (the plan&#39;s monthly transaction quota). Rate-limit headers accompany the &#x60;RATE_LIMIT_EXCEEDED&#x60; case.  |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  * Retry-After -  <br>  |

<a id="getTransaction"></a>
# **getTransaction**
> TransactionEnvelope getTransaction(transactionId)

Retrieve a single transaction

### Example
```java
// Import classes:
import com.griffnode.sdk.ApiClient;
import com.griffnode.sdk.ApiException;
import com.griffnode.sdk.Configuration;
import com.griffnode.sdk.auth.*;
import com.griffnode.sdk.models.*;
import com.griffnode.sdk.api.TransactionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.griffnode.com/v1");
    
    // Configure HTTP bearer authorization: SecretKey
    HttpBearerAuth SecretKey = (HttpBearerAuth) defaultClient.getAuthentication("SecretKey");
    SecretKey.setBearerToken("BEARER TOKEN");

    TransactionsApi apiInstance = new TransactionsApi(defaultClient);
    String transactionId = "transactionId_example"; // String | 
    try {
      TransactionEnvelope result = apiInstance.getTransaction(transactionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransactionsApi#getTransaction");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **transactionId** | **String**|  | |

### Return type

[**TransactionEnvelope**](TransactionEnvelope.md)

### Authorization

[SecretKey](../README.md#SecretKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The transaction. |  -  |
| **401** | Missing or invalid API key (UNAUTHORIZED). |  -  |
| **403** | Key lacks permission — e.g. a publishable key on a secret-only endpoint, or plan too low (FORBIDDEN, USE_PAY_ENDPOINT, PLAN_UPGRADE_REQUIRED, NO_ACTIVE_PLAN). |  -  |
| **404** | Resource not found (TRANSACTION_NOT_FOUND). |  -  |

<a id="listTransactions"></a>
# **listTransactions**
> ListTransactions200Response listTransactions(limit, offset, status, crypto)

List the merchant&#39;s transactions (newest first)

### Example
```java
// Import classes:
import com.griffnode.sdk.ApiClient;
import com.griffnode.sdk.ApiException;
import com.griffnode.sdk.Configuration;
import com.griffnode.sdk.auth.*;
import com.griffnode.sdk.models.*;
import com.griffnode.sdk.api.TransactionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.griffnode.com/v1");
    
    // Configure HTTP bearer authorization: SecretKey
    HttpBearerAuth SecretKey = (HttpBearerAuth) defaultClient.getAuthentication("SecretKey");
    SecretKey.setBearerToken("BEARER TOKEN");

    TransactionsApi apiInstance = new TransactionsApi(defaultClient);
    Integer limit = 20; // Integer | 
    Integer offset = 0; // Integer | 
    TransactionStatus status = TransactionStatus.fromValue("pending"); // TransactionStatus | 
    CryptoSymbol crypto = CryptoSymbol.fromValue("BTC"); // CryptoSymbol | 
    try {
      ListTransactions200Response result = apiInstance.listTransactions(limit, offset, status, crypto);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransactionsApi#listTransactions");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **limit** | **Integer**|  | [optional] [default to 20] |
| **offset** | **Integer**|  | [optional] [default to 0] |
| **status** | [**TransactionStatus**](.md)|  | [optional] [enum: pending, awaiting_confirmation, completed, partial, expired, failed] |
| **crypto** | [**CryptoSymbol**](.md)|  | [optional] [enum: BTC, LTC, DOGE, DASH, ETH, USDT, USDC, EURC, DAI, WBTC, SHIB, PEPE, LINK, UNI, AAVE, MKR] |

### Return type

[**ListTransactions200Response**](ListTransactions200Response.md)

### Authorization

[SecretKey](../README.md#SecretKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A page of transactions. |  -  |
| **401** | Missing or invalid API key (UNAUTHORIZED). |  -  |
| **403** | Key lacks permission — e.g. a publishable key on a secret-only endpoint, or plan too low (FORBIDDEN, USE_PAY_ENDPOINT, PLAN_UPGRADE_REQUIRED, NO_ACTIVE_PLAN). |  -  |

