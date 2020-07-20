def imp():


def plot_just_scores(pd_df, ax):
    # Takes axis and pd_df of test data and plots all 
    # the scores regardless of wins or loss.
    ax.hist(pd_df['score'], bins=100, range=(0, 1500))
    ax.set_yticklabels('')