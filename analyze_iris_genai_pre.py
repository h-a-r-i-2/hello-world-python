import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def load_dataset(csv_path):
    df = pd.read_csv(csv_path)
    print("CSV file loaded successfully!")
    print(df.head())
    return df

def compute_mean(df):
    means = df.mean(numeric_only = True)
    print("The column wise mean is", means)
    
def plot_histogram(df, output_dir="plots"):
    """Plots histogram for each numeric column."""
    os.makedirs(output_dir, exist_ok=True)
    numeric_cols = df.select_dtypes(include='number').columns
    
    for col in numeric_cols:
        plt.figure(figsize=(6, 4))
        sns.histplot(df[col], kde=True, bins=20)
        plt.title(f"Histogram of {col}")
        plt.xlabel(col)
        plt.ylabel("Frequency")
        plot_path = f"{output_dir}/{col}_histogram.png"
        plt.savefig(plot_path)
        plt.close()
        print(f"📈 Saved histogram: {plot_path}")

def main():
    csv_path = "iris.csv"
    
    df = load_dataset(csv_path)
    compute_mean(df)
    plot_histogram(df)
    
if __name__ == "__main__":
    main()