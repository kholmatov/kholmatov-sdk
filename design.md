# Design of the Lord of the Rings SDK

The Lord of the Rings SDK is designed to provide an easy and intuitive way to interact with The One API. The design is focused on simplifying the process of making requests and handling responses for the end user.

## Architecture

The SDK is designed around a central `Client` class, which manages all interactions with the API. This class provides methods for making requests to various endpoints, such as `get_movies`, `get_movie`, `get_movie_quotes`, `get_quotes`, and `get_quote`. 

These methods accept a variety of arguments, allowing users to specify query parameters in a simple and intuitive way. For example, users can pass in filters as keyword arguments, which are automatically converted into the appropriate query string.

## Error Handling

The SDK uses the `requests` library's built-in functionality to raise exceptions for HTTP errors. This makes it easy for users to handle errors in a try/except block.

## Pagination, Sorting, and Filtering

The SDK supports pagination, sorting, and filtering options for making requests. This is done by passing in these options as keyword arguments to the `get_movies` or `get_quotes` methods.

## Testing

The SDK includes a suite of unit tests, which mock the API responses using the `requests_mock` library. This allows us to test the functionality of the SDK without making actual requests to the API.

## Documentation

All methods in the `Client` class are documented with docstrings, providing information on the method's purpose, its arguments, and its return value. These docstrings follow the Google Python Style Guide.

The SDK also includes a README file, which provides a high-level overview of the SDK's functionality, as well as examples of how to use each method.

## Future Improvements

As the API evolves, the SDK will be updated to include new endpoints and features. Feedback from users will also be incorporated to improve the SDK's usability and functionality.
