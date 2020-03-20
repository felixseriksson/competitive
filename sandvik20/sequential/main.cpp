#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
#define rep(i,a,b) for (ll i = a; i<ll(b); i++)
//compile with g++/cc -g -Wall -Wconversion -fsanitize=address,
//undefined <filename.cpp>
int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    cout << setprecision(15);

    // ll N, P;
    // cin >> N >> P;
    // vector<ll> T;
    // ll temp;
    // for (int i = 0; i < N; i++){
    //     cin >> temp;
    //     T.push_back(temp);
    // }
    // int inputare;
    // cin >> inputare;
    // ll summa = accumulate(T.begin(), T.end(), 0);
    // ll max = *max_element(T.begin(), T.end());
    // cout << summa+(max*(P-1)) << endl;
    ll N, P, inputarea, temp, maxi, summa;
    cin >> N >> P;
    maxi = 0;
    summa = 0;
    for (ll i = 0; i < N; i++){
        cin >> temp;
        summa += temp;
        maxi = max(temp, maxi);
    }
    summa += maxi*(P-1);
    cout << summa << endl;

}
