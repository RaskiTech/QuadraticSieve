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

class SolveSystemOfLinearEquations {
    // Some gaussian elimination i think???
    static void Preprocess(std::vector<std::vector<uint8_t>>& mat) {
        int h = mat.size(); // Height
        int w = mat[0].size(); // Width

        // We know we want in the end all of them to be 0, so we don't care about keeping track of the answer
        for (int cIndex = 0, rIndex = 0; cIndex < w; cIndex++, rIndex++) {
            if (rIndex > h - 1) {
                std::cout << "Ran out of rows. Would need more rows." << std::endl;
                break;
            }

            if (mat[rIndex][cIndex] == 0) {
                // Look down and hopefully find a 1
                for (int c = rIndex + 1; c < h; c++) {
                    if (mat[c][cIndex] == 1) {
                        std::swap(mat[rIndex], mat[c]);
                        break;
                    }
                }
                // If we didn't find a 1 in that column
                if (mat[rIndex][cIndex] == 0) {
                    std::cout << "We didn't find a 1.";
                    // Continue without incrementing row index
                    rIndex--;
                    continue;
                }
            }
            for (int c = rIndex + 1; c < h; c++) {
                if (mat[c][rIndex] == 1) {
                    // Add row at index to row c
                    for (int r = 0; r < w; r++)
                        mat[c][r] = (mat[rIndex][r] + mat[c][r]) % 2;
                }
            }
        }
    }

    // Function to handle changing amount of nested iteration
    static void IterateInBruteForce(std::vector<uint8_t>& idxVec, int deepness, int startValue, int maxIterValue, 
        const std::vector<std::vector<uint8_t>>& originalMat, std::vector<std::vector<uint8_t>>& mat, std::vector<uint8_t>& ans, std::vector<uint8_t>& outSolved, int& workRow, const std::vector<uint8_t>& indicies)
    {
        for (idxVec[deepness] = startValue; idxVec[deepness] < maxIterValue; idxVec[deepness]++) {
            if (deepness != 0 && idxVec[deepness] == idxVec[deepness - 1])
                continue;
            if (deepness == idxVec.size() - 1) {
                // This code block will run for every combination of vec, where vec[i-1] < vec[i] < indicies.size()
                // vec will be the 1's to the array indicies


                // Update all the columns
                int next1sIndex = 0;
                for (int i = 0; i < indicies.size(); i++) {
                    int column = indicies[i];

                    // Is this a 1 or a 0 this iteration?
                    if (idxVec[next1sIndex] == i) {
                        next1sIndex++;
                        // It's a 1
                        for (int r = workRow - 1; r > -1; r--) {
                            if (mat[r][column ] == 1)
                                ans[r] = (ans[r] + 1) % 2;
                            mat[r][column] = 0;
                        }
						outSolved[column] = 1;
                    }
                    else {
                        for (int r = workRow - 1; r > -1; r--)
                            mat[r][column] = 0;
                        outSolved[column] = 0;
                    }
                }

                // Solve the next row, unless this is the last
                if (workRow == 0) {
                    for (int i = 0; i < outSolved.size(); i++)
                        std::cout << " " << (int)outSolved[i];
                    std::cout << std::endl;
                }
                else BruteForce(originalMat, mat, ans, outSolved, workRow - 1);

                // Set all back for next time
                for (int i = 0; i < indicies.size(); i++) {
                    int column = indicies[i];

                    for (int r = workRow - 1; r > -1; r--)
                        mat[r][column] = originalMat[r][column];
                }
            }
            else IterateInBruteForce(idxVec, deepness + 1, idxVec[deepness], maxIterValue, originalMat, mat, ans, outSolved, workRow, indicies);
        }
    }

    static void BruteForce(const std::vector<std::vector<uint8_t>>& originalMat, std::vector<std::vector<uint8_t>>& mat, std::vector<uint8_t>& ans, std::vector<uint8_t>& outSolved, int workRow) {
        bool rowEmpty = true;

		// Find the variables to set
		auto indicies = std::vector<uint8_t>();
		for (int c = 0; c < mat[workRow].size(); c++) {
            if (mat[workRow][c] == 1) {
                rowEmpty = false;
				indicies.push_back(c);
            }
		}

		// Because of the mod 2, we can add 2 1s and nothing will change
		for (int amountOf1s = ans[workRow]; amountOf1s <= indicies.size(); amountOf1s += 2) {
            if (amountOf1s == 0) {

                // Update all the columns
                for (int i = 0; i < indicies.size(); i++) {
                    int column = indicies[i];

                    for (int r = workRow - 1; r > -1; r--)
                        mat[r][column] = 0;
                    outSolved[column] = 0;
                }

                if (workRow == 0) {
                    for (int i = 0; i < outSolved.size(); i++)
                        std::cout << " " << (int)outSolved[i];
                    std::cout << std::endl;
                }
                else
					// Solve the next row
					BruteForce(originalMat, mat, ans, outSolved, workRow - 1);

                // Set all back
                for (int i = 0; i < indicies.size(); i++) {
                    int column = indicies[i];

                    for (int r = workRow - 1; r > -1; r--)
                        mat[r][column] = originalMat[r][column];
                    outSolved[column] = (uint8_t)-1;
                }
            }
            else {
				std::vector<uint8_t> vec = std::vector<uint8_t>(amountOf1s);
				IterateInBruteForce(vec, 0, 0, indicies.size(), originalMat, mat, ans, outSolved, workRow, indicies);
            }
		}
    }

public:
    static void Solve(std::vector<std::vector<uint8_t>>& mat) {
        int h = mat.size(); // Height
        int w = mat[0].size(); // Width

        Preprocess(mat);

		std::cout << "\n\n";
		for (int i = 0; i < mat.size(); i++) {
			for (int j = 0; j < mat[0].size(); j++)
				std::cout << (int)mat[i][j];
			std::cout << std::endl;
		}
		std::cout << std::endl;

		std::vector<uint8_t> ans = std::vector<uint8_t>(mat[0].size(), (uint8_t)-1);
		auto referenceMat = mat;

		// Solve the matrix using brute force. Because of the preprocessing, this shouldn't be so bad
		auto tmp = std::vector<uint8_t>(h, 0);
        int workRow = h - 1;
		BruteForce(referenceMat, mat, tmp, ans, workRow);
    }
};

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
    std::vector<std::vector<uint8_t>> factorExponents;
    squaredModNBSmoothNumbers.reserve(amountOfBSmoothNumbers);
    factorExponents.reserve(amountOfBSmoothNumbers);
    while (squaredModNBSmoothNumbers.size() < amountOfBSmoothNumbers) {
        std::vector<uint8_t> exponentArray = std::vector<uint8_t>(primesToCheck.size(), 0); // Initialize all the exponent amounts to 0

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





void Test() {

    // The following is an example. Every column is an exponent vector, and thus every row shows what exponent vectors contribute to that exponent
    // TODO: Flip this algorithm across the y=x axis. Make it take a vector of exponents instead of a vector of exponent contributions
    auto equations = std::vector<std::vector<uint8_t>>();
    equations.push_back(std::vector<uint8_t>{ 1, 0, 1, 1 });
    equations.push_back(std::vector<uint8_t>{ 1, 1, 0, 0 });
    equations.push_back(std::vector<uint8_t>{ 0, 1, 0, 1 });
    equations.push_back(std::vector<uint8_t>{ 0, 1, 0, 1 });
    equations.push_back(std::vector<uint8_t>{ 0, 1, 0, 1 });

    SolveSystemOfLinearEquations::Solve(equations);
}

int main() {
    Test();

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