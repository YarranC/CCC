#include <iostream>
#include <string>

// Function to subtract two large numbers represented as strings
std::string subtract(const std::string& a, const std::string& b) {
    // Assumes a >= b
    int n = a.length();
    int m = b.length();
    std::string result = "";
    int carry = 0;

    for (int i = 0; i < n; ++i) {
        int digitA = a[n - 1 - i] - '0';
        int digitB = (i < m) ? b[m - 1 - i] - '0' : 0;
        int digit = digitA - digitB - carry;

        if (digit < 0) {
            digit += 10;
            carry = 1;
        }
        else {
            carry = 0;
        }

        result = char(digit + '0') + result;
    }

    // Remove leading zeros
    size_t startpos = result.find_first_not_of('0');
    if (std::string::npos != startpos) {
        result = result.substr(startpos);
    }
    else {
        result = "0";
    }

    return result;
}

// Function to check if a >= b for large numbers represented as strings
bool isGreaterOrEqual(const std::string& a, const std::string& b) {
    if (a.length() > b.length()) return true;
    if (a.length() < b.length()) return false;
    return a >= b;
}

int main() {
    int n;
    std::cin >> n;
    std::cin.ignore(); // To ignore the newline character after the integer input

    for (int i = 0; i < n; ++i) {
        std::string dividend, divisor;
        std::getline(std::cin, dividend);
        std::getline(std::cin, divisor);

        if (dividend.length() < divisor.length() || !isGreaterOrEqual(dividend, divisor)) {
            std::cout << 0 << std::endl;
            std::cout << dividend << std::endl;
        }
        else {
            int length = divisor.length();

            std::string quotient = "";
            std::string remainder = dividend.substr(0, length);
            for (int j = 0; j <= dividend.length() - length; ++j) {
                int cnt = 0;
                while (isGreaterOrEqual(remainder, divisor)) {
                    remainder = subtract(remainder, divisor);
                    cnt++;
                }
                quotient += std::to_string(cnt);
                if (length + j < dividend.length()) {
                    remainder += dividend[length + j];
                    // Remove leading zeros from remainder
                    size_t startpos = remainder.find_first_not_of('0');
                    if (std::string::npos != startpos) {
                        remainder = remainder.substr(startpos);
                    }
                    else {
                        remainder = "0";
                    }
                }
            }

            // Remove leading zeros from quotient
            size_t startpos = quotient.find_first_not_of('0');
            if (std::string::npos != startpos) {
                quotient = quotient.substr(startpos);
            }
            else {
                quotient = "0";
            }

            std::cout << quotient << std::endl;
            std::cout << remainder << std::endl;
        }

        if (i < n - 1) {
            std::cout << std::endl;
        }
    }

    return 0;