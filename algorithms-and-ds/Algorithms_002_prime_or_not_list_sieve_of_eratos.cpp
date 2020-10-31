/* 
 * algorithms-002-prime-or-not-list-sieve-of-eratos.cpp
 * ds-algo-interview-cookbook
 *
 * Print all prime numbers till number N efficiently using 
 * the Sieve of Eratosthenes method.
 * 
 * Created by Ravi Vats on 08/03/20.
*/

#include <cstring>
#include <iostream>
using namespace std;

// Time Complexity = O(n * log(log(n)))
// Space Complexity = O(n)
void printPrimeNumbers(int N) {
    // boolean array holding whether numbers 0 to N are prime or not
    bool isPrime[N + 1];
    // intially setting every number as a prime
    memset(isPrime, true, sizeof(isPrime));

    // 0 and 1 are not primes
    isPrime[0] = isPrime[1] = false;

    for (int p = 2; p * p <= N; p++)
        if (isPrime[p] == true)
            for (int i = p * p; i <= N; i += p)
                isPrime[i] = false;

    cout << "Prime numbers between 0 to " << N << " are: " << endl;
    for (int p = 0; p <= N; p++)
        if (isPrime[p] == true)
            cout << " " << p;
    cout << endl;
}

int main() {
    printPrimeNumbers(100);
    return 0;
}