import argparse
from app.cleaner import load_data, save_data, clean_data, plot_column_frequency

def main():
 parser = argparse.ArgumentParser(description="CLI tool for cleaning Excel/CSV data.")
 parser.add_argument('input_file', help="Path to the input Excel/CSV file.")
 parser.add_argument('output_file', help="Path to the output cleaned Excel/CSV file.")
 parser.add_argument('--remove_duplicates', action='store_true', help="Remove duplicate rows from the dataset.")
 parser.add_argument('--regex_clean', type=str, help="Regex pattern to clean the data (e.g., remove commas, dots, etc.).")
 parser.add_argument('--plot_freq', type=str, help="Column name to plot frequency of values.")
 parser.add_argument('--output_dir', type=str, default='.', help="Directory to save the output frequency plot.")
 
 args = parser.parse_args()

 data = load_data(args.input_file)

 if args.remove_duplicates or args.regex_clean:
     data = clean_data(data, args.regex_clean)

 save_data(data, args.output_file)

 if args.plot_freq:
     plot_file = plot_column_frequency(data, args.plot_freq, args.output_dir)
     print(f"Frequency plot saved at: {plot_file}")

if __name__ == "__main__":
 main()
