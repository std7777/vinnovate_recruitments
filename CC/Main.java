import java.util.Scanner;

public class Main {

    // Quick Sort
    static void sort(int[] a) {
        quickSort(a, 0, a.length - 1);
    }

    static void quickSort(int[] a, int low, int high) {
        if (low < high) {
            int p = partition(a, low, high);
            quickSort(a, low, p - 1);
            quickSort(a, p + 1, high);
        }
    }

    static int partition(int[] a, int low, int high) {
        int pivot = a[high];
        int i = low - 1;

        for (int j = low; j < high; j++) {
            if (a[j] <= pivot) {
                i++;
                int temp = a[i];
                a[i] = a[j];
                a[j] = temp;
            }
        }

        int temp = a[i + 1];
        a[i + 1] = a[high];
        a[high] = temp;

        return i + 1;
    }

    // Find longest subarray with difference exactly 1
    static int[] subArray(int[] a) {
        int maxLen = 1, currLen = 1;
        int start = 0, tempStart = 0;

        for (int i = 0; i < a.length - 1; i++) {
            if (a[i + 1] - a[i] == 1) {
                currLen++;
            } else {
                if (currLen > maxLen) {
                    maxLen = currLen;
                    start = tempStart;
                }
                currLen = 1;
                tempStart = i + 1;
            }
        }

        // check last subarray
        if (currLen > maxLen) {
            maxLen = currLen;
            start = tempStart;
        }

        return new int[]{start, maxLen};
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int[] a = new int[n];

        for (int i = 0; i < n; i++) {
            a[i] = sc.nextInt();
        }

        sort(a);                      // Quick Sort
        int[] result = subArray(a);   // find subarray

        for (int i = result[0]; i < result[0] + result[1]; i++) {
            System.out.print(a[i] + " ");
        }

        sc.close();
    }
}
