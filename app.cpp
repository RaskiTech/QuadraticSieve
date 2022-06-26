#include <iostream>
#include <vector>
#include <chrono>
#include <glm/glm.hpp>
#include <numeric>
#include <unordered_set>
#include <glm/gtc/constants.hpp>
#include <glm/gtc/integer.hpp>

using namespace glm;
#define size_t uint64_t


const int primes[] = {
    2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,181,191,193,197,199,211,223,227,229,
    233,239,241,251,257,263,269,271,277,281,283,293,307,311,313,317,331,337,347,349,353,359,367,373,379,383,389,397,401,409,419,421,431,433,439,443,449,457,461,463,467,479,487,
    491,499,503,509,521,523,541,547,557,563,569,571,577,587,593,599,601,607,613,617,619,631,641,643,647,653,659,661,673,677,683,691,701,709,719,727,733,739,743,751,757,761,769,
    773,787,797,809,811,821,823,827,829,839,853,857,859,863,877,881,883,887,907,911,919,929,937,941,947,953,967,971,977,983,991,997,1009,1013,1019,1021,1031,1033,1039,1049,1051,
    1061,1063,1069,1087,1091,1093,1097,1103,1109,1117,1123,1129,1151,1153,1163,1171,1181,1187,1193,1201,1213,1217,1223,1229,1231,1237,1249,1259,1277,1279,1283,1289,1291,1297,
    1301,1303,1307,1319,1321,1327,1361,1367,1373,1381,1399,1409,1423,1427,1429,1433,1439,1447,1451,1453,1459,1471,1481,1483,1487,1489,1493,1499,1511,1523,1531,1543,1549,1553,
    1559,1567,1571,1579,1583,1597,1601,1607,1609,1613,1619,1621,1627,1637,1657,1663,1667,1669,1693,1697,1699,1709,1721,1723,1733,1741,1747,1753,1759,1777,1783,1787,1789,1801,
    1811,1823,1831,1847,1861,1867,1871,1873,1877,1879,1889,1901,1907,1913,1931,1933,1949,1951,1973,1979,1987,1993,1997,1999,2003,2011,2017,2027,2029,2039,2053,2063,2069,2081,
    2083,2087,2089,2099,2111,2113,2129,2131,2137,2141,2143,2153,2161,2179,2203,2207,2213,2221,2237,2239,2243,2251,2267,2269,2273,2281,2287,2293,2297,2309,2311,2333,2339,2341,
    2347,2351,2357,2371,2377,2381,2383,2389,2393,2399,2411,2417,2423,2437,2441,2447,2459,2467,2473,2477,2503,2521,2531,2539,2543,2549,2551,2557,2579,2591,2593,2609,2617,2621,
    2633,2647,2657,2659,2663,2671,2677,2683,2687,2689,2693,2699,2707,2711,2713,2719,2729,2731,2741,2749,2753,2767,2777,2789,2791,2797,2801,2803,2819,2833,2837,2843,2851,2857,
    2861,2879,2887,2897,2903,2909,2917,2927,2939,2953,2957,2963,2969,2971,2999,3001,3011,3019,3023,3037,3041,3049,3061,3067,3079,3083,3089,3109,3119,3121,3137,3163,3167,3169,
    3181,3187,3191,3203,3209,3217,3221,3229,3251,3253,3257,3259,3271,3299,3301,3307,3313,3319,3323,3329,3331,3343,3347,3359,3361,3371,3373,3389,3391,3407,3413,3433,3449,3457,
    3461,3463,3467,3469,3491,3499,3511,3517,3527,3529,3533,3539,3541,3547,3557,3559,3571,3581,3583,3593,3607,3613,3617,3623,3631,3637,3643,3659,3671,3673,3677,3691,3697,3701,
    3709,3719,3727,3733,3739,3761,3767,3769,3779,3793,3797,3803,3821,3823,3833,3847,3851,3853,3863,3877,3881,3889,3907,3911,3917,3919,3923,3929,3931,3943,3947,3967,3989,4001,
    4003,4007,4013,4019,4021,4027,4049,4051,4057,4073,4079,4091,4093,4099,4111,4127,4129,4133,4139,4153,4157,4159,4177,4201,4211,4217,4219,4229,4231,4241,4243,4253,4259,4261,
    4271,4273,4283,4289,4297,4327,4337,4339,4349,4357,4363,4373,4391,4397,4409,4421,4423,4441,4447,4451,4457,4463,4481,4483,4493,4507,4513,4517,4519,4523,4547,4549,4561,4567,
    4583,4591,4597,4603,4621,4637,4639,4643,4649,4651,4657,4663,4673,4679,4691,4703,4721,4723,4729,4733,4751,4759,4783,4787,4789,4793,4799,4801,4813,4817,4831,4861,4871,4877,
    4889,4903,4909,4919,4931,4933,4937,4943,4951,4957,4967,4969,4973,4987,4993,4999,5003,5009,5011,5021,5023,5039,5051,5059,5077,5081,5087,5099,5101,5107,5113,5119,5147,5153,
    5167,5171,5179,5189,5197,5209,5227,5231,5233,5237,5261,5273,5279,5281,5297,5303,5309,5323,5333,5347,5351,5381,5387,5393,5399,5407,5413,5417,5419,5431,5437,5441,5443,5449,
    5471,5477,5479,5483,5501,5503,5507,5519,5521,5527,5531,5557,5563,5569,5573,5581,5591,5623,5639,5641,5647,5651,5653,5657,5659,5669,5683,5689,5693,5701,5711,5717,5737,5741,
    5743,5749,5779,5783,5791,5801,5807,5813,5821,5827,5839,5843,5849,5851,5857,5861,5867,5869,5879,5881,5897,5903,5923,5927,5939,5953,5981,5987,6007,6011,6029,6037,6043,6047,
    6053,6067,6073,6079,6089,6091,6101,6113,6121,6131,6133,6143,6151,6163,6173,6197,6199,6203,6211,6217,6221,6229,6247,6257,6263,6269,6271,6277,6287,6299,6301,6311,6317,6323,
    6329,6337,6343,6353,6359,6361,6367,6373,6379,6389,6397,6421,6427,6449,6451,6469,6473,6481,6491,6521,6529,6547,6551,6553,6563,6569,6571,6577,6581,6599,6607,6619,6637,6653,
    6659,6661,6673,6679,6689,6691,6701,6703,6709,6719,6733,6737,6761,6763,6779,6781,6791,6793,6803,6823,6827,6829,6833,6841,6857,6863,6869,6871,6883,6899,6907,6911,6917,6947,
    6949,6959,6961,6967,6971,6977,6983,6991,6997,7001,7013,7019,7027,7039,7043,7057,7069,7079,7103,7109,7121,7127,7129,7151,7159,7177,7187,7193,7207,7211,7213,7219,7229,7237,
    7243,7247,7253,7283,7297,7307,7309,7321,7331,7333,7349,7351,7369,7393,7411,7417,7433,7451,7457,7459,7477,7481,7487,7489,7499,7507,7517,7523,7529,7537,7541,7547,7549,7559,
    7561,7573,7577,7583,7589,7591,7603,7607,7621,7639,7643,7649,7669,7673,7681,7687,7691,7699,7703,7717,7723,7727,7741,7753,7757,7759,7789,7793,7817,7823,7829,7841,7853,7867,
    7873,7877,7879,7883,7901,7907,7919
};

