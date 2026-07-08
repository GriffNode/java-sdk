# MarketDataApi

All URIs are relative to *https://api.griffnode.com/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getPrices**](MarketDataApi.md#getPrices) | **GET** /prices | Current crypto and fiat exchange rates (USD-denominated) |
| [**listCryptocurrencies**](MarketDataApi.md#listCryptocurrencies) | **GET** /cryptos/list | All supported cryptocurrencies and tokens |
| [**listMerchantCryptocurrencies**](MarketDataApi.md#listMerchantCryptocurrencies) | **GET** /merchant/cryptos | Cryptocurrencies this merchant has wallets configured for |


<a id="getPrices"></a>
# **getPrices**
> GetPrices200Response getPrices()

Current crypto and fiat exchange rates (USD-denominated)

### Example
```java
// Import classes:
import com.griffnode.sdk.ApiClient;
import com.griffnode.sdk.ApiException;
import com.griffnode.sdk.Configuration;
import com.griffnode.sdk.auth.*;
import com.griffnode.sdk.models.*;
import com.griffnode.sdk.api.MarketDataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.griffnode.com/v1");
    
    // Configure HTTP bearer authorization: SecretKey
    HttpBearerAuth SecretKey = (HttpBearerAuth) defaultClient.getAuthentication("SecretKey");
    SecretKey.setBearerToken("BEARER TOKEN");

    MarketDataApi apiInstance = new MarketDataApi(defaultClient);
    try {
      GetPrices200Response result = apiInstance.getPrices();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MarketDataApi#getPrices");
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

[**GetPrices200Response**](GetPrices200Response.md)

### Authorization

[SecretKey](../README.md#SecretKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Live rates. |  -  |
| **401** | Missing or invalid API key (UNAUTHORIZED). |  -  |
| **500** | Internal error (RATE_FETCH_FAILED, ADDRESS_GENERATION_FAILED, UPSTREAM_ERROR, …). |  -  |

<a id="listCryptocurrencies"></a>
# **listCryptocurrencies**
> ListCryptocurrencies200Response listCryptocurrencies()

All supported cryptocurrencies and tokens

### Example
```java
// Import classes:
import com.griffnode.sdk.ApiClient;
import com.griffnode.sdk.ApiException;
import com.griffnode.sdk.Configuration;
import com.griffnode.sdk.auth.*;
import com.griffnode.sdk.models.*;
import com.griffnode.sdk.api.MarketDataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.griffnode.com/v1");
    
    // Configure HTTP bearer authorization: SecretKey
    HttpBearerAuth SecretKey = (HttpBearerAuth) defaultClient.getAuthentication("SecretKey");
    SecretKey.setBearerToken("BEARER TOKEN");

    MarketDataApi apiInstance = new MarketDataApi(defaultClient);
    try {
      ListCryptocurrencies200Response result = apiInstance.listCryptocurrencies();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MarketDataApi#listCryptocurrencies");
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

[**ListCryptocurrencies200Response**](ListCryptocurrencies200Response.md)

### Authorization

[SecretKey](../README.md#SecretKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Supported-currency catalogue. |  -  |
| **401** | Missing or invalid API key (UNAUTHORIZED). |  -  |

<a id="listMerchantCryptocurrencies"></a>
# **listMerchantCryptocurrencies**
> ListCryptocurrencies200Response listMerchantCryptocurrencies()

Cryptocurrencies this merchant has wallets configured for

### Example
```java
// Import classes:
import com.griffnode.sdk.ApiClient;
import com.griffnode.sdk.ApiException;
import com.griffnode.sdk.Configuration;
import com.griffnode.sdk.auth.*;
import com.griffnode.sdk.models.*;
import com.griffnode.sdk.api.MarketDataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.griffnode.com/v1");
    
    // Configure HTTP bearer authorization: SecretKey
    HttpBearerAuth SecretKey = (HttpBearerAuth) defaultClient.getAuthentication("SecretKey");
    SecretKey.setBearerToken("BEARER TOKEN");

    MarketDataApi apiInstance = new MarketDataApi(defaultClient);
    try {
      ListCryptocurrencies200Response result = apiInstance.listMerchantCryptocurrencies();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MarketDataApi#listMerchantCryptocurrencies");
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

[**ListCryptocurrencies200Response**](ListCryptocurrencies200Response.md)

### Authorization

[SecretKey](../README.md#SecretKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The merchant&#39;s configured currencies. |  -  |
| **401** | Missing or invalid API key (UNAUTHORIZED). |  -  |

