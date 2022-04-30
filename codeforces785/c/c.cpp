#include <bits/stdc++.h>
using namespace std;

const int N = 40001, M = 500;
long long MOD = 1000000007;
long long dp[N][M];

int reverse(int n) {
    int r = 0;
    while (n > 0) {
        r = r * 10 + n % 10;
        n /= 10;
    }
    return r;
}

bool palindrome(int n) {
    return (reverse(n) == n);
}

int main() {
    vector<int> palindromes;
    for (int i = 0; i <= N; i++) {
        if (palindrome(i)) {
            palindromes.push_back(i);
        }
    }

    for (int j = 1; j < M; j++) {
        dp[0][j] = 1;
    }

    for (int i = 1; i < N; i++) {
        dp[i][0] = 0;
        for (int j = 1; j < M; j++) {
            if (palindromes[j] <= i) {
                dp[i][j] = (dp[i][j-1] + dp[i - palindromes[j]][j]) % MOD;
            } else {
                dp[i][j] = dp[i][j-1];
            }
        }
    }

    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int cases;
    cin >> cases;
    while (cases--) {
        int n;
        cin >> n;
        cout << dp[n][M-1] << "\n";
    }
}