# Lord Of The Rings SDK

The Lord Of The Rings SDK is a Python client for The One API. It provides a simple and convenient way to interact with the API, supporting pagination, sorting, and filtering options for making requests.

## Installation
Install it directly from the source code, you can do so with pip as well. Navigate to the root directory of the SDK source code (the directory containing setup.py), and run:

```bash
pip install .
```

[//]: # (Only after the published SDK to PyPI, it can be installed with pip, like so:)

[//]: # (```bash)

[//]: # (pip install kholmatov-sdk)

[//]: # (```)

## Usage

First, you need to import the `Client` from the SDK and initialize it with your API key:

```python
from kholmatov_sdk import Client

client = Client(api_key='your_api_key')
```

The SDK provides several methods to interact with the API:

- `get_movies`: Fetches movies.
- `get_movie`: Fetches a specific movie by its ID.
- `get_movie_quotes`: Fetches quotes from a specific movie by its ID.
- `get_quotes`: Fetches quotes.
- `get_quote`: Fetches a specific quote by its ID.

### Pagination:

```python
# Limit the number of items per page (default limit is 10)
movies = client.get_movies(limit=100)

# Get a specific page (page numbers start at 1)
movies = client.get_movies(page=2)

# Offset by a certain number of items (default offset is 0)
movies = client.get_movies(offset=3)
```

### Sorting:

```python
# Sort by name in ascending order
movies = client.get_movies(sort='name:asc')

# Sort by character in descending order
quotes = client.get_quotes(sort='character:desc')
```

### Filtering:

The filtering works by casting simple URL parameter expressions to MongoDB lookup expressions and can be applied to any available key on the data models.

```python
# Match / negate match
movies = client.get_movies(name='The Hobbit Series')
movies = client.get_movies(name=('!=', 'The Hobbit Series'))

# Existence check
movies = client.get_movies(name='filtering_exists')  # Check if name exists
movies = client.get_movies(name='filtering_not_exists')  # Check if name does not exist

# Regular expressions
movies = client.get_movies(name='/Ring/i')
movies = client.get_movies(name=('!=', '/Ring/i'))

# Comparison operations

movies = client.get_movies(budgetInMillions=('<', 100))
movies = client.get_movies(academyAwardWins=('>', 0))
movies = client.get_movies(runtimeInMinutes=('>=', 160))
```
## Testing

The SDK includes a suite of unit tests that you can run to verify its functionality on your system. These tests make use of the `unittest` module from Python's standard library, and they're designed to assert the correctness of the SDK's various features. 

You can run the tests with the following command:

```bash
python -m unittest discover
```

This command tells Python to run the `unittest` test discovery, which will find the tests in `tests` directory and run them all.

The tests make use of the `unittest.mock.patch` function to replace the `requests.get` function with a mock. This allows the tests to simulate HTTP responses from the API without making actual requests. Instead of receiving data from the API, the tests use locally stored "mock" data.

Each test in the suite exercises a different part of the SDK's functionality:

- `test_get_movies`: Tests the ability to retrieve a list of all movies.
- `test_get_movie`: Tests the ability to retrieve a single movie by its ID.
- `test_get_movies_with_budget_less_than_100`: Tests the ability to filter movies by budget.
- `test_get_movies_with_awards_greater_than_0`: Tests the ability to filter movies by the number of awards won.
- `test_get_movies_with_runtime_greater_than_or_equal_to_160`: Tests the ability to filter movies by runtime.
- `test_get_movies_by_sorting`: Tests the ability to sort movies by name.
- `test_get_movie_by_filtering`: Tests the ability to retrieve movies that match a certain name filter.
- `test_get_movie_quotes`: Tests the ability to retrieve quotes from a specific movie.
- `test_get_quotes`: Tests the ability to retrieve a list of all quotes.
- `test_get_quote`: Tests the ability to retrieve a single quote by its ID.
- `test_get_quotes_by_pagination`: Tests the ability to paginate through a list of quotes.

Please note that you will need to replace the `api_key` placeholder in the tests with your actual API key. Remember to keep your API key secure and not to publish it in public repositories.

---

Remember to replace any specific details (like file paths or directory names) with those that are accurate for this SDK.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This SDK is licensed under the MIT License.