import os
import matplotlib.pyplot as plt
from datetime import datetime

FILE_PATH = os.path.join(os.path.dirname(__file__),
                         "2022_january_expenses.txt")


def tableGeneration():
    '''Generates a list of list from the text file, being each of them a row of
    the imported table, it splits its content base on tab division.
    '''

    data_table = []
    with open(FILE_PATH, "r") as file:
        while line := file.readline():
            data_table.append(line.strip().split("\t"))
    return data_table


def getValues(table, column_numbers):
    '''From the given table return the selected columns as a new list of list
    being this ones rows of the new table.
    '''

    if type(column_numbers) != list:
        column_numbers = [column_numbers]
    rows_number = len(table)
    result_table = []
    for row in range(rows_number):
        row_val = []
        for column in range(len(column_numbers)):
            row_val.append(table[row][column_numbers[column]])
        result_table.append(row_val)
    return result_table


def getProcessedData(raw_table):
    '''From the given table, get unique values of the key elements in a
    dictionary, then adds the values of the list that have the same key.
    '''

    unique_labels = dict.fromkeys(set([row[1] for row in raw_table]), 0)
    for row in raw_table:
        row[0] = float(row[0].replace(",", "."))
        unique_labels[row[1]] = unique_labels[row[1]] + row[0]
    return unique_labels


def crtPieChart(axs, numbers, categories, row, column):
    '''Creates the pie obj with its position on the grid.'''

    axs[row, column].pie(numbers, labels=categories, autopct='%1.1f%%',
                         textprops={'size': 'smaller'})
    axs[row, column].axis('equal')


def crtPlotChart(axs, numbers, categories, row, column):
    '''Creates the pie obj with its position on the grid.'''

    axs[row, column].plot(categories, numbers)
    axs[row, column].set_xticklabels(categories, rotation=45, fontsize=5)


def crtBarChart(axs, numbers, categories, row, column):
    '''Creates the pie obj with its position on the grid.'''

    axs[row, column].bar(categories, numbers)
    axs[row, column].set_xticklabels(categories, rotation=15, fontsize=5)


def main():
    '''Executes main function'''

    data_table = tableGeneration()
    category_filter_table = getValues(data_table, [5, 6])
    company_filter_table = getValues(data_table, [5, 2])
    date_filter_table = getValues(data_table, [5, 1])
    account_filter_table = getValues(data_table, [5, 4])
    category_dict = getProcessedData(category_filter_table)
    company_dict = getProcessedData(company_filter_table)
    date_dict = getProcessedData(date_filter_table)
    date_dict = dict(sorted(date_dict.items(),
                            key=lambda date: datetime.strptime(date[0],
                                                               '%d/%m/%Y')))
    account_dict = getProcessedData(account_filter_table)

    fig, axs = plt.subplots(2, 2, figsize=(12, 10))
    crtPieChart(axs, list(category_dict.values()),
                list(category_dict.keys()), 0, 0)
    crtPieChart(axs, list(company_dict.values()),
                list(company_dict.keys()), 0, 1)
    crtPlotChart(axs, list(date_dict.values()),
                 list(date_dict.keys()), 1, 0)
    crtBarChart(axs, list(account_dict.values()),
                list(account_dict.keys()), 1, 1)

    plt.show()


if __name__ == "__main__":
    main()
