def who_sold_what(file):

    """Generate sales report showing total melons each salesperson sold."""

    report_dict = {}

    with open(file) as f:
        for line in f:
            line = line.rstrip()
            name, total, melons_sold = line.split('|')

            if name in report_dict:
                report_dict[name] += int(melons_sold)
            else:
                report_dict[name] = int(melons_sold)
    return report_dict
who_sold_what('sales-report.txt')


def print_report(melons_sold_by):
    """Print a report of salespeople and the total # of melons sold"""
    for name, melons_sold in melons_sold_by.items():
        print(f'{name} sold {melons_sold} melons')
print_report(who_sold_what('sales-report.txt'))
