#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int t;
    cin >> t;  // Number of test cases

    while (t--) {
        int n;
        cin >> n;  // Length of sequences

        vector<int> seq_x(n);
        vector<int> seq_y(n);

        for (int i = 0; i < n; ++i) {
            cin >> seq_x[i];
        }

        for (int i = 0; i < n; ++i) {
            cin >> seq_y[i];
        }

        int max_dist = 0;

        for (int i = 0; i < n; ++i) {
            int low = 0;
            int high = n - 1;
            int mid;

            while (low <= high) {
                mid = (low + high) / 2;
                if (seq_y[mid] >= seq_x[i]) {
                    low = mid + 1;
                }
                else {
                    high = mid - 1;
                }
            }

            max_dist = max(max_dist, high - i);
        }

        cout << "The maximum distance is " << max_dist << endl;
    }

    return 0;
}