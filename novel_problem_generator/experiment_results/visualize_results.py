import pandas as pd
import matplotlib.pyplot as plt


def load_data(file_path):
    return pd.read_csv(file_path)


def process_data(df, desired_columns):
    return df[desired_columns]


def calculate_group_averages(df):
    return df.groupby("Group").mean()


def plot_group_averages(group_avg, output_file):
    plt.figure(figsize=(12, 8))

    metrics = ["Sensibleness", "Clarity", "Novelty", "Difficulty"]
    colors = ["blue", "green", "orange", "red"]

    for i, (metric, color) in enumerate(zip(metrics, colors), 1):
        plt.subplot(2, 2, i)
        group_avg[metric].plot(kind="bar", color=color)
        plt.title(f"Average {metric} by Group")
        plt.ylabel(metric)
        plt.xlabel("Group")
        plt.ylim(0, 5)
        plt.xticks(rotation=45)

    plt.tight_layout()
    plt.savefig(output_file)
    plt.close()


def calculate_success_percentage(df):
    df["Successful"] = (
        (df["Novelty"] > 3)
        & (df["Sensibleness"] > 2)
        & (df["Clarity"] > 2)
        & (df["Difficulty"] >= 2)
    )
    return df.groupby("Group")["Successful"].mean() * 100


def plot_success_percentage(group_success_pct, output_file):
    plt.figure(figsize=(8, 6))
    group_success_pct.plot(kind="bar", color="purple")
    plt.title("Percentage of Successful Tasks by Group")
    plt.ylabel("Percentage (%)")
    plt.xlabel("Group")
    plt.xticks(rotation=45)
    plt.ylim(0, 100)
    plt.tight_layout()
    plt.savefig(output_file)
    plt.close()


def main():
    file_path = "evaluations.csv"
    desired_columns = [
        "Group",
        "TaskNumber",
        "Sensibleness",
        "Clarity",
        "Novelty",
        "Difficulty",
    ]

    df = load_data(file_path)
    df = process_data(df, desired_columns)

    group_avg = calculate_group_averages(df)
    plot_group_averages(group_avg, "avg_tasks_by_group.png")

    group_success_pct = calculate_success_percentage(df)
    plot_success_percentage(group_success_pct, "successful_tasks_by_group.png")


if __name__ == "__main__":
    main()
