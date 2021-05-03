#include <algorithm>
#include <iostream>
#include <vector>
#include <random>

using namespace std;

/*
Author: Jonathan Smyth
Date : 29.04.2021
Descr: Sorting the array in ascending order, using bucket sort.

Just a simple file, nothing more. compiled with g++.

todo - add header file, cmake list maybe etc. 

debug is set as default, will generate random array and then sort it. 
The none debug is some what redundant, ideally maybe make it cmdline args for main.

funtion is simple sort, returns void and need pointer to the array. as it is pointer, 
the array var is changed after function call.


built with - g++ -o main arraySort.cpp

*/
 


#define DEBUG 1

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
}


 
int main()
{

   if(DEBUG){
      int test[30];
      std::random_device rd;
      std::mt19937 gen(rd());
      std::uniform_int_distribution<> dis(0, 2);
      cout << "Random generated array, unsorted. " << endl;
      for(int i =0;i<30;i++){
         test[i] = dis(gen);
         cout << test[i] << " ";
      }
      cout<<endl;
      int count = sizeof(test) / sizeof(test[0]);
      bin_sort(test,count);
      cout << "TEST array is \n";
      for (int i = 0; i < count; i++)
         cout << test[i] << " ";
      cout<<endl;
   }
   // original envio array
    int foo [30] = { 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 2, 0, 0, 1, 1, 0,
                    0, 1, 1, 2, 2, 2, 0, 1, 1, 2 };
    int count = sizeof(foo) / sizeof(foo[0]);

    bin_sort(foo,count);
   
    cout << "Sorted array is \n";
    for (int i = 0; i < count; i++)
        cout << foo[i] << " ";
    return 0;
}