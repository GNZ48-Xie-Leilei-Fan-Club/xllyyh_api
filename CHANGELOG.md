# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.0] 2019-03-16
### Added
- Added `README.md`
  - Added Overview section
- Added `.gitignore`
- Use `pipenv` for dependency management
  - Added `Pipfile` and `Pipfile.lock`
  - Added major dependencies
    - `django`
    - `django-rest_framework`
    - `djangorestframework-jsonapi`
- Added models and corresponding serializers and list views
    - `KeywordedResponse`
    - `IgnoreNumber`
- Added MIT license