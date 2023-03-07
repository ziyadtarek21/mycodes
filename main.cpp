#include <bits/stdc++.h>
using namespace std;

//selction sort
//    for(int i=0;i<arr_size-1;i++){
//        int min=i;
//    for(int j=i+1;j<arr_size;j++){
//    if(arr[j]<arr[min]){
//        min=j;
//    }
//}
//    swap(arr[i],arr[min]);
//}

// insertion sort
//    for (int i = 1, j; i < arr_size; i++)
//    {
//        int tmp = arr [i];
//        for (j = i; j > 0 && tmp < arr [j-1]; j--)
//            arr [j] = arr [j - 1];
//        arr [j] = tmp;
//    }


//bubble sort
//for(int i=1;i<arr_size;i++){
//        for(int j=0;j<arr_size-1;j++){
//
//            if(arr[j]>arr[j+1]){
//                swap(arr[j],arr[j+1]);
//            }
//        }
//    }


//////////////////////mrege sort/////////////////////////////////////
void merge(int array[], int const left, int const mid,
           int const right)
{
    int ArrOne = mid - left + 1;
    int ArrTwo = right - mid;

    // Create temp arrays
    int leftArray [ArrOne];
    int rightArray[ArrTwo];


    // Copy data to temp arrays leftArray[] and rightArray[]
    for (int i = 0; i < ArrOne; i++)
        leftArray[i] = array[left + i];
    for (int j = 0; j < ArrTwo; j++)
        rightArray[j] = array[mid + 1 + j];


    int indexOfSubArrayOne= 0, // Initial index of first sub-array
    indexOfSubArrayTwo= 0; // Initial index of second sub-array
    int indexOfMergedArray= left; // Initial index of merged array

    // Merge the temp arrays back into array[left..right]
    while (indexOfSubArrayOne < ArrOne && indexOfSubArrayTwo < ArrTwo) {
        if (leftArray[indexOfSubArrayOne] <= rightArray[indexOfSubArrayTwo]) {
            array[indexOfMergedArray]
                    = leftArray[indexOfSubArrayOne];
            indexOfSubArrayOne++;
        }
        else {
            array[indexOfMergedArray]
                    = rightArray[indexOfSubArrayTwo];
            indexOfSubArrayTwo++;
        }
        indexOfMergedArray++;
    }
    // Copy the remaining elements of
    // left[], if there are any
    while (indexOfSubArrayOne < ArrOne) {
        array[indexOfMergedArray]
                = leftArray[indexOfSubArrayOne];
        indexOfSubArrayOne++;
        indexOfMergedArray++;
    }
    // Copy the remaining elements of
    // right[], if there are any
    while (indexOfSubArrayTwo < ArrTwo) {
        array[indexOfMergedArray]
                = rightArray[indexOfSubArrayTwo];
        indexOfSubArrayTwo++;
        indexOfMergedArray++;
    }
}



void mergeSort(int array[], int const begin, int const end)
{
    if (begin >= end)
        return; // Returns recursively

    int mid = begin + (end - begin) / 2;
    mergeSort(array, begin, mid);
    mergeSort(array, mid + 1, end);
    merge(array, begin, mid, end);
}

void printArray(int A[], int size)
{
    for (auto i = 0; i < size; i++)
        cout << A[i] << " ";
}
////////////////////////////////////////////////////////////////////////////////////////

///////////////////////quick sort//////////////////////////////////////////////////////

int partition(int arr [],int left , int right)
{
    int pivote = arr[left];
    int i = left;  // this is the first element position as we assume it is the pivote
    for (int j = left + 1 ; j <= right ; j++)
    {
        if (arr[j] < pivote)
        {
            i++;
            swap(arr[i] , arr[j]);
        }
    }
    swap(arr[i] , arr[left]);
    return i;
}


void quicksort(int arr[] , int left , int right)
{
    if (left >= right)
    {
        return;
    }
    else
    {
        int mid = partition(arr , left , right);
        quicksort(arr , left , mid - 1);
        quicksort(arr , mid + 1 , right);
    }
}
/////////////////////////////////////////////////////////////////////////////////////////////////
int main() {
    int arr[] = { 12, 11, 13, 5, 6, 7 };
    auto arr_size = sizeof(arr) / sizeof(arr[0]);

    cout << "Given array is \n";
    printArray(arr, arr_size);

   /// mergeSort(arr, 0, arr_size - 1);
   //quicksort(arr,0,5);

for(int i=1;i<arr_size;i++){
        for(int j=0;j<arr_size-1;j++){

            if(arr[j]>arr[j+1]){
                swap(arr[j],arr[j+1]);
            }
        }
    }

    cout << "\nSorted array is \n";
    printArray(arr, arr_size);

    return 0;
}










//for(int i=1,j;i<5;i++){
//        int tmp=arr[i];
//        for ( j = i; j > 0 && tmp < arr [j-1]; j--){
//            arr [j] = arr [j-1];
//        }
//        arr[j]=tmp;
//    }