///////////////////////////////////////////////////
/////////////// Utility functions /////////////////
///////////////////////////////////////////////////

size_t gcd(size_t a, size_t b) {
   if (b == 0)
   return a;
   return gcd(b, a % b);
}

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


class SolveSystemOfLinearEquations {
    // Answerarray should already be initialized with the chosen variables
    static uint8_t InsertAnswerIntoArray(const int& rowIndex, const std::vector<std::vector<uint8_t>>& mat, const std::vector<std::vector<int>>& onesByColumn, std::vector<uint8_t>& answerArray) {
        if (answerArray[rowIndex] != (uint8_t)-1)
            return answerArray[rowIndex];

        // Find the first 1 in that row
        int first1Column = 0;
        for (int i = 0; i < mat[rowIndex].size(); i++)
            if (mat[rowIndex][i] == 1) {
                first1Column = i;
                break;
            }

        // Calculate do we need this
        
        answerArray[rowIndex] = 0;

        for (int i = 0; i < onesByColumn[first1Column].size(); i++) {
            answerArray[rowIndex] = (answerArray[rowIndex] + InsertAnswerIntoArray(onesByColumn[first1Column][i], mat, onesByColumn, answerArray)) % 2;
        }

        return answerArray[rowIndex];
    }

public:
    // CheckValidAnswer return: Continue searching?
    template<typename T>
    static void FindKernels(std::vector<std::vector<uint8_t>>& mat, T CheckValidAnswer) {
        // The layout idea:     Mat          Ans
        //                      0 0 0 0 1    ?
        //                      0 0 0 1 0    ?
        //                      0 0 1 0 1    ?

        //     How many ones?   0 0 0 0 1

        int h = mat.size(); // Height
        int w = mat[0].size(); // Width

        /*
        std::cout << "Before preprocessing:" << std::endl;
        for (int i = 0; i < h; i++) {
            for (int j = 0; j < w; j++)
                std::cout << (int)mat[i][j] << " ";
            std::cout << std::endl;
        }
        */

        std::vector<int> freeVariableIndices = std::vector<int>();

        bool lastColumn = false;
        for (int cIndex = w-1, rIndex = 0; rIndex < h; cIndex--, rIndex++) {
            if (cIndex < 0) {
                // Ran out of columns. Would need more of them, but no can do
                cIndex = 0;
                lastColumn = true;
                if (mat[rIndex][cIndex] == 1)
					freeVariableIndices.push_back(rIndex);
            }

            if (mat[rIndex][cIndex] == 0) {
                // Look down and hopefully find a 1
                for (int c = 0; c < cIndex; c++) {
                    if (mat[rIndex][c] == 1) {
                        for (int i = 0; i < h; i++)
                            std::swap(mat[i][cIndex], mat[i][c]);
                        break;
                    }
                }
                // If we didn't find a 1 in that column
                if (mat[rIndex][cIndex] == 0) {
                    // Continue without incrementing column index
                    if (!lastColumn) {
						cIndex++;
                    }
					freeVariableIndices.push_back(rIndex);
                    //if (freeVariableIndices.size() == 0 || freeVariableIndices[freeVariableIndices.size()-1] != rIndex)
                    continue;
                }
            }
            for (int c = 0; c < cIndex; c++) {
                if (mat[rIndex][c] == 1) {
                    // Add column at index to column c
                    for (int r = 0; r < h; r++)
                        mat[r][c] = (mat[r][cIndex] + mat[r][c]) % 2;
                }
            }
        }

        /*
        std::cout << "After:" << std::endl;
        int fIndex = 0;
        for (int i = 0; i < h; i++) {
            for (int j = 0; j < w; j++)
                std::cout << (int)mat[i][j] << " ";
            if (fIndex < freeVariableIndices.size() && freeVariableIndices[fIndex] == i) {
                fIndex++;
                std::cout << " Free variable";
            }

            std::cout << std::endl;
        }
        */

        // Go through the array and get all the indicies of 1's
        std::vector<std::vector<int>> onesByColumn = std::vector<std::vector<int>>();
        for (int i = 0; i < w; i++) {
            onesByColumn.push_back(std::vector<int>());
            bool seenFirst1 = false;
            for (int j = 0; j < h; j++) {
                if (mat[j][i] == 1) {
                    if (!seenFirst1) {
                        seenFirst1 = true;
                        continue;
                    }
                    onesByColumn[i].push_back(j);
                }
            }
        }

        std::vector<uint8_t> ans = std::vector<uint8_t>(h);

        // We will use binary representation to iterate through each possibility
        size_t maxSelection = pow(2, freeVariableIndices.size());
        size_t lastSelection = maxSelection - 1; // The first is 1, and we want to update every bit
        for (size_t selection = 1; selection < maxSelection; selection++) {
            // Figure out the last bit in selection that has changed
            size_t lastBitChanged = glm::log2(lastSelection ^ selection) + 1;
            lastSelection = selection;

            // Optimization, only recalculate the ones that could be affected by this change
            std::fill(ans.begin(), ans.begin() + freeVariableIndices[lastBitChanged - 1] + 1, (uint8_t)-1);

            // Populate ansArray with the selected variables
            for (int pos = 0; pos < freeVariableIndices.size(); pos++)
                ans[freeVariableIndices[pos]] = (((selection >> pos) & 1) != 0);

            /*
            std::cout << "Printing answer array with automatically set variables:\n";
            for (int i = 0; i < ans.size(); i++)
                std::cout << (int)ans[i] << " ";
            std::cout << std::endl << std::endl;
            //*/

            // Solve this answer
			for (int i = 0; i < freeVariableIndices[lastBitChanged - 1] + 1; i++)
				InsertAnswerIntoArray(i, mat, onesByColumn, ans);

            if (!CheckValidAnswer(ans))
                break;
        }
    }
};

