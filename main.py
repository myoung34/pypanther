from pypanther import get_rules, register

import rules
from overrides import aws_guardduty

rules = get_rules(module=rules)
aws_guardduty.apply_overrides(rules)

register(rules)
