""" This is a set of test rules for GuardDuty """
from typing import Dict

from pypanther import LogType, Rule, RuleTest, Severity

from helpers.misc import load_json_file

guard_duty_tests = [
    RuleTest(
        name="Guardduty severity is too high",
        expected_result=True,
        expected_alert_context={
            "description": "UnauthorizedAccess:EC2/TorClient",
            "mitre_technique": "Endpoint Denial of Service",
            "mitre_tactic": "Impact",
        },
        log=load_json_file("example_logs/guardduty1.json"),
    ),
    RuleTest(
        name="Guardduty severity is too high",
        expected_result=True,
        expected_alert_context={
            "description": "CryptoCurrency:EC2/BitcoinTool.B",
            "mitre_technique": "Endpoint Denial of Service",
            "mitre_tactic": "Impact",
        },
        log=load_json_file("example_logs/guardduty2.json"),
    ),
    RuleTest(
        name="Guardduty: TOR client",
        expected_result=True,
        log=load_json_file("example_logs/guardduty1.json"),
    ),
    RuleTest(
        name="Guardduty: TOR client",
        expected_result=True,
        log=load_json_file("example_logs/guardduty2.json"),
    ),
]


class GuarddutyTest(Rule):
    """ This is a pypanther rule for GuardDuty """
    id = "AWS.GuardDuty.SeverityTooHigh"
    enabled = False
    log_types = [LogType.AWS_GUARDDUTY]
    default_severity = Severity.MEDIUM
    # 10 matches per minute
    threshold = 50
    dedup_period_minutes = 5
    default_description = "This rule is a test"
    reports = {"MITRE ATT&CK": ["TA0010:T1499"]}  # Impact: Endpoint Denial of Service
    default_runbook = (
        "Do Something"
    )
    tests = guard_duty_tests

    def rule(self, event) -> bool:
        """ The tests """
        return_val = False
        if event.get("Severity") < 8:
            return_val = True
        # Fail for any UnauthorizedAccess:EC2/TorClient
        if event.get("Type") == "UnauthorizedAccess:EC2/TorClient":
            return_val = False
        return return_val

    def title(self, event) -> str:
        """ No idea """
        return "This is a big ass test"

    def alert_context(self, event) -> Dict:
        """ no idea """
        return {
            "description": event.get("Type"),
            "mitre_technique": "Endpoint Denial of Service",
            "mitre_tactic": "Impact",
        }
