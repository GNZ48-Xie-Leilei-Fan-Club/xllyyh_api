# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.2.0] 2019-08-25
### Added
- Added dependencies
  - Pin `django` to ~=2.1.7
  - `django-extensions`
  - `requests`
  - `django-celery-beat`
  - `redis`
  - `ipdb`
  - `django-model-utils`
  - `django-cors-headers`
  - `pymysql`
  - `django-filter`
  - `gunicorn`
  - `pillow`
  - `sentry-sdk`
- Added celery for scheduling tasks
  - Added tasks for fetching modian campaign statuses and orders
- Added models
  - `api/models/battle.py`
    - `BattleCampaign`
    - `BattleGroup`
    - `BattleNotification`
  - `api/models/campaign.py`
    - `Campaign`
    - `Order`
  - `api/models/card.py`
    - `CardSet`
    - `Card`
    - `Rarity`
    - `CardUserAssociation`
  - `api/models/event_notice.py`
    - `NewMemberNotice`
  - `api/models/monitor.py`
    - `MonitorCampaign`
    - `MonitorMember`
  - `api/models/transaction.py`
    - `Transaction`
    - `DrawTransaction`
    - `CardTransactionAssociation`
  - `api/models/user.py`
    - `FanClubUser`
    - `ModianUser`
- Added new endpoints
  - Endpoint for chatbot to know what notices to send to new members
    - `/chatbot/new_member_notices`
  - Endpoint for battle related functionalities
    - Datav related endpoints
      - `/battle/individual`
      - `/battle/group`
      - `/battle/notification`
      - `/battle/monitor`
    - Chatbot related endpoints
      - `/battle/total_ranking`
      - `/battle/battle_broadcast`
- Make use of sentry as to log errors and exceptions


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