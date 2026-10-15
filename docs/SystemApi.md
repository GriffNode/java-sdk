# SystemApi

All URIs are relative to *https://api.griffnode.com/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getHealth**](SystemApi.md#getHealth) | **GET** /health | API health check |
| [**hostedCheckoutRedirect**](SystemApi.md#hostedCheckoutRedirect) | **GET** /pay | Hosted-checkout redirect (browser flow, publishable key) |


<a id="getHealth"></a>
# **getHealth**
> GetHealth200Response getHealth()

API health check

### Example
```java
// Import classes:
import com.griffnode.sdk.ApiClient;
import com.griffnode.sdk.ApiException;
import com.griffnode.sdk.Configuration;
import com.griffnode.sdk.models.*;
import com.griffnode.sdk.api.SystemApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.griffnode.com/v1");

    SystemApi apiInstance = new SystemApi(defaultClient);
    try {
      GetHealth200Response result = apiInstance.getHealth();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SystemApi#getHealth");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetHealth200Response**](GetHealth200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Service status (intentionally NOT wrapped in the success envelope). |  -  |

<a id="hostedCheckoutRedirect"></a>
# **hostedCheckoutRedirect**
> hostedCheckoutRedirect(pk, amount, crypto, currency, link)

Hosted-checkout redirect (browser flow, publishable key)

Browser-facing redirect to the hosted payment page, authenticated by a **publishable** key in the query string (safe to expose client-side). Not used by the server-side SDKs — included for completeness. 

### Example
```java
// Import classes:
import com.griffnode.sdk.ApiClient;
import com.griffnode.sdk.ApiException;
import com.griffnode.sdk.Configuration;
import com.griffnode.sdk.models.*;
import com.griffnode.sdk.api.SystemApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.griffnode.com/v1");

    SystemApi apiInstance = new SystemApi(defaultClient);
    String pk = "pk_example"; // String | Publishable key, pk_live_… / pk_test_…
    String amount = "amount_example"; // String | Fiat amount (≥ 1.00 USD equivalent).
    CryptoSymbol crypto = CryptoSymbol.fromValue("BTC"); // CryptoSymbol | 
    String currency = "USD"; // String | Fiat currency of `amount`. Ignored when `link` is set: a payment link always uses its own amount and currency.
    String link = "link_example"; // String | Payment-link slug. The link's own amount, currency, expiry and single-use rules apply (410 if expired, 409 if a single-use link was already paid).
    try {
      apiInstance.hostedCheckoutRedirect(pk, amount, crypto, currency, link);
    } catch (ApiException e) {
      System.err.println("Exception when calling SystemApi#hostedCheckoutRedirect");
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
| **pk** | **String**| Publishable key, pk_live_… / pk_test_… | |
| **amount** | **String**| Fiat amount (≥ 1.00 USD equivalent). | |
| **crypto** | [**CryptoSymbol**](.md)|  | [enum: BTC, LTC, DOGE, DASH, ETH, USDT, USDC, DAI, WBTC, SHIB, PEPE, LINK, UNI, AAVE, MKR] |
| **currency** | **String**| Fiat currency of &#x60;amount&#x60;. Ignored when &#x60;link&#x60; is set: a payment link always uses its own amount and currency. | [optional] [default to USD] [enum: USD, PLN, EUR, GBP] |
| **link** | **String**| Payment-link slug. The link&#39;s own amount, currency, expiry and single-use rules apply (410 if expired, 409 if a single-use link was already paid). | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **302** | Redirect to https://griffnode.com/transaction/{transaction_id} |  -  |
| **400** | Validation error (INVALID_REQUEST, INVALID_CRYPTO, INVALID_AMOUNT, AMOUNT_TOO_LOW, INVALID_CURRENCY, INVALID_METADATA, WALLET_NOT_CONFIGURED, MISSING_ITEMS, MISSING_ORDER_ID, …). |  -  |

