#include <iostream>
#include <vector>
#include <string>
#include <unordered_set>

using namespace std;

int m, n;
vector<string> A;
vector<string> B;
vector<int> seq;
unordered_set<string> memo;

// Check if current sequences match
bool check(const vector<string>& set1, const vector<string>& set2) {
    string seq1 = "";
    string seq2 = "";
    for (int i = 0; i < seq.size(); ++i) {
        seq1 += set1[seq[i] - 1];
        seq2 += set2[seq[i] - 1];
    }
    return seq1 == seq2;
}

// Check if one sequence is a prefix of the other
bool isPrefix(const string& seq1, const string& seq2) {
    return seq1.size() <= seq2.size() ? seq2.substr(0, seq1.size()) == seq1 : seq1.substr(0, seq2.size()) == seq2;
}

bool build(int k) {
    if (k >= m) {
        return check(A, B);
    }

    string currentSeq = "";
    for (int i : seq) {
        currentSeq += to_string(i);
    }

    if (memo.find(currentSeq) != memo.end()) {
        return false;
    }
    memo.insert(currentSeq);

    string currentA = "", currentB = "";
    for (int i = 0; i < seq.size(); ++i) {
        currentA += A[seq[i] - 1];
        currentB += B[seq[i] - 1];
    }

    // Early termination if lengths differ
    if (currentA.size() != currentB.size() && !isPrefix(currentA, currentB)) {
        return false;
    }

    for (int i = 0; i < n; ++i) {
        seq.push_back(i + 1);

        if (check(A, B)) {
            return true;
        }

        if (build(k + 1)) {
            return true;
        }

        seq.pop_back();
    }

    return false;
}

int main() {
    cin >> m >> n;

    A.resize(n);
    B.resize(n);

    for (int i = 0; i < n; ++i) {
        cin >> A[i];
    }

    for (int i = 0; i < n; ++i) {
        cin >> B[i];
    }

    if (build(0)) {
        cout << seq.size() << endl;
        for (int i = 0; i < seq.size(); ++i) {
            cout << seq[i] << endl;
        }
    }
    else {
        cout << "No solution." << endl;
    }

    return 0;
}