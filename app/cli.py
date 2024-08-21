import argparse
from .cleaner import DataCleaner

def main():
    parser = argparse.ArgumentParser(description="TINYDATACLI: A tool for cleaning and analyzing data.")
    parser.add_argument('input', help="Input file path (CSV or Excel)")
    parser.add_argument('output', help="Output file path")
    parser.add_argument('--remove_duplicates', action='store_true', help="Remove duplicate rows")
    parser.add_argument('--regex_clean', type=str, help="Regex pattern to clean data")
    parser.add_argument('--plot_freq', type=str, help="Column name to plot frequency")
    parser.add_argument('--output_dir', type=str, help="Directory to save plots")

    args = parser.parse_args()
    cleaner = DataCleaner(args.input, args.output)

    if args.remove_duplicates:
        cleaner.remove_duplicates()
    if args.regex_clean:
        cleaner.regex_clean(args.regex_clean)
    if args.plot_freq:
        cleaner.plot_frequency(args.plot_freq, args.output_dir)

if __name__ == "__main__":
    main()
