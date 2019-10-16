# TDT4113 project 6 - Robot [![Actions Status](https://github.com/LudvigHz/plab2-robot/workflows/Robot%20action/badge.svg)](https://github.com/ludvighz/plab2-robot/actions)
> Repo for TDT4113 zumo robot assignment 2019

## Development
- ### Setup environment
  You need the `venv` python package installed
  ```sh
  python3 -m venv venv
  source venv/bin/activate
  pip install -r requirements.txt
  ```
- ### Codestyle
  We use pylint, and require a score of 8.0 or higher. Test with `pylint keypad`
  Formatting uses `black`. Format with `black keypad`

- ### Testing
  The project uses `unittest` for testing. Test with `python -m unittest` to run all tests.
