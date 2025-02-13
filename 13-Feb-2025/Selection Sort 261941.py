# Problem: Selection Sort - https://practice.geeksforgeeks.org/problems/selection-sort/1

class Solution: 
    def selectionSort(self, arr):
        #code here
        for i in range(len(arr)):
            min=i
            for j in range(i,len(arr)):
                if(arr[min]>arr[j]):
                    min=j
            arr[i],arr[min]=arr[min],arr[i]
        return arr