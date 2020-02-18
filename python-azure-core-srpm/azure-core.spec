#
# spec file for package python-azure-core
#
# Copyright (c) 2020 Nico Kadel-Garcia.
#

# Fedora and RHEL split python2 and python3
# Older RHEL requires EPEL and python34 or python36
%global with_python3 1

# Incompatible with python2
%global with_python2 0

%global pypi_name azure-core

# Common SRPM package
Name:           python-%{pypi_name}
Version:        1.2.2
Release:        0%{?dist}
Url:            https://github.com/Azure/azure-sdk-for-python/tree/master/sdk/core/azure-core
Summary:        Microsoft Azure Core Library for Python
License:        MIT
Group:          Development/Languages/Python
# Stop using py2pack macros, use local macros published by Fedora
Source0:        https://files.pythonhosted.org/packages/source/%(n=%{pypi_name}; echo ${n:0:1})/%{pypi_name}/%{pypi_name}-%{version}.zip
BuildArch:      noarch

%if 0%{?rhel}
Buildrequires: epel-rpm-macros
%endif

BuildRequires:  unzip

%description

# Azure Core Library

Azure core library defines basic exceptions and shared modules those are needed when you use client libraries. 

As an end user, you don't need to manually install azure-core because it will be installed automatically when you install other SDKs. 

