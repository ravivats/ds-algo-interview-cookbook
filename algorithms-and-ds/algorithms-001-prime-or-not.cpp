/* 
 * algorithms-001-prime-or-not.cpp
 * ds-algo-interview-cookbook
 *
 * Print if the given number is prime or not.
 * 
 * Created by Ravi Vats on 08/03/20.
*/

#include <iostream>
using namespace std;

// Using Optimized Introduction and School Method for Primality Test
// Time Complexity = O(n^0.5)
// Space Complexity = O(1)
bool isPrime(int n) {
    if (n <= 1) return false;
    if (n <= 3) return true;
    if (n % 2 == 0 || n % 3 == 0) return false;

    for (int i = 5; i * i < n; i += 6)
        if (n % i == 0 || n % (i + 2) == 0)
            return false;

    return true;
}

int main() {
    int list[4] = {13, 59, 67, 69};
    // to set the flag to print boolean values in cout as true/false instead of 0/1
    cout << boolalpha;
    for (int i = 0; i < sizeof(list) / sizeof(list[0]); i++) {
        cout << list[i] << " is a prime number: " << isPrime(list[i]) << endl;
    }
    return 0;
}