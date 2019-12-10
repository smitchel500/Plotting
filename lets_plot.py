# lets_plot.py

import linePlot

QUIT = 'q'

if __name__ == '__main__':
    choice = ''
    while choice != QUIT:
        choice = input("Single (1), Double (2), or Quit (q): ")
        if choice == QUIT:
            break
        if int(choice) == 1:
            filename1 = input("Enter file name: ")
        else:
            filename1 = input("Enter 1st file name: ")
            filename2 = input("Enter 2nd file name: ")
        xlabel = input("Enter X-axis label: ")
        ylabel = input("Enter Y-axis label: ")
        if int(choice) == 1:
            legend1 = input("Enter legend: ")
            linePlot.singleLinePlot(filename1, xlabel, ylabel, legend1)
        else:
            legend1 = input("Enter 1st legend: ")
            legend2 = input("Enter 2nd legend: ")
            linePlot.doubleLinePlot(filename1, filename2, xlabel, ylabel, legend1, legend2)
