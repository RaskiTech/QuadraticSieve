#include <iostream>
#include <vector>
#include <chrono>
#include <glm/glm.hpp>
#include <glm/gtc/constants.hpp>
#include <glm/gtc/integer.hpp>

using namespace glm;
#define size_t uint64_t

const int primes[] = {
    2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 41, 43
};

///////////////////////////////////////////////////
/////////////// Utility functions /////////////////
///////////////////////////////////////////////////

// Binary search
int FindPositionInPrimes(size_t number) {
    size_t start = 0;
    size_t end = sizeof(primes)/sizeof(primes[0])-1;

    while (start <= end) {
        size_t mid = (start + end) / 2;
        if (primes[mid] < number)
            start = mid + 1;
        else
            end = mid - 1;
    }

    return start + 1;
}
// Does x^y % p. We are dealing with numbers that would be too large without this function.
int APowerBModuloC(long long a, unsigned int b, int c) {
    int res = 1;
    a = a % c;
    if (a == 0) return 0;
    while (b > 0) {
        if (b & 1)
            res = (res*a) % c;
        b = b>>1;
        a = (a*a) % c;
    }
    return res;
}

///////////////////////////////////////////////////
///////////////// The algorithm ///////////////////
///////////////////////////////////////////////////

size_t QuadraticSieve(size_t N) {
    size_t Bmax = primes[sizeof(primes)/sizeof(primes[0])-1]; // the highest prime we have stored
    // Choose a value for B. This is an approximation for a good value
    size_t B = min( (size_t)round(pow(exp(sqrt(log(N)*log(log(N)))), one_over_root_two<size_t>())), Bmax );
    if (B < 10) {
        B = 11;
        std::cout << "We need to rethink B. Let's set it to " << B << std::endl;
    }

    size_t amountOfPrimesUpToB = FindPositionInPrimes(B);

    // We start checking values from the square root. That gives us a higher change that the square is B-smooth
    size_t guess = ceil(sqrt(N));
    size_t amountOfBSmoothNumbers = 10; // TODO: Change hard coded value: "There is no formula to calculate this, but usually you should continue till you find atleast 5 more smooth numbers than the number of primes in the Factor Base."

    // FOR SIEVING, but don't need to recompute each time
    // We don't need to check through every single one of the primes.
    // We can use something called Euler's criterion to check only some of them.
    std::vector<size_t> primesToCheck;
    primesToCheck.reserve(amountOfPrimesUpToB); // Some of this will likely be unused, but we don't care about space
    primesToCheck.push_back(2); // Trick doesn't work on 2
    for (int i = 1; i < amountOfPrimesUpToB; i++) {
        bool passTest = APowerBModuloC(N, (primes[i]-1)/2, primes[i]) == 1; // a^b % c
        if (passTest)
            primesToCheck.push_back(primes[i]);
    }


    // Find some amount of numbers whose square mod N is B-smooth
    std::vector<size_t> squaredModNBSmoothNumbers;
    std::vector<std::vector<size_t>> factorExponents;
    squaredModNBSmoothNumbers.reserve(amountOfBSmoothNumbers);
    factorExponents.reserve(amountOfBSmoothNumbers);
    while (squaredModNBSmoothNumbers.size() < amountOfBSmoothNumbers) {
        std::vector<size_t> exponentArray = std::vector<size_t>(primesToCheck.size(), 0); // Initialize all the exponent amounts to 0

        // Sieve the number
        size_t remainder = guess * guess % N;
        for (int i = 0; i < primesToCheck.size(); i++) {
            while (remainder % primesToCheck[i] == 0) {
                remainder /= primesToCheck[i];
                exponentArray[i] = (exponentArray[i] + 1) % 2; // In the end we want all exponents to be even, so we can get away with mod 2

                // Is the sieving complete
                if (remainder == 1) {
                    squaredModNBSmoothNumbers.push_back(guess);
                    factorExponents.push_back(exponentArray);
                    break;
                }
            }
        }

        guess++;
    }

    // TODO:
    // We have the exponents, find some combination of exponents that gets every exponent even
    // Use those exponents to calculate factors
    // If the factor is not one of the trivial factors (1, N), return it

    return -1;
}

int main() {
    size_t factor1 = 53;
    size_t factor2 = 59;

    std::cout << "Quadratic Sieve cracking " << factor1 * factor2 << ". Expected: " << factor1 << " or " << factor2 << "." << std::endl;

    std::chrono::time_point<std::chrono::system_clock> start = std::chrono::system_clock::now();
    size_t ans = QuadraticSieve(factor1 * factor2);
    std::chrono::time_point<std::chrono::system_clock> end = std::chrono::system_clock::now();
    double milliseconds = std::chrono::duration_cast<std::chrono::milliseconds>(end - start).count();
    
    std::cout << "Got " << ans << " in " << milliseconds / 1000 << " seconds." << std::endl;
    
    std::string buf;
    std::cin >> buf;

    return 0;
}