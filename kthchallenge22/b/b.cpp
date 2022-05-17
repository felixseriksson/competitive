#include <bits/stdc++.h>
#include <iostream>
#include <string>
#include <queue>
using namespace std;

int MOD = 1000000007;

int nk(int n, int k) {
    if ((k == 1) || (n == k)) {
        return (n*(n+1)/2) % MOD;
    }
    else {
        return nk(n-1, k-1) + nk(n-1, k);
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int q;
    cin >> q;
    int n, k, x;
    while(q--) {
        cin >> n >> k >> x;
        if (nk(n, k) == x) {
            cout << "Correct" << endl;
        }
        else {
            cout << "Incorrect" << endl;
        }
    }
}