#include <iostream>
#include <vector>
#include <iomanip> // for std::fixed and std::setprecision

int main() {
    std::vector<double> x(100);
    std::vector<double> y(100);
    std::vector<bool> out(100, false);  // list of "out" sheep

    int n;
    std::cin >> n;
    for (int i = 0; i < n; i++) {
        std::cin >> x[i] >> y[i];
    }

    for (int i = 0; i < n; i++) {
        double left = 0, right = 1000;
        for (int j = 0; j < n; j++) {
            if (!out[i] && !out[j] && i != j) {
                double xm = (x[i] + x[j]) / 2;
                double ym = (y[i] + y[j]) / 2;
                double s = (x[i] - x[j]) / (y[j] - y[i]);
                if (s == 0) {
                    if (y[i] < y[j])
                        out[j] = true;
                    else
                        out[i] = true;
                }
                else {
                    double p = -ym / s + xm;
                    if (x[j] < x[i])
                        left = std::max(p, left);
                    else
                        right = std::min(p, right);
                }
            }
        }
        if (left >= right)
            out[i] = true;
    }

    for (int j = 0; j < n; j++) {
        if (!out[j]) {
            std::cout << "The sheep at (" << std::fixed << std::setprecision(2) << x[j] << ", " << y[j] << ") might be eaten." << std::endl;
        }
    }

    return 0;
}