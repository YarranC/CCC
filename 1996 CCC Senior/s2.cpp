#include <iostream>
#include <string>
using namespace std;

int main() {
	int cnt;
	cin >> cnt;
	for (int i = 0; i < cnt; ++i) {
		string num, orig_num;
		int l;
		cin >> num;
		orig_num = num;

		while (num.length() > 2) {
			int idx, d, t;
			l = num.length();
			cout << num << endl;
			idx = l - 1;
			d = num[idx];
			idx--;
			t = num[idx];
			if (d > t) {
				t += 10;
				if (num[idx - 1] != '0') {
					num[idx - 1] = char(int(num[idx - 1]) - 1);
				}
				else {
					num[idx - 1] = '9';
					for (int j = idx - 2; j >= 0; j--) {
						if (num[j] == '0') {
							num[j] = '9';
						}
						else {
							num[j] = char(int(num[j]) - 1);
							break;
						}
					}
				}
			}
			t -= d;

			num[idx] = char(t + 48);

			num = num.substr(0, l - 1);
			if (num[0] == '0') {
				num = num.substr(1, l - 1);
			}
		}

		if (num.length() < 2) {
			if (l > 2) {
				cout << num << endl;
			}
			cout << "The number " << orig_num << " is not divisible by 11." << endl;
		}
		else if (num[0] == num[1]) {
			cout << num << endl;
			cout << "The number " << orig_num << " is divisible by 11." << endl;
		}
		else {
			if (num.length() == 2) {
				cout << num << endl;
			}
			cout << "The number " << orig_num << " is not divisible by 11." << endl;
		}
		if (i < cnt - 1) {
			cout << endl;
		}
	}
	return 0;
}