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

