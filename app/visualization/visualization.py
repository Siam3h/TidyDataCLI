import pandas as pd
import matplotlib.pyplot as plt
import os
class Visualisation:
    def plot_frequency(self, column_name, output_dir):
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        freq = self.df[column_name].value_counts()
        freq.plot(kind='bar')
        plt.title(f'Frequency of {column_name}')
        plt.xlabel(column_name)
        plt.ylabel('Count')
        plt.savefig(os.path.join(output_dir, f'{column_name}_frequency.png'))
        plt.close()