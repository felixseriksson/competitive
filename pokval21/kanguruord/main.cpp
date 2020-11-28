#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
#define rep(i,a,b) for (ll i = a; i<ll(b); i++)
//compile with g++/cc -g -Wall -Wconversion -fsanitize=address,
//undefined <filename.cpp>
int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    cout << setprecision(10);

    string ordet;
    int times;
    int ctr = 0;
    cin >> ordet;
    int ordlen = ordet.length();
    cin >> times;
    for (int i = 0; i < times; i++) {
        string potential;
        cin >> potential;
        int potlength = potential.length();
        vector<int> forwardindices;
        vector<int> reverseindices;
        int forward = 0;
        int reverse = 1;
        // cout << "am now before for loop" << endl;
        // cout << "ordlen is " << ordlen << endl;
        for (int j = 0; j < ordlen; j++) {
            // cout << "just stepped into for loop" << endl;
            // cout << "forward is " << forward << endl;
            if (forward < potential.length()) {
                // cout << "entered forward check" << endl;
                if (ordet[j] == potential[forward]) {
                    // cout << ordet[j] << " with index " << j << " same as forward index " << forward << endl;
                    forwardindices.push_back(j);
                    forward++;
                }
            }
            // cout << "reverse is " << reverse << endl;
            if (reverse < potential.length() + 1) {
                // cout << "entered reverse check" << endl;
                if (ordet[ordlen - j - 1] == potential[potential.length() - reverse]) {
                    // cout << ordet[ordlen - j] << " with index " << ordlen - j << " same as reverse index " << reverse << endl;
                    reverseindices.push_back(ordlen - j - 1);
                    reverse++;
                }
            }
        }
        std::reverse(reverseindices.begin(), reverseindices.end());
        if (forward == potential.length() && reverse == potential.length() + 1 && (forwardindices != reverseindices)) {
            // cout << potential << " är en stökig substring" << endl;
            // for (int k=0; k < forwardindices.size(); k++) {
            //     std::cout << forwardindices.at(k) << ' ';
            // }
            // cout << endl;
            // for (int k=0; k < reverseindices.size(); k++) {
            //     std::cout << reverseindices.at(k) << ' ';
            // }
            // cout << endl;
            ctr++;
        }
    }
    cout << ctr << "\n";

    return 0;

}
