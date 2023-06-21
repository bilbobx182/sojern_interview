## Repo Structure
```
-/ tracking_api
    --/requirements.txt
-/ util_cli
-/ tests
```

## Code
The code was run and validated against version Python 3.8.2
If you don't have a compatible you can use [pyenv](https://github.com/pyenv/pyenv)

### Utils
Question 1 of the assignment:
Utils uses all default python modules
```
python3 util_cli/app.py --version1 2.0 --version2 1.0
1
```

### Tracking API
Question 3 of the assignment
run `pip3 install -r tracking_api/requirements.txt` before trying to execute the API.
Can be run by the following command. `python3 tracking_api/app.py `
Uses uvicorn / FASTAPI.
Workers, host, and port are configured by environment variables. `sojernworkers`,`sojernport`,`sojernhost` respectively.

Ideally if scale is a concern :
- Put the API behind a load balancer to distribute work.
- We would scale horizontally for this kind of API.
- Requirements on how frequently the file contents changes would help define cache strategy.
- We would also use an external cache rather than application lru cache.

#### Example startup
```
INFO:     Will watch for changes in these directories: ['/Users/ciarannolan/PycharmProjects/sojern']
WARNING:  "workers" flag is ignored when reloading is enabled.
INFO:     Uvicorn running on http://0.0.0.0:9008 (Press CTRL+C to quit)
INFO:     Started reloader process [15577] using StatReload
```


## Tests
To run tests, run the following command from the top level directory
Currently we have typical unit tests for the utils, and some integration for the API.

`python3 -m unittest discover -v`
An example is
```
(venv) ➜  sojern python3 -m unittest discover -v                  
test_image_200 (tests.test_integration_tracking_api.TestAPI)
Test to validate that the gif is returned. ... ok
test_no_file (tests.test_integration_tracking_api.TestAPI) ... ok
test_ping_200 (tests.test_integration_tracking_api.TestAPI)
Test to validate that the ping returns 200 when the file is there. ... ok
test_ping_503 (tests.test_integration_tracking_api.TestAPI)
Test to validate that the ping returns 200 when the file is there. ... ok
test_random_fails (tests.test_integration_tracking_api.TestAPI)
Test to validating unknown endpoints return 404 ... ok
test_basic_bad_path (tests.test_util_cli.TestUtilCLI)
Test alphanumeric edge cases ... ok
test_edge_case_versions_same (tests.test_util_cli.TestUtilCLI)
Test same version returns 0 ... ok
test_happy_path_returns_1 (tests.test_util_cli.TestUtilCLI)
Test happy path returns 1 ... ok
test_happy_path_validate_versions_double (tests.test_util_cli.TestUtilCLI)
Test that longer version comparisons don't trip it up. ... ok
test_happy_path_validate_versions_single (tests.test_util_cli.TestUtilCLI)
Test normal path of versions being passed in. ... ok


```