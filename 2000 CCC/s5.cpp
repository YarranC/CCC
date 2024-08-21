#include <iostream>
#include <iomanip>
#include <vector>
#include <cmath>
#include <algorithm>

using namespace std;

struct Sheep {
    double x;
    double y;

    // Define the equality operator for Sheep
    bool operator==(const Sheep& other) const {
        return x == other.x && y == other.y;
    }
};

// Comparator function to sort sheep based on their x-coordinate
bool compareSheep(const Sheep& a, const Sheep& b) {
    return a.x < b.x;
}

int main() {
    int n;
    cin >> n;

    vector<Sheep> sheeps(n);
    vector<Sheep> eaten;

    for (int i = 0; i < n; ++i) {
        cin >> sheeps[i].x >> sheeps[i].y;
    }

    // Sort the sheeps based on their x-coordinate
    sort(sheeps.begin(), sheeps.end(), compareSheep);

    for (const auto& s : sheeps) {
        double d = pow(s.y, 2);
        Sheep e = s;
        for (const auto& t : sheeps) {
            double dd = pow(t.x - s.x, 2) + pow(t.y, 2);
            if (dd < d) {
                d = dd;
                e = t;
            }
        }
        if (find(eaten.begin(), eaten.end(), e) == eaten.end()) {
            eaten.push_back(e);
        }
    }

    for (const auto& s : eaten) {
        cout << "The sheep at (" << fixed << setprecision(2) << s.x << ", " << s.y << ") might be eaten." << endl;
    }

    return 0;
}