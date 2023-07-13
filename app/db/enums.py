from enum import Enum


class SourceApp(str, Enum):
    JIRA_ALIGN = "JIRA-ALIGN"


class ActionType(str, Enum):
    AGILITY_PLAN = "AGILITY_PLAN"
    PLAYBOOK = "PLAYBOOK"
    JOB = "JOB"
    OBJECTIVE = "OBJECTIVE"
    COURSE = "COURSE"
    ASSESSMENT = "ASSESSMENT"
    MENTORING = "MENTORING"
    PLAY = "PLAY"
    NONE = ""


class ActionStatus(str, Enum):
    INITIAL = "INITIAL"
    STARTED = "STARTED"
    BLOCKED = "BLOCKED"
    COMPLETED = "COMPLETED"


class ResourceType(str, Enum):
    TEAM = "TEAM"
    ROLE = "ROLE"
    USER = "USER"
    PORTFOLIO = "PORTFOLIO"
    PROGRAM = "PROGRAM"
    SPRINT = "SPRINT"
    RELEASE = "RELEASE"
    TEAMPRO = "TEAMPRO"


class ResourceUrl(str, Enum):
    USER = "Users?expand=true"
    ROLE = "systemroles"
    PORTFOLIO = "Portfolios"
    PROGRAM = "Programs"
    TEAM = "Teams"
    SPRINT = "Iterations"
    RELEASE = "Releases"
    TEAMPRO = "Teams"


class OrganizationType(str, Enum):
    """
    NOTE: Remember to update the "organization_type_enum" enum in the database as well
    if you add a new organization type here. Ref: app/alembic/versions/9e07696e059f_create_play_table.py
    """

    PORTFOLIO = "PORTFOLIO"
    PROGRAM = "PROGRAM"
    TEAM = "TEAM"


class MetricsType(str, Enum):
    PERCENTAGE = "PERCENTAGE"
    DOLLARS = "DOLLARS"
    UNITS = "UNITS"


class AgilityPlanRelationType(str, Enum):
    ACTION = "ACTION"
    OBJECTIVE = "OBJECTIVE"
    USER = "USER"
    ROLE = "ROLE"
    LEAD = "LEAD"
    SPONSOR = "SPONSOR"
    CORETEAM = "CORETEAM"
    COACH = "COACH"
    ORGANIZATION = "ORGANIZATION"
