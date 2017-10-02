# pydocket

Python library for the [Regulations.gov API](https://regulationsgov.github.io/developers/index.html).

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

Python 3 (not tested on Python 2)

You'll need to [acquire a Data.gov API Key](https://api.data.gov/signup/) to perform queries.

### Installing

Clone, create a Python 3 virtual environment, and install requirements.

```
git clone https://github.com/gregoryfoster/pydocket.git
cd pydocket
virtualenv -p $(which python3) .venv
source .venv/bin/activate
pip install requirements.txt
```

### Usage

Export your Data.gov API key in your development environment to perform queries:

```
export DATA_GOV_API_KEY=[your_api_key_here]
```

See the [`tests`](tests) and [`download.py`](download.py) for examples of usage.

## Running the tests

Uses `pytest` fixtures and `VCR`.

```
cd tests
python test_pydocket.py
```

## Deployment

Not yet on PyPI, so deploy using [`pip`'s VCS support](https://pip.pypa.io/en/stable/reference/pip_install/#vcs-support):

```
mkdir your_project
cd your_project
virtualenv -p $(which python3) .venv
source .venv/bin/activate
pip install git+https://github.com/gregoryfoster/pydocket.git
```

## Built With

* [requests](http://docs.python-requests.org/en/master/) - HTTP for humans by [@kennethreitz](https://github.com/kennethreitz)

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. Releases are documented as [tags on this repository](https://github.com/gregoryfoster/pydocket/tags).

## Authors

* **Gregory Foster** - *Initial work* - [@gregoryfoster](https://github.com/gregoryfoster)

See also the list of [contributors](https://github.com/gregoryfoster/pydocket/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

## Acknowledgments

* Initial development follows [@kevgathuku's](https://github.com/kevgathuku) article ["Building and Testing an API Wrapper in Python"](https://semaphoreci.com/community/tutorials/building-and-testing-an-api-wrapper-in-python)
