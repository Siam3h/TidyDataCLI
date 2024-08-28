import argparse
from ..reporting import generate_report

def reporting_command(subparsers):
    parser = subparsers.add_parser('report', help="Generate a report")
    parser.add_argument('input', type=str, help="Input file path")
    parser.add_argument('output', type=str, help="Output file path")
    
    parser.set_defaults(func=report_command)

def report_command(args):
    report = generate_report(args.input)
    with open(args.output, 'w') as f:
        f.write(report)
    print(f"Report saved to {args.output}")
