/* 
 * algorithms-003-prime-or-not-list-optimized-sieve-of-eratos.cpp
 * ds-algo-interview-cookbook
 *
 * Print all prime numbers till number N efficiently using 
 * the Optimized version of Sieve of Eratosthenes method which
 * improves time complexity from O(n * log(log(n))) to O(n).
 * 
 * Created by Ravi Vats on 08/03/20.
*/

#include <cstring>
#include <iostream>
#include <vector>
using namespace std;
const long long MAX_SIZE = 100001;

// Time Complexity = O(n)
// Space Complexity = O(n)
void printPrimeNumbers(int N) {
    vector<bool> isPrime(N+1, true);
    // prime[] : stores list of all prime numbers till N
    vector<long long int> prime;
    // SPF[] that store smallest prime factor of number
    // For example : smallest prime factor of '8' and '16' is '2' 
    // so we put SPF[8] = 2 , SPF[16] = 2
    vector<long long int> SPF(N+1);
    
    isPrime[0] = isPrime[1] = false;

    for (int i = 2; i <= N; i++) {
        if (isPrime[i] == true) {
            prime.push_back(i);
            SPF[i] = i;  // any prime number is its own smallest prime factor
        }

        // Remove all multiples of  i*prime[j] which are
        // not prime by making isPrime[i*prime[j]] = false
        // and put smallest prime factor of i*Prime[j] as prime[j]
        // For example :let  i = 5 , j = 0 , prime[j] = 2, i*prime[j] = 10
        // so smallest prime factor of '10' is '2' that is prime[j]
        // so mark 10 as a non-prime and set SPF[i*prime[j]] = prime[j]
        for (long long int j = 0; j < prime.size() && i * prime[j] <= N && prime[j] <= SPF[i]; j++) {
            isPrime[i * prime[j]] = false;
            SPF[i * prime[j]] = prime[j];
        }   
    }

    cout << "Prime numbers between 0 to " << N << " are: " << endl;
    for (auto it = prime.begin(); it < prime.end(); it++) {
        cout << " " << *it;
    }
    cout << endl;
}


int main() {
    printPrimeNumbers(97);
    return 0;
}