If you are a client library developer, please reference [client library developer reference](https://github.com/Azure/azure-sdk-for-python/blob/master/sdk/core/azure-core/CLIENT_LIBRARY_DEVELOPER.md) for more information.

[Source code](https://github.com/Azure/azure-sdk-for-python/tree/ce7d600e96d308e7caaa92ab8e932601a65d63ef/sdk/core/azure-core) | [Package (Pypi)][package] | [API reference documentation](https://github.com/Azure/azure-sdk-for-python/tree/ce7d600e96d308e7caaa92ab8e932601a65d63ef/sdk/core/azure-core)

## Azure Core Library Exceptions

### AzureError
AzureError is the base exception for all errors.
```python
class AzureError(Exception):
    def __init__(self, message, *args, **kwargs):
        self.inner_exception = kwargs.get('error')
        self.exc_type, self.exc_value, self.exc_traceback = sys.exc_info()
        self.exc_type = self.exc_type.__name__ if self.exc_type else type(self.inner_exception)
        self.exc_msg = "{}, {}: {}".format(message, self.exc_type, self.exc_value)  # type: ignore
        self.message = str(message)
        super(AzureError, self).__init__(self.message, *args)
```

*message* is any message (str) to be associated with the exception. 

*args* are any additional args to be included with exception.

*kwargs* are keyword arguments to include with the exception. Use the keyword *error* to pass in an internal exception.

**The following exceptions inherit from AzureError:**

### ServiceRequestError
An error occurred while attempt to make a request to the service. No request was sent.

### ServiceResponseError
The request was sent, but the client failed to understand the response.
The connection may have timed out. These errors can be retried for idempotent or safe operations.

### HttpResponseError
A request was made, and a non-success status code was received from the service.
```python
class HttpResponseError(AzureError):
    def __init__(self, message=None, response=None, **kwargs):
        self.reason = None
        self.response = response
        if response:
            self.reason = response.reason
        message = "Operation returned an invalid status code '{}'".format(self.reason)
        try:
            try:
                if self.error.error.code or self.error.error.message:
                    message = "({}) {}".format(
                        self.error.error.code,
                        self.error.error.message)
            except AttributeError:
                if self.error.message: #pylint: disable=no-member
                    message = self.error.message #pylint: disable=no-member
        except AttributeError:
            pass
        super(HttpResponseError, self).__init__(message=message, **kwargs)
```
*message* is the HTTP response error message (optional)

*response* is the HTTP response (optional).

*kwargs* are keyword arguments to include with the exception.

**The following exceptions inherit from HttpResponseError:**

### DecodeError
An error raised during response deserialization.

### ResourceExistsError
An error response with status code 4xx. This will not be raised directly by the Azure core pipeline.

### ResourceNotFoundError
An error response, typically triggered by a 412 response (for update) or 404 (for get/post).

### ClientAuthenticationError
An error response with status code 4xx. This will not be raised directly by the Azure core pipeline.

### ResourceModifiedError
An error response with status code 4xx, typically 412 Conflict. This will not be raised directly by the Azure core pipeline.

### ResourceNotModifiedError
An error response with status code 304. This will not be raised directly by the Azure core pipeline.

### TooManyRedirectsError
An error raised when the maximum number of redirect attempts is reached. The maximum amount of redirects can be configured in the RedirectPolicy.
```python
class TooManyRedirectsError(HttpResponseError):
    def __init__(self, history, *args, **kwargs):
        self.history = history
        message = "Reached maximum redirect attempts."
        super(TooManyRedirectsError, self).__init__(message, *args, **kwargs)
```

*history* is used to document the requests/responses that resulted in redirected requests.

*args* are any additional args to be included with exception.

*kwargs* are keyword arguments to include with the exception.

## Shared modules

### MatchConditions
MatchConditions is an enum to describe match conditions.
```python
class MatchConditions(Enum):
    Unconditionally = 1
    IfNotModified = 2
    IfModified = 3
    IfPresent = 4
    IfMissing = 5
```

## Contributing
This project welcomes contributions and suggestions. Most contributions require
you to agree to a Contributor License Agreement (CLA) declaring that you have
the right to, and actually do, grant us the rights to use your contribution.
For details, visit [https://cla.microsoft.com](https://cla.microsoft.com).

When you submit a pull request, a CLA-bot will automatically determine whether
you need to provide a CLA and decorate the PR appropriately (e.g., label,
comment). Simply follow the instructions provided by the bot. You will only
need to do this once across all repos using our CLA.

This project has adopted the
[Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
For more information, see the
[Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/)
or contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any
additional questions or comments.

<!-- LINKS -->
[package]: https://pypi.org/project/azure-core/


# Release History

## 1.2.2 (2020-02-10)

### Bug fixes

- Fixed a bug that sends None as request_id #9545
- Enable mypy for customers #9572
- Handle TypeError in deep copy #9620
- Fix text/plain content-type in decoder #9589

## 1.2.1 (2020-01-14)

### Bug fixes

- Fixed a regression in 1.2.0 that was incompatible with azure-keyvault-* 4.0.0
[#9462](https://github.com/Azure/azure-sdk-for-python/issues/9462)


## 1.2.0 (2020-01-14)

### Features

- Add user_agent & sdk_moniker kwargs in UserAgentPolicy init   #9355
- Support OPTIONS HTTP verb     #9322
- Add tracing_attributes to tracing decorator   #9297
- Support auto_request_id in RequestIdPolicy   #9163
- Support fixed retry   #6419
- Support "retry-after-ms" in response header   #9240

### Bug fixes

- Removed `__enter__` and `__exit__` from async context managers    #9313

## 1.1.1 (2019-12-03)

### Bug fixes

- Bearer token authorization requires HTTPS
- Rewind the body position in retry #8307

## 1.1.0 (2019-11-25)

### Features

- New RequestIdPolicy   #8437
- Enable logging policy in default pipeline #8053
- Normalize transport timeout.   #8000
  Now we have:
  * 'connection_timeout' - a single float in seconds for the connection timeout. Default 5min
  * 'read_timeout' - a single float in seconds for the read timeout. Default 5min

### Bug fixes

- RequestHistory: deepcopy fails if request contains a stream  #7732
- Retry: retry raises error if response does not have http_response #8629
- Client kwargs are now passed to DistributedTracingPolicy correctly    #8051
- NetworkLoggingPolicy now logs correctly all requests in case of retry #8262

## 1.0.0 (2019-10-29)

### Features

- Tracing: DistributedTracingPolicy now accepts kwargs network_span_namer to change network span name  #7773
- Tracing: Implementation of AbstractSpan can now use the mixin HttpSpanMixin to get HTTP span update automatically  #7773
- Tracing: AbstractSpan contract "change_context" introduced  #7773
- Introduce new policy HttpLoggingPolicy  #7988

### Bug fixes

- Fix AsyncioRequestsTransport if input stream is an async generator  #7743
- Fix form-data with aiohttp transport  #7749

### Breaking changes

- Tracing: AbstractSpan.set_current_span is longer supported. Use change_context instead.  #7773
- azure.core.pipeline.policies.ContentDecodePolicy.deserialize_from_text changed

## 1.0.0b4 (2019-10-07)

### Features

- Tracing: network span context is available with the TRACING_CONTEXT in pipeline response  #7252
- Tracing: Span contract now has `kind`, `traceparent` and is a context manager  #7252
- SansIOHTTPPolicy methods can now be coroutines #7497
- Add multipart/mixed support #7083:

  - HttpRequest now has a "set_multipart_mixed" method to set the parts of this request
  - HttpRequest now has a "prepare_multipart_body" method to build final body.
  - HttpResponse now has a "parts" method to return an iterator of parts
  - AsyncHttpResponse now has a "parts" methods to return an async iterator of parts
  - Note that multipart/mixed is a Python 3.x only feature

### Bug fixes

- Tracing: policy cannot fail the pipeline, even in the worst condition  #7252
- Tracing: policy pass correctly status message if exception  #7252
- Tracing: incorrect span if exception raised from decorated function  #7133
- Fixed urllib3 ConnectTimeoutError being raised by Requests during a socket timeout. Now this exception is caught and wrapped as a `ServiceRequestError`  #7542

### Breaking changes

- Tracing: `azure.core.tracing.context` removed
- Tracing: `azure.core.tracing.context.tracing_context.with_current_context` renamed to `azure.core.tracing.common.with_current_context`  #7252
- Tracing: `link` renamed `link_from_headers`  and `link` takes now a string
- Tracing: opencensus implementation has been moved to the package `azure-core-tracing-opencensus`
- Some modules and classes that were importables from several differente places have been removed:

   - `azure.core.HttpResponseError` is now only `azure.core.exceptions.HttpResponseError`
   - `azure.core.Configuration` is now only `azure.core.configuration.Configuration`
   - `azure.core.HttpRequest` is now only `azure.core.pipeline.transport.HttpRequest`
   - `azure.core.version` module has been removed. Use `azure.core.__version__` to get version number.
   - `azure.core.pipeline_client` has been removed. Import from `azure.core` instead.
   - `azure.core.pipeline_client_async` has been removed. Import from `azure.core` instead.
   - `azure.core.pipeline.base` has been removed. Import from `azure.core.pipeline` instead.
   - `azure.core.pipeline.base_async` has been removed. Import from `azure.core.pipeline` instead.
   - `azure.core.pipeline.policies.base` has been removed. Import from `azure.core.pipeline.policies` instead.
   - `azure.core.pipeline.policies.base_async` has been removed. Import from `azure.core.pipeline.policies` instead.
   - `azure.core.pipeline.policies.authentication` has been removed. Import from `azure.core.pipeline.policies` instead.
   - `azure.core.pipeline.policies.authentication_async` has been removed. Import from `azure.core.pipeline.policies` instead.
   - `azure.core.pipeline.policies.custom_hook` has been removed. Import from `azure.core.pipeline.policies` instead.
   - `azure.core.pipeline.policies.redirect` has been removed. Import from `azure.core.pipeline.policies` instead.
   - `azure.core.pipeline.policies.redirect_async` has been removed. Import from `azure.core.pipeline.policies` instead.
   - `azure.core.pipeline.policies.retry` has been removed. Import from `azure.core.pipeline.policies` instead.
   - `azure.core.pipeline.policies.retry_async` has been removed. Import from `azure.core.pipeline.policies` instead.
   - `azure.core.pipeline.policies.distributed_tracing` has been removed. Import from `azure.core.pipeline.policies` instead.
   - `azure.core.pipeline.policies.universal` has been removed. Import from `azure.core.pipeline.policies` instead.
   - `azure.core.tracing.abstract_span` has been removed. Import from `azure.core.tracing` instead.
   - `azure.core.pipeline.transport.base` has been removed. Import from `azure.core.pipeline.transport` instead.
   - `azure.core.pipeline.transport.base_async` has been removed. Import from `azure.core.pipeline.transport` instead.
   - `azure.core.pipeline.transport.requests_basic` has been removed. Import from `azure.core.pipeline.transport` instead.
   - `azure.core.pipeline.transport.requests_asyncio` has been removed. Import from `azure.core.pipeline.transport` instead.
   - `azure.core.pipeline.transport.requests_trio` has been removed. Import from `azure.core.pipeline.transport` instead.
   - `azure.core.pipeline.transport.aiohttp` has been removed. Import from `azure.core.pipeline.transport` instead.
   - `azure.core.polling.poller` has been removed. Import from `azure.core.polling` instead.
   - `azure.core.polling.async_poller` has been removed. Import from `azure.core.polling` instead.

## 1.0.0b3 (2019-09-09)

### Bug fixes

-  Fix aiohttp auto-headers #6992
-  Add tracing to policies module init  #6951

## 1.0.0b2 (2019-08-05)

### Breaking changes

- Transport classes don't take `config` parameter anymore (use kwargs instead)  #6372
- `azure.core.paging` has been completely refactored  #6420
- HttpResponse.content_type attribute is now a string (was a list)  #6490
- For `StreamDownloadGenerator` subclasses, `response` is now an `HttpResponse`, and not a transport response like `aiohttp.ClientResponse` or `requests.Response`. The transport response is available in `internal_response` attribute  #6490

### Bug fixes

- aiohttp is not required to import async pipelines classes #6496
- `AsyncioRequestsTransport.sleep` is now a coroutine as expected #6490
- `RequestsTransport` is not tight to `ProxyPolicy` implementation details anymore #6372
- `AiohttpTransport` does not raise on unexpected kwargs  #6355

### Features

- New paging base classes that support `continuation_token` and `by_page()`  #6420
- Proxy support for `AiohttpTransport`  #6372

## 1.0.0b1 (2019-06-26)

- Preview 1 release




%if %{with_python2}
%package -n python2-%{pypi_name}
Version:        1.2.2
Release:        0%{?dist}
Url:            https://github.com/Azure/azure-sdk-for-python/tree/master/sdk/core/azure-core
Summary:        Microsoft Azure Core Library for Python
License:        MIT

BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
%{?python_provide:%python_provide python2-%{pypi_name}}

%description -n python2-%{pypi_name}

# Azure Core Library

Azure core library defines basic exceptions and shared modules those are needed when you use client libraries. 

As an end user, you don't need to manually install azure-core because it will be installed automatically when you install other SDKs. 

If you are a client library developer, please reference [client library developer reference](https://github.com/Azure/azure-sdk-for-python/blob/master/sdk/core/azure-core/CLIENT_LIBRARY_DEVELOPER.md) for more information.

[Source code](https://github.com/Azure/azure-sdk-for-python/tree/ce7d600e96d308e7caaa92ab8e932601a65d63ef/sdk/core/azure-core) | [Package (Pypi)][package] | [API reference documentation](https://github.com/Azure/azure-sdk-for-python/tree/ce7d600e96d308e7caaa92ab8e932601a65d63ef/sdk/core/azure-core)

## Azure Core Library Exceptions

### AzureError
AzureError is the base exception for all errors.
```python
class AzureError(Exception):
    def __init__(self, message, *args, **kwargs):
        self.inner_exception = kwargs.get('error')
        self.exc_type, self.exc_value, self.exc_traceback = sys.exc_info()
        self.exc_type = self.exc_type.__name__ if self.exc_type else type(self.inner_exception)
        self.exc_msg = "{}, {}: {}".format(message, self.exc_type, self.exc_value)  # type: ignore
        self.message = str(message)
        super(AzureError, self).__init__(self.message, *args)
```

*message* is any message (str) to be associated with the exception. 

*args* are any additional args to be included with exception.

*kwargs* are keyword arguments to include with the exception. Use the keyword *error* to pass in an internal exception.

**The following exceptions inherit from AzureError:**

### ServiceRequestError
An error occurred while attempt to make a request to the service. No request was sent.

### ServiceResponseError
The request was sent, but the client failed to understand the response.
The connection may have timed out. These errors can be retried for idempotent or safe operations.

### HttpResponseError
A request was made, and a non-success status code was received from the service.
```python
class HttpResponseError(AzureError):
    def __init__(self, message=None, response=None, **kwargs):
        self.reason = None
        self.response = response
        if response:
            self.reason = response.reason
        message = "Operation returned an invalid status code '{}'".format(self.reason)
        try:
            try:
                if self.error.error.code or self.error.error.message:
                    message = "({}) {}".format(
                        self.error.error.code,
                        self.error.error.message)
            except AttributeError:
                if self.error.message: #pylint: disable=no-member
                    message = self.error.message #pylint: disable=no-member
        except AttributeError:
            pass
        super(HttpResponseError, self).__init__(message=message, **kwargs)
```
*message* is the HTTP response error message (optional)

*response* is the HTTP response (optional).

*kwargs* are keyword arguments to include with the exception.

**The following exceptions inherit from HttpResponseError:**

### DecodeError
An error raised during response deserialization.

### ResourceExistsError
An error response with status code 4xx. This will not be raised directly by the Azure core pipeline.

### ResourceNotFoundError
An error response, typically triggered by a 412 response (for update) or 404 (for get/post).

### ClientAuthenticationError
An error response with status code 4xx. This will not be raised directly by the Azure core pipeline.

### ResourceModifiedError
An error response with status code 4xx, typically 412 Conflict. This will not be raised directly by the Azure core pipeline.

### ResourceNotModifiedError
An error response with status code 304. This will not be raised directly by the Azure core pipeline.

### TooManyRedirectsError
An error raised when the maximum number of redirect attempts is reached. The maximum amount of redirects can be configured in the RedirectPolicy.
```python
class TooManyRedirectsError(HttpResponseError):
    def __init__(self, history, *args, **kwargs):
        self.history = history
        message = "Reached maximum redirect attempts."
        super(TooManyRedirectsError, self).__init__(message, *args, **kwargs)
```

*history* is used to document the requests/responses that resulted in redirected requests.

*args* are any additional args to be included with exception.

*kwargs* are keyword arguments to include with the exception.

## Shared modules

### MatchConditions
MatchConditions is an enum to describe match conditions.
```python
class MatchConditions(Enum):
    Unconditionally = 1
    IfNotModified = 2
    IfModified = 3
    IfPresent = 4
    IfMissing = 5
```

## Contributing
This project welcomes contributions and suggestions. Most contributions require
you to agree to a Contributor License Agreement (CLA) declaring that you have
the right to, and actually do, grant us the rights to use your contribution.
For details, visit [https://cla.microsoft.com](https://cla.microsoft.com).

When you submit a pull request, a CLA-bot will automatically determine whether
you need to provide a CLA and decorate the PR appropriately (e.g., label,
comment). Simply follow the instructions provided by the bot. You will only
need to do this once across all repos using our CLA.

This project has adopted the
[Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
For more information, see the
[Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/)
or contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any
additional questions or comments.

<!-- LINKS -->
[package]: https://pypi.org/project/azure-core/


# Release History

## 1.2.2 (2020-02-10)

### Bug fixes

- Fixed a bug that sends None as request_id #9545
- Enable mypy for customers #9572
- Handle TypeError in deep copy #9620
- Fix text/plain content-type in decoder #9589

## 1.2.1 (2020-01-14)

### Bug fixes

- Fixed a regression in 1.2.0 that was incompatible with azure-keyvault-* 4.0.0
[#9462](https://github.com/Azure/azure-sdk-for-python/issues/9462)


## 1.2.0 (2020-01-14)

### Features

- Add user_agent & sdk_moniker kwargs in UserAgentPolicy init   #9355
- Support OPTIONS HTTP verb     #9322
- Add tracing_attributes to tracing decorator   #9297
- Support auto_request_id in RequestIdPolicy   #9163
- Support fixed retry   #6419
- Support "retry-after-ms" in response header   #9240

### Bug fixes

- Removed `__enter__` and `__exit__` from async context managers    #9313

## 1.1.1 (2019-12-03)

### Bug fixes

- Bearer token authorization requires HTTPS
- Rewind the body position in retry #8307

## 1.1.0 (2019-11-25)

### Features

- New RequestIdPolicy   #8437
- Enable logging policy in default pipeline #8053
- Normalize transport timeout.   #8000
  Now we have:
  * 'connection_timeout' - a single float in seconds for the connection timeout. Default 5min
  * 'read_timeout' - a single float in seconds for the read timeout. Default 5min

### Bug fixes

- RequestHistory: deepcopy fails if request contains a stream  #7732
- Retry: retry raises error if response does not have http_response #8629
- Client kwargs are now passed to DistributedTracingPolicy correctly    #8051
- NetworkLoggingPolicy now logs correctly all requests in case of retry #8262

## 1.0.0 (2019-10-29)

### Features

- Tracing: DistributedTracingPolicy now accepts kwargs network_span_namer to change network span name  #7773
- Tracing: Implementation of AbstractSpan can now use the mixin HttpSpanMixin to get HTTP span update automatically  #7773
- Tracing: AbstractSpan contract "change_context" introduced  #7773
- Introduce new policy HttpLoggingPolicy  #7988

### Bug fixes

- Fix AsyncioRequestsTransport if input stream is an async generator  #7743
- Fix form-data with aiohttp transport  #7749

### Breaking changes

- Tracing: AbstractSpan.set_current_span is longer supported. Use change_context instead.  #7773
- azure.core.pipeline.policies.ContentDecodePolicy.deserialize_from_text changed

## 1.0.0b4 (2019-10-07)

### Features

- Tracing: network span context is available with the TRACING_CONTEXT in pipeline response  #7252
- Tracing: Span contract now has `kind`, `traceparent` and is a context manager  #7252
- SansIOHTTPPolicy methods can now be coroutines #7497
- Add multipart/mixed support #7083:

  - HttpRequest now has a "set_multipart_mixed" method to set the parts of this request
  - HttpRequest now has a "prepare_multipart_body" method to build final body.
  - HttpResponse now has a "parts" method to return an iterator of parts
  - AsyncHttpResponse now has a "parts" methods to return an async iterator of parts
  - Note that multipart/mixed is a Python 3.x only feature

### Bug fixes

- Tracing: policy cannot fail the pipeline, even in the worst condition  #7252
- Tracing: policy pass correctly status message if exception  #7252
- Tracing: incorrect span if exception raised from decorated function  #7133
- Fixed urllib3 ConnectTimeoutError being raised by Requests during a socket timeout. Now this exception is caught and wrapped as a `ServiceRequestError`  #7542

### Breaking changes

- Tracing: `azure.core.tracing.context` removed
- Tracing: `azure.core.tracing.context.tracing_context.with_current_context` renamed to `azure.core.tracing.common.with_current_context`  #7252
- Tracing: `link` renamed `link_from_headers`  and `link` takes now a string
- Tracing: opencensus implementation has been moved to the package `azure-core-tracing-opencensus`
- Some modules and classes that were importables from several differente places have been removed:

   - `azure.core.HttpResponseError` is now only `azure.core.exceptions.HttpResponseError`
   - `azure.core.Configuration` is now only `azure.core.configuration.Configuration`
   - `azure.core.HttpRequest` is now only `azure.core.pipeline.transport.HttpRequest`
   - `azure.core.version` module has been removed. Use `azure.core.__version__` to get version number.
   - `azure.core.pipeline_client` has been removed. Import from `azure.core` instead.
   - `azure.core.pipeline_client_async` has been removed. Import from `azure.core` instead.
   - `azure.core.pipeline.base` has been removed. Import from `azure.core.pipeline` instead.
   - `azure.core.pipeline.base_async` has been removed. Import from `azure.core.pipeline` instead.
   - `azure.core.pipeline.policies.base` has been removed. Import from `azure.core.pipeline.policies` instead.
   - `azure.core.pipeline.policies.base_async` has been removed. Import from `azure.core.pipeline.policies` instead.
   - `azure.core.pipeline.policies.authentication` has been removed. Import from `azure.core.pipeline.policies` instead.
   - `azure.core.pipeline.policies.authentication_async` has been removed. Import from `azure.core.pipeline.policies` instead.
   - `azure.core.pipeline.policies.custom_hook` has been removed. Import from `azure.core.pipeline.policies` instead.
   - `azure.core.pipeline.policies.redirect` has been removed. Import from `azure.core.pipeline.policies` instead.
   - `azure.core.pipeline.policies.redirect_async` has been removed. Import from `azure.core.pipeline.policies` instead.
   - `azure.core.pipeline.policies.retry` has been removed. Import from `azure.core.pipeline.policies` instead.
   - `azure.core.pipeline.policies.retry_async` has been removed. Import from `azure.core.pipeline.policies` instead.
   - `azure.core.pipeline.policies.distributed_tracing` has been removed. Import from `azure.core.pipeline.policies` instead.
   - `azure.core.pipeline.policies.universal` has been removed. Import from `azure.core.pipeline.policies` instead.
   - `azure.core.tracing.abstract_span` has been removed. Import from `azure.core.tracing` instead.
   - `azure.core.pipeline.transport.base` has been removed. Import from `azure.core.pipeline.transport` instead.
   - `azure.core.pipeline.transport.base_async` has been removed. Import from `azure.core.pipeline.transport` instead.
   - `azure.core.pipeline.transport.requests_basic` has been removed. Import from `azure.core.pipeline.transport` instead.
   - `azure.core.pipeline.transport.requests_asyncio` has been removed. Import from `azure.core.pipeline.transport` instead.
   - `azure.core.pipeline.transport.requests_trio` has been removed. Import from `azure.core.pipeline.transport` instead.
   - `azure.core.pipeline.transport.aiohttp` has been removed. Import from `azure.core.pipeline.transport` instead.
   - `azure.core.polling.poller` has been removed. Import from `azure.core.polling` instead.
   - `azure.core.polling.async_poller` has been removed. Import from `azure.core.polling` instead.

## 1.0.0b3 (2019-09-09)

### Bug fixes

-  Fix aiohttp auto-headers #6992
-  Add tracing to policies module init  #6951

## 1.0.0b2 (2019-08-05)

### Breaking changes

- Transport classes don't take `config` parameter anymore (use kwargs instead)  #6372
- `azure.core.paging` has been completely refactored  #6420
- HttpResponse.content_type attribute is now a string (was a list)  #6490
- For `StreamDownloadGenerator` subclasses, `response` is now an `HttpResponse`, and not a transport response like `aiohttp.ClientResponse` or `requests.Response`. The transport response is available in `internal_response` attribute  #6490

### Bug fixes

- aiohttp is not required to import async pipelines classes #6496
- `AsyncioRequestsTransport.sleep` is now a coroutine as expected #6490
- `RequestsTransport` is not tight to `ProxyPolicy` implementation details anymore #6372
- `AiohttpTransport` does not raise on unexpected kwargs  #6355

### Features

- New paging base classes that support `continuation_token` and `by_page()`  #6420
- Proxy support for `AiohttpTransport`  #6372

## 1.0.0b1 (2019-06-26)

- Preview 1 release




%endif # with_python2

%if %{with_python3}
%package -n python%{python3_pkgversion}-%{pypi_name}
Version:        1.2.2
Release:        0%{?dist}
Url:            https://github.com/Azure/azure-sdk-for-python/tree/master/sdk/core/azure-core
Summary:        Microsoft Azure Core Library for Python
License:        MIT

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

%description -n python%{python3_pkgversion}-%{pypi_name}

# Azure Core Library

Azure core library defines basic exceptions and shared modules those are needed when you use client libraries. 

As an end user, you don't need to manually install azure-core because it will be installed automatically when you install other SDKs. 

If you are a client library developer, please reference [client library developer reference](https://github.com/Azure/azure-sdk-for-python/blob/master/sdk/core/azure-core/CLIENT_LIBRARY_DEVELOPER.md) for more information.

[Source code](https://github.com/Azure/azure-sdk-for-python/tree/ce7d600e96d308e7caaa92ab8e932601a65d63ef/sdk/core/azure-core) | [Package (Pypi)][package] | [API reference documentation](https://github.com/Azure/azure-sdk-for-python/tree/ce7d600e96d308e7caaa92ab8e932601a65d63ef/sdk/core/azure-core)

## Azure Core Library Exceptions

### AzureError
AzureError is the base exception for all errors.
```python
class AzureError(Exception):
    def __init__(self, message, *args, **kwargs):
        self.inner_exception = kwargs.get('error')
        self.exc_type, self.exc_value, self.exc_traceback = sys.exc_info()
        self.exc_type = self.exc_type.__name__ if self.exc_type else type(self.inner_exception)
        self.exc_msg = "{}, {}: {}".format(message, self.exc_type, self.exc_value)  # type: ignore
        self.message = str(message)
        super(AzureError, self).__init__(self.message, *args)
```

*message* is any message (str) to be associated with the exception. 

*args* are any additional args to be included with exception.

*kwargs* are keyword arguments to include with the exception. Use the keyword *error* to pass in an internal exception.

**The following exceptions inherit from AzureError:**

### ServiceRequestError
An error occurred while attempt to make a request to the service. No request was sent.

### ServiceResponseError
The request was sent, but the client failed to understand the response.
The connection may have timed out. These errors can be retried for idempotent or safe operations.

### HttpResponseError
A request was made, and a non-success status code was received from the service.
```python
class HttpResponseError(AzureError):
    def __init__(self, message=None, response=None, **kwargs):
        self.reason = None
        self.response = response
        if response:
            self.reason = response.reason
        message = "Operation returned an invalid status code '{}'".format(self.reason)
        try:
            try:
                if self.error.error.code or self.error.error.message:
                    message = "({}) {}".format(
                        self.error.error.code,
                        self.error.error.message)
            except AttributeError:
                if self.error.message: #pylint: disable=no-member
                    message = self.error.message #pylint: disable=no-member
        except AttributeError:
            pass
        super(HttpResponseError, self).__init__(message=message, **kwargs)
```
*message* is the HTTP response error message (optional)

*response* is the HTTP response (optional).

*kwargs* are keyword arguments to include with the exception.

**The following exceptions inherit from HttpResponseError:**

### DecodeError
An error raised during response deserialization.

### ResourceExistsError
An error response with status code 4xx. This will not be raised directly by the Azure core pipeline.

### ResourceNotFoundError
An error response, typically triggered by a 412 response (for update) or 404 (for get/post).

### ClientAuthenticationError
An error response with status code 4xx. This will not be raised directly by the Azure core pipeline.

### ResourceModifiedError
An error response with status code 4xx, typically 412 Conflict. This will not be raised directly by the Azure core pipeline.

### ResourceNotModifiedError
An error response with status code 304. This will not be raised directly by the Azure core pipeline.

### TooManyRedirectsError
An error raised when the maximum number of redirect attempts is reached. The maximum amount of redirects can be configured in the RedirectPolicy.
```python
class TooManyRedirectsError(HttpResponseError):
    def __init__(self, history, *args, **kwargs):
        self.history = history
        message = "Reached maximum redirect attempts."
        super(TooManyRedirectsError, self).__init__(message, *args, **kwargs)
```

*history* is used to document the requests/responses that resulted in redirected requests.

*args* are any additional args to be included with exception.

*kwargs* are keyword arguments to include with the exception.

## Shared modules

### MatchConditions
MatchConditions is an enum to describe match conditions.
```python
class MatchConditions(Enum):
    Unconditionally = 1
    IfNotModified = 2
    IfModified = 3
    IfPresent = 4
    IfMissing = 5
```

## Contributing
This project welcomes contributions and suggestions. Most contributions require
you to agree to a Contributor License Agreement (CLA) declaring that you have
the right to, and actually do, grant us the rights to use your contribution.
For details, visit [https://cla.microsoft.com](https://cla.microsoft.com).

When you submit a pull request, a CLA-bot will automatically determine whether
you need to provide a CLA and decorate the PR appropriately (e.g., label,
comment). Simply follow the instructions provided by the bot. You will only
need to do this once across all repos using our CLA.

This project has adopted the
[Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
For more information, see the
[Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/)
or contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any
additional questions or comments.

<!-- LINKS -->
[package]: https://pypi.org/project/azure-core/


# Release History

## 1.2.2 (2020-02-10)

### Bug fixes

- Fixed a bug that sends None as request_id #9545
- Enable mypy for customers #9572
- Handle TypeError in deep copy #9620
- Fix text/plain content-type in decoder #9589

## 1.2.1 (2020-01-14)

### Bug fixes

- Fixed a regression in 1.2.0 that was incompatible with azure-keyvault-* 4.0.0
[#9462](https://github.com/Azure/azure-sdk-for-python/issues/9462)


## 1.2.0 (2020-01-14)

### Features

- Add user_agent & sdk_moniker kwargs in UserAgentPolicy init   #9355
- Support OPTIONS HTTP verb     #9322
- Add tracing_attributes to tracing decorator   #9297
- Support auto_request_id in RequestIdPolicy   #9163
- Support fixed retry   #6419
- Support "retry-after-ms" in response header   #9240

### Bug fixes

- Removed `__enter__` and `__exit__` from async context managers    #9313

## 1.1.1 (2019-12-03)

### Bug fixes

- Bearer token authorization requires HTTPS
- Rewind the body position in retry #8307

## 1.1.0 (2019-11-25)

### Features

- New RequestIdPolicy   #8437
- Enable logging policy in default pipeline #8053
- Normalize transport timeout.   #8000
  Now we have:
  * 'connection_timeout' - a single float in seconds for the connection timeout. Default 5min
  * 'read_timeout' - a single float in seconds for the read timeout. Default 5min

### Bug fixes

- RequestHistory: deepcopy fails if request contains a stream  #7732
- Retry: retry raises error if response does not have http_response #8629
- Client kwargs are now passed to DistributedTracingPolicy correctly    #8051
- NetworkLoggingPolicy now logs correctly all requests in case of retry #8262

## 1.0.0 (2019-10-29)

### Features

- Tracing: DistributedTracingPolicy now accepts kwargs network_span_namer to change network span name  #7773
- Tracing: Implementation of AbstractSpan can now use the mixin HttpSpanMixin to get HTTP span update automatically  #7773
- Tracing: AbstractSpan contract "change_context" introduced  #7773
- Introduce new policy HttpLoggingPolicy  #7988

### Bug fixes

- Fix AsyncioRequestsTransport if input stream is an async generator  #7743
- Fix form-data with aiohttp transport  #7749

### Breaking changes

- Tracing: AbstractSpan.set_current_span is longer supported. Use change_context instead.  #7773
- azure.core.pipeline.policies.ContentDecodePolicy.deserialize_from_text changed

## 1.0.0b4 (2019-10-07)

### Features

- Tracing: network span context is available with the TRACING_CONTEXT in pipeline response  #7252
- Tracing: Span contract now has `kind`, `traceparent` and is a context manager  #7252
- SansIOHTTPPolicy methods can now be coroutines #7497
- Add multipart/mixed support #7083:

  - HttpRequest now has a "set_multipart_mixed" method to set the parts of this request
  - HttpRequest now has a "prepare_multipart_body" method to build final body.
  - HttpResponse now has a "parts" method to return an iterator of parts
  - AsyncHttpResponse now has a "parts" methods to return an async iterator of parts
  - Note that multipart/mixed is a Python 3.x only feature

### Bug fixes

- Tracing: policy cannot fail the pipeline, even in the worst condition  #7252
- Tracing: policy pass correctly status message if exception  #7252
- Tracing: incorrect span if exception raised from decorated function  #7133
- Fixed urllib3 ConnectTimeoutError being raised by Requests during a socket timeout. Now this exception is caught and wrapped as a `ServiceRequestError`  #7542

### Breaking changes

- Tracing: `azure.core.tracing.context` removed
- Tracing: `azure.core.tracing.context.tracing_context.with_current_context` renamed to `azure.core.tracing.common.with_current_context`  #7252
- Tracing: `link` renamed `link_from_headers`  and `link` takes now a string
- Tracing: opencensus implementation has been moved to the package `azure-core-tracing-opencensus`
- Some modules and classes that were importables from several differente places have been removed:

   - `azure.core.HttpResponseError` is now only `azure.core.exceptions.HttpResponseError`
   - `azure.core.Configuration` is now only `azure.core.configuration.Configuration`
   - `azure.core.HttpRequest` is now only `azure.core.pipeline.transport.HttpRequest`
   - `azure.core.version` module has been removed. Use `azure.core.__version__` to get version number.
   - `azure.core.pipeline_client` has been removed. Import from `azure.core` instead.
   - `azure.core.pipeline_client_async` has been removed. Import from `azure.core` instead.
   - `azure.core.pipeline.base` has been removed. Import from `azure.core.pipeline` instead.
   - `azure.core.pipeline.base_async` has been removed. Import from `azure.core.pipeline` instead.
   - `azure.core.pipeline.policies.base` has been removed. Import from `azure.core.pipeline.policies` instead.
   - `azure.core.pipeline.policies.base_async` has been removed. Import from `azure.core.pipeline.policies` instead.
   - `azure.core.pipeline.policies.authentication` has been removed. Import from `azure.core.pipeline.policies` instead.
   - `azure.core.pipeline.policies.authentication_async` has been removed. Import from `azure.core.pipeline.policies` instead.
   - `azure.core.pipeline.policies.custom_hook` has been removed. Import from `azure.core.pipeline.policies` instead.
   - `azure.core.pipeline.policies.redirect` has been removed. Import from `azure.core.pipeline.policies` instead.
   - `azure.core.pipeline.policies.redirect_async` has been removed. Import from `azure.core.pipeline.policies` instead.
   - `azure.core.pipeline.policies.retry` has been removed. Import from `azure.core.pipeline.policies` instead.
   - `azure.core.pipeline.policies.retry_async` has been removed. Import from `azure.core.pipeline.policies` instead.
   - `azure.core.pipeline.policies.distributed_tracing` has been removed. Import from `azure.core.pipeline.policies` instead.
   - `azure.core.pipeline.policies.universal` has been removed. Import from `azure.core.pipeline.policies` instead.
   - `azure.core.tracing.abstract_span` has been removed. Import from `azure.core.tracing` instead.
   - `azure.core.pipeline.transport.base` has been removed. Import from `azure.core.pipeline.transport` instead.
   - `azure.core.pipeline.transport.base_async` has been removed. Import from `azure.core.pipeline.transport` instead.
   - `azure.core.pipeline.transport.requests_basic` has been removed. Import from `azure.core.pipeline.transport` instead.
   - `azure.core.pipeline.transport.requests_asyncio` has been removed. Import from `azure.core.pipeline.transport` instead.
   - `azure.core.pipeline.transport.requests_trio` has been removed. Import from `azure.core.pipeline.transport` instead.
   - `azure.core.pipeline.transport.aiohttp` has been removed. Import from `azure.core.pipeline.transport` instead.
   - `azure.core.polling.poller` has been removed. Import from `azure.core.polling` instead.
   - `azure.core.polling.async_poller` has been removed. Import from `azure.core.polling` instead.

## 1.0.0b3 (2019-09-09)

### Bug fixes

-  Fix aiohttp auto-headers #6992
-  Add tracing to policies module init  #6951

## 1.0.0b2 (2019-08-05)

### Breaking changes

- Transport classes don't take `config` parameter anymore (use kwargs instead)  #6372
- `azure.core.paging` has been completely refactored  #6420
- HttpResponse.content_type attribute is now a string (was a list)  #6490
- For `StreamDownloadGenerator` subclasses, `response` is now an `HttpResponse`, and not a transport response like `aiohttp.ClientResponse` or `requests.Response`. The transport response is available in `internal_response` attribute  #6490

### Bug fixes

- aiohttp is not required to import async pipelines classes #6496
- `AsyncioRequestsTransport.sleep` is now a coroutine as expected #6490
- `RequestsTransport` is not tight to `ProxyPolicy` implementation details anymore #6372
- `AiohttpTransport` does not raise on unexpected kwargs  #6355

### Features

- New paging base classes that support `continuation_token` and `by_page()`  #6420
- Proxy support for `AiohttpTransport`  #6372

## 1.0.0b1 (2019-06-26)

- Preview 1 release




%endif # with_python3

%prep
%setup -q -n %{pypi_name}-%{version}

%build
%if %{with_python2}
%py2_build
%endif # with_python2

%if %{with_python3}
%py3_build
%endif # with_python3

%install
%if %{with_python2}
%py2_install
%endif # with_python2

%if %{with_python3}
%py3_install
%endif # with_python3

%clean
rm -rf %{buildroot}

%if %{with_python2}
%files -n python2-%{pypi_name}
%defattr(-,root,root,-)
%{python2_sitelib}/*
%endif # with_python2

%if %{with_python3}
%files -n python%{python3_pkgversion}-%{pypi_name}
%defattr(-,root,root,-)
%{python3_sitelib}/*
%endif # with_python3

%changelog
