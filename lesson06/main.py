from list_average import AverageGenerator, AverageComparator

if __name__ == '__main__':
    print(avg1 := AverageGenerator(5, 1, 100))
    print(avg2 := AverageGenerator(5, 1, 100))
    print(AverageComparator.avg_compare(avg1.average, avg2.average))
    print(AverageComparator.avg_compare(avg2.average, avg1.average))
    print(AverageComparator.avg_compare(avg1.average, avg1.average))
    arr = [1, 2, 3, 4]
    arr2 = [4, 5, 6, 7]
    print()
    print(AverageComparator.avg_compare(arr, arr2))
    print(AverageComparator.avg_compare(arr2, arr))
    print(AverageComparator.avg_compare(arr, arr))