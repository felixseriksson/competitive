#include <bits/stdc++.h>

using namespace std;

void solve(int n, int k) {
    vector<double> p;
    double pi;
    for (int i = 0; i < n; i++) {
        cin >> pi;
        p.push_back(pi);
    }

    sort(p.begin(), p.end(), greater<double>());

    double dp[n + 1][2 * n + 1];
    memset(dp, 0, sizeof(double)*(n + 1)*(2 * n + 1));
    for (int j = 0; j < n + 1; j++) {
        dp[0][j] = 1;
    }

    for (int i = 1; i < n + 1; i++) {
        dp[i][n - i] = 1;
        dp[i][n + i] = p.at(i - 1)*dp[i - 1][n + i - 1];
        for (int j = n - i + 1; j < n + i; j++) {
            dp[i][j] = p.at(i - 1)*dp[i - 1][j - 1] + (1.0f - p.at(i - 1))* dp[i - 1][j + 1];
        }
    }

    double maxx = 0;
    for (int i = 0; i < n+1; i++) {
        maxx = max(maxx, dp[i][n + k]);
    }
    cout << maxx << endl;
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    int n, k;
    cin >> n >> k;
    
    solve(n, k);
}