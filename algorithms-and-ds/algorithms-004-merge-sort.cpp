/* 
 * algorithms-004-merge-sort.cpp
 * ds-algo-interview-cookbook
 *
 * Sort an array using the merge sort algorithm
 * 
 * Created by Ravi Vats on 08/03/20.
*/
#include <iostream>
using namespace std;

void merge(int arr[], int l, int mid, int r) {
    int size_l = mid - l + 1;
    int size_r = r - (mid + 1) + 1;
    int i, j, k;

    // defining temp arrays
    int leftArr[size_l], rightArr[size_r];

    // copying data to temp arrays
    for (i = 0; i < size_l; i++) {
        leftArr[i] = arr[l + i];
    }

    for (i = 0; i < size_r; i++) {
        rightArr[i] = arr[mid + 1 + i];
    }

    i = 0, j = 0, k = l;
    for (; i < size_l && j < size_r; k++) {
        if (leftArr[i] <= rightArr[j]) {
            arr[k] = leftArr[i];
            i++;
        } else {
            arr[k] = rightArr[j];
            j++;
        }
    }
    while (i < size_l) {
        arr[k] = leftArr[i];
        i++;
        k++;
    }
    while (j < size_r) {
        arr[k] = rightArr[j];
        j++;
        k++;
    }
}

void mergeSort(int arr[], int l, int r) {
    // base condition check
    if (l >= r)
        return;

    // mid calculated like this to avoid overflow error due to summation of (l + r)
    // in the formula mid = (l + r) / 2
    int mid = l + (r - l) / 2;
    mergeSort(arr, l, mid);
    mergeSort(arr, mid + 1, r);
    merge(arr, l, mid, r);
}

int main() {
    int arr[10] = {2, 3, 4, 5, 1, 6, 9, 7, 10, 8};
    int l = sizeof(arr) / sizeof(arr[0]);
    mergeSort(arr, 0, l - 1);
    cout << "Sorted array is: \n";
    for (int i = 0; i < l; i++) {
        cout << arr[i] << "\t";
    }
    cout << "\n";
}
