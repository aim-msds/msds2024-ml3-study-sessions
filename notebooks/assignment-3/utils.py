"""Utility functions for the assignment 3 solution key"""

import matplotlib.pyplot as plt


def plot_history(history, metric='mae'):
    loss = history.history[metric]
    val_loss = history.history[f'val_{metric}']
    epochs = range(1, len(loss) + 1)

    fig, ax = plt.subplots()

    ax.plot(epochs, loss, 'o', color='tab:blue', label=f'Training {metric.title()}')
    ax.plot(epochs, val_loss, color='tab:blue', label=f'Validation {metric.title()}')
    ax.legend(bbox_to_anchor=(1., 1.))
    ax.set_xlabel("Epoch")
    ax.set_ylabel("Mean Absolute Error")

    return fig, ax


def plot_predictions(actual, predicted, dates):
    fig, ax = plt.subplots()
    ax.plot(dates, actual, color='tab:blue', label='Actual')
    ax.plot(dates, predicted, color='tab:orange', label='Predicted')

    ax.legend(bbox_to_anchor=(1., 1.))
    ax.set_xlabel("Dates")
    ax.set_ylabel("Daily Consumption (MWh)")

    return fig, ax
