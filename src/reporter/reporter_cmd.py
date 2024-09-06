import argparse
from .reporter import generate_report

def reporting_command(subparsers):
    """
    Adds a subcommand for generating a report.
    """
    parser = subparsers.add_parser('report', help="Generate a report")
    parser.add_argument('input', type=str, help="Input file path")
    parser.add_argument('output', type=str, help="Output file path")
    parser.add_argument('--format', type=str, choices=['txt', 'pdf'], default='txt', help="Output format ('txt' or 'pdf')")

    parser.set_defaults(func=report_command)

def report_command(args):
    """
    Handles the command to generate a report.
    """
    try:
        report = generate_report(args.input, output_format=args.format)
        with open(args.output, 'w' if args.format == 'txt' else 'wb') as f:
            if args.format == 'txt':
                f.write(report)
            print(f"Report saved to {args.output}")
    except Exception as e:
        print(f"Error generating report: {e}")
