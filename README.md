<p align="center">
    <img src="logo.png" alt="Civo Logo">
</p>

# Python SDK for CIVO API

Easy access to the Civo Cloud Platform API.

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

## Table of Contents

- [How to install](#how-to-install)
- [Configuration](#configuration)
- [Usage](#usage)
  - [Regions](#regions)
  - [Quota](#quota)

## How to install

You can install python-digitalocean using **pip**

    pip install -U civo

or poetry:

    poetry add civo

or:

    easy_install civo

**[⬆ back to top](#table-of-contents)**

## Configuration

This is Python SDK for the Civo Cloud Platform. First, you should get an API key, through the [Civo Account Dashboard](https://www.civo.com/account/security), on _Security_ tab. After you have your API key, you should create and `.env` file or pass the API key as param to the Civo Python SDK. The _CIVO_TOKEN_ or _token_ params are **required**.

    CIVO_TOKEN=klEoWjEtDNsiusI38xGk9WZWeFnKrzECj1ZE9dwdK8nvcW1q

**[⬆ back to top](#table-of-contents)**

## Usage

First, import the `AsyncCivoClient` (or `SyncCivoClient`) class and create your **Civo** asynchronous (or synchronous) client using the API key.

```python
from civo.v2 import AsyncCivoClient

client = AsyncCivoClient(token="klEoWjEtDNsiusI38xGk9WZWeFnKrzECj1ZE9dwdK8nvcW1q")
```

It is also possible to use the `CivoAuth` class (which by default obtains its properties from environment variables or from the content of the `.env` file) and the static method `AsyncCivoClient.from_auth` (or `SyncCivoClient.from_auth`) to initialize the client.

```python
from civo.v2 import AsyncCivoClient, CivoAuth

client = AsyncCivoClient.from_auth(CivoAuth())
```

The recommended way to use the Civo client is as context manager. For example:

```python
async with AsyncCivoClient(...) as client:
    ...
```

or

```python
with SyncCivoClient(...) as client:
    ...
```

### Regions

```python
async with AsyncCivoClient(...) as client:
    regions = client.get_regions()
```

Example response:

```python
Regions(regions=[Region(code='NYC1', name='New York 1', type='civostack', default=True, out_of_capacity=False, country='us', country_name='United States', features={'iaas': True, 'kubernetes': True}), Region(code='FRA1', name='Frankfurt 1', type='civostack', default=False, out_of_capacity=False, country='de', country_name='Germany', features={'iaas': True, 'kubernetes': True}), Region(code='LON1', name='London 1', type='civostack', default=False, out_of_capacity=False, country='uk', country_name='United Kingdom', features={'iaas': True, 'kubernetes': True})])
```

### Quota

```python
async with AsyncCivoClient(...) as client:
    quota = client.get_quota()
```

**[⬆ back to top](#table-of-contents)**

## Contributors

<p align="center">
    <img src="http://ForTheBadge.com/images/badges/made-with-python.svg">
</p>
