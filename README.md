# Top Errors Script

This is a Python-based CLI tool that helps in analyzing and identifying the most common errors occurring in your server logs. The script reads a given PHP error_log file, finds PHP error message, counts their occurrence and sorts them by frequency. The top 10 most common errors are then written into a CSV file and displayed on the screen.

## Usage:

```
# minimal
python top-errors.py <log_file>

# practical - uses https://github.com/Textualize/rich-cli
grep "2024" php_errors.log > 2024.log
python top-errors.py 2024.log | rich - --csv

CSV file '2024.log.csv' has been generated successfully.
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━┓
┃ Error                                                                                                                                                       ┃ Count ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━┩
│ PHP Warning:  date_create_from_format() expects parameter 2 to be string, array given in                                                                    │    77 │
│ /xxxx/xxxxxxxx/xxx/xxxxxx-xxxx/xxxxxxxxxxx/xxxxxxxxxxxxxxxxxx/xxxxxx-core/inc/classes/objects/class-event.php on line 97                                    │       │
│ PHP Fatal error:  Uncaught Exception: Post not correct post type: post expected. in                                                                         │    23 │
│ /xxxx/xxxxxxxx/xxx/xxxxxx-xxxx/xxxxxxxxxxx/xxxxxxxxxxxxxxxxxx/xxxxxx-core/inc/classes/objects/class-post.php:28                                             │       │
│ PHP Fatal error:  require(): Failed opening required '/xxxx/xxxxxxxx/xxx/xxxxxx-xxxx/xxxxxxxxxxx/wordpress/wp-blog-header.php'                              │    19 │
│ (include_path='.:/usr/local/php74/pear') in /xxxx/xxxxxxxx/xxx/xxxxxx-xxxx/xxxxxxxxxxx/index.php on line 17                                                 │       │
│ PHP Warning:  strpos(): Empty needle in /xxxx/xxxxxxxx/xxx/xxxxxx-xxxx/xxxxxxxxxxx/xxxxxxxxxxxxxxxxxx/xxxxxxxxx/inc/class-widget.php on line 106            │    12 │
│ PHP Warning:  Creating default object from empty value in /xxxx/xxxxxxxx/xxx/xxxxxx-xxxx/xxxxxxxxxxx/wordpress/wp-includes/nav-menu-template.php on line    │     5 │
│ 394                                                                                                                                                         │       │
│ PHP Warning:  require_once(/xxxx/xxxxxxxx/xxx/xxxxxx-xxxx/xxxxxxxxxxx/xxxxxxxxxxxxxxxxxx/query-monitor/query-monitor.php): failed to open stream: No such   │     4 │
│ file or directory in /xxxx/xxxxxxxx/xxx/xxxxxx-xxxx/xxxxxxxxxxx/xxxxxxxxxxxxxxxxxx/mu-loader.php on line 74                                                 │       │
│ PHP Fatal error:  require_once(): Failed opening required '/xxxx/xxxxxxxx/xxx/xxxxxx-xxxx/xxxxxxxxxxx/xxxxxxxxxxxxxxxxxx/query-monitor/query-monitor.php'   │     4 │
└─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┴───────┘
```

The script takes in one argument:
- `<log_file>`: Path to the log file which you want to analyze.

## Functionality:

- The script reads the log file and filters out entries that are PHP error messages.
- The occurrences of each unique error are counted using the Counter class from the Python's collections module.
- The errors are then sorted by their count in descending order.
- Only the top 10 most common errors are kept.
- The script outputs two items:
  - A CSV file records the most common errors and their count.
  - Print statements that indicate the error messages and their counts respectively.

## Code Explanation:

The code mainly consists of a main function and two helper functions. The helper functions are:

- `filter_entries(entry)`: This function is responsible for extracting the PHP error messages from the log entries.

The main function, `main()`, does the bulk of work which includes reading the file, using helper functions, creating a counter for PHP error messages, sorting them and writing to a CSV.

## Limitations and Considerations:

- The script currently only processes PHP error log files.
- Please make sure proper permissions are given to access and read the log file.

## Requirements

- Python 3.12.3 (earlier might work -- AI thinks it requires Python 3.6 or newer to run correctly.)
- Access to the log files to be analyzed.

## Improvements &amp; Contribution:

This script is basic and serves a simple functionality. However, there's always room for improvement.
A few possible features could be added, like handling different log formats and errors from sources other than PHP, or expanding the time window for log review. Any suggestions or contributions are welcome!