///////////////////////////////////////////////////
///////////////// The algorithm ///////////////////
///////////////////////////////////////////////////

size_t QuadraticSieve(size_t N) {
    size_t Bmax = primes[sizeof(primes)/sizeof(primes[0])-1]; // the highest prime we have stored
    // Some for the fastest value of B
    size_t B = min( (size_t)round(pow(exp(sqrt(log(N)*log(log(N)))), one_over_root_two<double>())), Bmax );
    if (B < 10) {
        B = 11;
    }
    std::cout << "B: " << B << std::endl;

    size_t amountOfPrimesUpToB = FindPositionInPrimes(B);

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

    // We start checking values from the square root. That gives us a higher change that the square is B-smooth
    size_t guess = ceil(sqrt(N));
    size_t amountOfBSmoothNumbers = primesToCheck.size() + 5;

    std::vector<size_t> squaredModNBSmoothNumbers;
    std::vector<std::vector<uint8_t>> factorExponents;
    std::vector<std::vector<uint8_t>> factorExponentsMod2;

    // Repeat until found a solution
    while (true) {
		squaredModNBSmoothNumbers.reserve(amountOfBSmoothNumbers);
		factorExponents.reserve(amountOfBSmoothNumbers);
		factorExponentsMod2.reserve(amountOfBSmoothNumbers);
        
        std::cout << "Moved to finding B-smooth values." << std::endl;

		// Find some amount of numbers whose square mod N is B-smooth
		while (squaredModNBSmoothNumbers.size() < amountOfBSmoothNumbers) {
			std::vector<uint8_t> exponentArray = std::vector<uint8_t>(primesToCheck.size(), 0); // Initialize all the exponent amounts to 0

			// Sieve the number
			size_t remainder = guess * guess % N;
			for (int i = 0; i < primesToCheck.size(); i++) {
				while (remainder % primesToCheck[i] == 0) {
					remainder /= primesToCheck[i];
					exponentArray[i] += 1; // In the end we want all exponents to be even, so we can get away with mod 2

					// Is the sieving complete
					if (remainder == 1) {
                        std::vector<uint8_t> exponentsMod2 = std::vector<uint8_t>(exponentArray.size());
                        for (int j = 0; j < exponentArray.size(); j++)
                            exponentsMod2[j] = exponentArray[j] % 2;

						squaredModNBSmoothNumbers.push_back(guess);
						factorExponents.push_back(exponentArray);
                        factorExponentsMod2.push_back(exponentsMod2);
						break;
					}
				}
			}

			guess++;
		}

        std::cout << "Moved to solving the matrix." << std::endl;

        size_t officalAnswer = 0;
        int callCount = 0;

        auto CheckAns = [&](const std::vector<uint8_t>& ans) {
            size_t leftSide = 1;
            size_t rightSide = 1;
            for (int j = 0; j < ans.size(); j++)
                if (ans[j] == 1) {
                    leftSide *= squaredModNBSmoothNumbers[j];

                    for (int k = 0; k < factorExponents[j].size(); k++)
                        rightSide *= pow((size_t)primes[k], (size_t)factorExponents[j][k]);
                }
            rightSide = (size_t)sqrt(rightSide);

            // Finally calculate the factor
            size_t ansCandidate = gcd(N, leftSide - rightSide);
			callCount++;

            // We don't accept a trivial factor as a result
            if (ansCandidate != 1 && ansCandidate != N) {
                officalAnswer = ansCandidate;
                return false;
            }

            return true;
        };

        SolveSystemOfLinearEquations::FindKernels(factorExponentsMod2, CheckAns);

        std::cout << std::endl << callCount << " calls to answer validation.\n";

        if (officalAnswer != 0)
            return officalAnswer;

        // We didn't find a number. Let's continue.
        amountOfBSmoothNumbers *= 1.3f;

    }

    std::cout << "Error: Did not find the number." << std::endl;
    return -1;
}


int main() {

#if 1
    size_t factor1 = 3000061;
    size_t factor2 = 3000223;
    // 0.006s
#else
    size_t factor1 = 3000061;
    size_t factor2 = 3002113;
#endif

    size_t product = factor1 * factor2;

    std::cout << "Quadratic Sieve cracking a " << (int)std::log10(product)+1 << " digit number: " << product << ". Expected: " << factor1 << " or " << factor2 << "." << std::endl;

    std::chrono::time_point<std::chrono::system_clock> start = std::chrono::system_clock::now();
    size_t ans = QuadraticSieve(factor1 * factor2);
    std::chrono::time_point<std::chrono::system_clock> end = std::chrono::system_clock::now();
    double milliseconds = std::chrono::duration_cast<std::chrono::milliseconds>(end - start).count();
    
    std::cout << "Got " << ans << " in " << milliseconds / 1000 << " seconds." << std::endl;

    if (ans == factor1 || ans == factor2)
        std::cout << "That is CORRECT. Praise the algorithm." << std::endl;
    else
        std::cout << "Wait.. Wut. Something must be broken." << std::endl;
    
    std::string buf;
    std::cin >> buf;

    return 0;
}