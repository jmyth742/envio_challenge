#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

/*
Author: Jonathan Smyth
Date : 29.04.2021
Descr: Sorting the array in ascending order, using bucket sort.
*/
 

#define EMPTY 0


void bin_sort(int* number, int count) {
    
    int temp;
   // Loop to get the elements stored in array
 
   // Logic of selection sort algorithm
   for(int i=0;i<count;i++){
      for(int j=i+1;j<count;j++){
         if(number[i]>=number[j]){
            temp=number[i];
            number[i]=number[j];
            number[j]=temp;
         }
      }
   }


 
/* Driver program to test above function */
int main()
{
    int bin[30] = {0};
    // int foo [30] = { 2, 2, 1, 0, 1, 0, 1, 1, 0, 2, 2, 1, 1, 1, 2, 0, 0, 1, 1, 0,
    //                 1, 0, 1, 2, 0, 0, 0, 1, 1, 2 };
    int foo [30] = { 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 2, 0, 0, 1, 1, 0,
                    0, 1, 1, 2, 2, 2, 0, 1, 1, 2 };
    int count = sizeof(foo) / sizeof(foo[0]);

    bin_sort(foo,count);
 
    cout << "Sorted array is \n";
    for (int i = 0; i < count; i++)
        cout << foo[i] << " ";
    return 0;
}