//# solution.
//# n은 최대 20인데, 0부터 20 미만까지의 20개의 수를 순열로 나열하는 것은, 20P20 = 20!이므로 시간 초과다.
//# 관점을 바꿔, 0을 n/2개, 1을 n/2개 가진 수열을 순열로 나열한다면, 0과 1이라는 같은 수를 가지므로 최악의 경우의 경우의 수는 최대 20!/(10!*10!) 이고, 이것은 약 20만 이하다.


#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int main() {
    int n;
    cin >> n;
    vector<vector<int>> a(n, vector<int>(n));
    for (int i=0; i<n; i++) {
        for (int j=0; j<n; j++) {
            cin >> a[i][j];
        }
    }
    vector<int> b(n);
    for (int i=0; i<n/2; i++) {
        b[i] = 1;
    }
    sort(b.begin(), b.end());
    int ans = 2147483647;
    do {
        vector<int> first, second;
        for (int i=0; i<n; i++) {
            if (b[i] == 0) {
                first.push_back(i);
            } else {
                second.push_back(i);
            }
        }
        int one = 0;
        int two = 0;
        for (int i=0; i<n/2; i++) {
            for (int j=0; j<n/2; j++) {
                if (i == j) continue;
                one += a[first[i]][first[j]];
                two += a[second[i]][second[j]];
            }
        }
        int diff = one-two;
        if (diff < 0) diff = -diff;
        if (ans > diff) ans = diff;
    } while(next_permutation(b.begin(), b.end()));
    cout << ans << '\n';
    return 0;
}