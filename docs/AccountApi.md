# AccountApi

All URIs are relative to *https://api.griffnode.com/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getAccount**](AccountApi.md#getAccount) | **GET** /account | Merchant plan, usage and limits |
| [**getStats**](AccountApi.md#getStats) | **GET** /stats | Merchant transaction analytics |
| [**listBalances**](AccountApi.md#listBalances) | **GET** /balances | Deprecated: always an empty list. GriffNode keeps no on-platform balance (no overage, no top-ups); crypto settles straight to your wallet. |
| [**listInvoices**](AccountApi.md#listInvoices) | **GET** /invoices | GriffNode billing invoices (platform ↔ merchant) |
| [**listPlans**](AccountApi.md#listPlans) | **GET** /plans | Plan catalogue and pricing |


<a id="getAccount"></a>
# **getAccount**
> GetAccount200Response getAccount()

Merchant plan, usage and limits

### Example
```java
// Import classes:
import com.griffnode.sdk.ApiClient;
import com.griffnode.sdk.ApiException;
import com.griffnode.sdk.Configuration;
import com.griffnode.sdk.auth.*;
import com.griffnode.sdk.models.*;
import com.griffnode.sdk.api.AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.griffnode.com/v1");
    
    // Configure HTTP bearer authorization: SecretKey
    HttpBearerAuth SecretKey = (HttpBearerAuth) defaultClient.getAuthentication("SecretKey");
    SecretKey.setBearerToken("BEARER TOKEN");

    AccountApi apiInstance = new AccountApi(defaultClient);
    try {
      GetAccount200Response result = apiInstance.getAccount();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountApi#getAccount");
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

[**GetAccount200Response**](GetAccount200Response.md)

### Authorization

[SecretKey](../README.md#SecretKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Account details. |  -  |
| **401** | Missing or invalid API key (UNAUTHORIZED). |  -  |
| **403** | Key lacks permission — e.g. a publishable key on a secret-only endpoint, or plan too low (FORBIDDEN, USE_PAY_ENDPOINT, PLAN_UPGRADE_REQUIRED, NO_ACTIVE_PLAN). |  -  |

<a id="getStats"></a>
# **getStats**
> GetStats200Response getStats()

Merchant transaction analytics

### Example
```java
// Import classes:
import com.griffnode.sdk.ApiClient;
import com.griffnode.sdk.ApiException;
import com.griffnode.sdk.Configuration;
import com.griffnode.sdk.auth.*;
import com.griffnode.sdk.models.*;
import com.griffnode.sdk.api.AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.griffnode.com/v1");
    
    // Configure HTTP bearer authorization: SecretKey
    HttpBearerAuth SecretKey = (HttpBearerAuth) defaultClient.getAuthentication("SecretKey");
    SecretKey.setBearerToken("BEARER TOKEN");

    AccountApi apiInstance = new AccountApi(defaultClient);
    try {
      GetStats200Response result = apiInstance.getStats();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountApi#getStats");
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

[**GetStats200Response**](GetStats200Response.md)

### Authorization

[SecretKey](../README.md#SecretKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Stats. |  -  |
| **401** | Missing or invalid API key (UNAUTHORIZED). |  -  |
| **403** | Key lacks permission — e.g. a publishable key on a secret-only endpoint, or plan too low (FORBIDDEN, USE_PAY_ENDPOINT, PLAN_UPGRADE_REQUIRED, NO_ACTIVE_PLAN). |  -  |

<a id="listBalances"></a>
# **listBalances**
> ListBalances200Response listBalances()

Deprecated: always an empty list. GriffNode keeps no on-platform balance (no overage, no top-ups); crypto settles straight to your wallet.

### Example
```java
// Import classes:
import com.griffnode.sdk.ApiClient;
import com.griffnode.sdk.ApiException;
import com.griffnode.sdk.Configuration;
import com.griffnode.sdk.auth.*;
import com.griffnode.sdk.models.*;
import com.griffnode.sdk.api.AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.griffnode.com/v1");
    
    // Configure HTTP bearer authorization: SecretKey
    HttpBearerAuth SecretKey = (HttpBearerAuth) defaultClient.getAuthentication("SecretKey");
    SecretKey.setBearerToken("BEARER TOKEN");

    AccountApi apiInstance = new AccountApi(defaultClient);
    try {
      ListBalances200Response result = apiInstance.listBalances();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountApi#listBalances");
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

[**ListBalances200Response**](ListBalances200Response.md)

### Authorization

[SecretKey](../README.md#SecretKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Balances. |  -  |
| **401** | Missing or invalid API key (UNAUTHORIZED). |  -  |
| **403** | Key lacks permission — e.g. a publishable key on a secret-only endpoint, or plan too low (FORBIDDEN, USE_PAY_ENDPOINT, PLAN_UPGRADE_REQUIRED, NO_ACTIVE_PLAN). |  -  |

<a id="listInvoices"></a>
# **listInvoices**
> ListInvoices200Response listInvoices(limit, offset)

GriffNode billing invoices (platform ↔ merchant)

### Example
```java
// Import classes:
import com.griffnode.sdk.ApiClient;
import com.griffnode.sdk.ApiException;
import com.griffnode.sdk.Configuration;
import com.griffnode.sdk.auth.*;
import com.griffnode.sdk.models.*;
import com.griffnode.sdk.api.AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.griffnode.com/v1");
    
    // Configure HTTP bearer authorization: SecretKey
    HttpBearerAuth SecretKey = (HttpBearerAuth) defaultClient.getAuthentication("SecretKey");
    SecretKey.setBearerToken("BEARER TOKEN");

    AccountApi apiInstance = new AccountApi(defaultClient);
    Integer limit = 20; // Integer | 
    Integer offset = 0; // Integer | 
    try {
      ListInvoices200Response result = apiInstance.listInvoices(limit, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountApi#listInvoices");
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

### Return type

[**ListInvoices200Response**](ListInvoices200Response.md)

### Authorization

[SecretKey](../README.md#SecretKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Invoices. |  -  |
| **401** | Missing or invalid API key (UNAUTHORIZED). |  -  |
| **403** | Key lacks permission — e.g. a publishable key on a secret-only endpoint, or plan too low (FORBIDDEN, USE_PAY_ENDPOINT, PLAN_UPGRADE_REQUIRED, NO_ACTIVE_PLAN). |  -  |

<a id="listPlans"></a>
# **listPlans**
> ListPlans200Response listPlans()

Plan catalogue and pricing

### Example
```java
// Import classes:
import com.griffnode.sdk.ApiClient;
import com.griffnode.sdk.ApiException;
import com.griffnode.sdk.Configuration;
import com.griffnode.sdk.auth.*;
import com.griffnode.sdk.models.*;
import com.griffnode.sdk.api.AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.griffnode.com/v1");
    
    // Configure HTTP bearer authorization: SecretKey
    HttpBearerAuth SecretKey = (HttpBearerAuth) defaultClient.getAuthentication("SecretKey");
    SecretKey.setBearerToken("BEARER TOKEN");

    AccountApi apiInstance = new AccountApi(defaultClient);
    try {
      ListPlans200Response result = apiInstance.listPlans();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountApi#listPlans");
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

[**ListPlans200Response**](ListPlans200Response.md)

### Authorization

[SecretKey](../README.md#SecretKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Plans. |  -  |
| **401** | Missing or invalid API key (UNAUTHORIZED). |  -  |
| **403** | Key lacks permission — e.g. a publishable key on a secret-only endpoint, or plan too low (FORBIDDEN, USE_PAY_ENDPOINT, PLAN_UPGRADE_REQUIRED, NO_ACTIVE_PLAN). |  -  |

