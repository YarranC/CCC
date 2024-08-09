#include <iostream>
#include <string>
using namespace std;

bool check(string numStr, bool change) {
    int len = numStr.length();

    if (len < 19) {
        long long num = stol(numStr);
        if (num > 9 and !change) {
            std::cout << num << std::endl;
        }
        else {
            change = false;
        }
        if (num == 11) {
            return true;
        }
        else if (num > 11) {
            long long ud = num % 10;
            long long t = num / 10;
            return check(to_string(t - ud), false);
        }
        else {
            return false;
        }
    }
    else {
        cout << numStr << endl;

        while (numStr.length() > 18) {
            long long num;
            int l;
            num = stol(numStr.substr(len - 18, 18));
            numStr = numStr.substr(0, len - 18);

            l = to_string(num).length();
            if (l < 18) {
                if (l <= 2) {
                    num += 1000000000000000000;
                    for (int i = numStr.length() - 1; i >= 0; i--) {
                        if (numStr[i] == '0') {
                            numStr[i] = '9';
                        }
                        else {
                            if (i == 0 and int(numStr[i]) == 49) {
                                numStr = numStr.substr(1, numStr.length() - 1);
                                break;
                            }
                            else
                            {
                                numStr[i] = char(int(numStr[i]) - 1);
                                break;
                            }
                        }
                    }
                }
                else {
                    for (int i = 0; i < 18 - l; i++) {
                        numStr += '0';
                    }
                }
            }

            while (num > 9) {
                long long ud = num % 10;
                long long t = num / 10;
                if (t - ud < 0) {
                    break;
                }
                cout << numStr << t - ud << endl;

                num = t - ud;
            }

            if (num != 0) {
                numStr = numStr + to_string(num);
                change = true;
            }
            else {
                change = false;
            }

            len = numStr.length();
        }

        return check(numStr, change);
    }
}

int main() {
    int cnt;
    std::cin >> cnt;
    for (int i = 0; i < cnt; ++i) {
        string num;
        std::cin >> num;

        if (check(num, false)) {
            std::cout << "The number " << num << " is divisible by 11." << std::endl;
        }
        else {
            std::cout << "The number " << num << " is not divisible by 11." << std::endl;
        }
        if (i < cnt - 1) {
            std::cout << std::endl;
        }
    }
    return 0;
}