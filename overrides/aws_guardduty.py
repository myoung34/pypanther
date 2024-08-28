from pypanther import LogType
from pypanther.wrap import exclude, include


def guard_duty_discovery_filter(event):
    """Uses GuardDuty findings to check if the finding starts with Discovery."""
    return event.get("type").startswith("Discovery")


def apply_overrides(rules):
    for rule in rules:
        if LogType.AWS_GUARDDUTY in rule.log_types:
            exclude(guard_duty_discovery_filter)(rule)