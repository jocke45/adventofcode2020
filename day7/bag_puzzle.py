def rule_spliter(bag_rule):
    return bag_rule.replace(" bags", "").replace(" bag", "").split(" contain ")


def rule_value_spliter(contain_rule):
    return contain_rule.replace(".", "").split(", ")


def bag_puzzle(bag_rules):
    bag_rule_handler(bag_rules)


def bag_rule_handler(bag_rules):
    rules = {key: rule_value_spliter(val) for key, val in dict(
        map(rule_spliter, bag_rules)).items()}
    print(rules)
