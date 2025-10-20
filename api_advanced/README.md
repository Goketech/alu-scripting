
API Advanced - Exercises
=========================

This folder contains small Python scripts that interact with the Reddit JSON API to fetch information about subreddits and their hot posts. Each exercise consists of a "driver" script (named like `N-main.py`) which imports and calls the functionality implemented in the companion module(s).

Files
-----

- `0-subs.py` — number_of_subscribers(subreddit)
	- Returns the number of subscribers for the given subreddit using the endpoint `/r/{subreddit}/about.json`.
	- Usage example (from command line):
		- `./0-main.py <subreddit>` prints the number of subscribers.

- `0-main.py` — simple driver for `0-subs.py`
	- Imports `number_of_subscribers` and prints the result for the subreddit provided as the first command-line argument.

- `1-top_ten.py` — top_ten(subreddit)
	- Fetches and prints the titles of the first 10 hot posts for the given subreddit using `/r/{subreddit}/hot.json?limit=10`.
	- Prints `None` on error.
	- Usage example: `./1-main.py <subreddit>`

- `1-main.py` — driver for `1-top_ten.py`

- `2-recurse.py` — recurse(subreddit, hot_list=[], after="")
	- Recursively fetches up to all hot posts (pagination) for a subreddit, returning a list of titles.
	- Uses the `after` parameter and requests with `limit=100` to page through results.
	- Usage example: `./2-main.py <subreddit>` prints the number of titles returned.

- `2-main.py` — driver for `2-recurse.py`

- `3-count.py` — count_words(subreddit, word_list=[], hot_list=[], after="")
	- Recursively fetches hot post titles (like `2-recurse`) and counts occurrences of words provided in `word_list`.
	- Prints counts sorted by descending frequency then alphabetically.
	- Usage example: `./3-main.py <subreddit> "word1 word2 word3"`

- `3-main.py` — driver for `3-count.py`

Notes and assumptions
---------------------

- These scripts use the `requests` library and set a `User-Agent` header. Run them in an environment where `requests` is installed.
- They are small exercise scripts and perform basic error handling by catching broad exceptions and returning `None` or `0` in error cases. Consider improving error handling and response status checks for production use.

How to run
----------

Make the driver executable (if needed) and run it with the subreddit name and any additional arguments required by the specific exercise.

Example:

```bash
chmod +x 0-main.py && ./0-main.py programming
python3 1-main.py programming
python3 3-main.py programming "python javascript" 
```
