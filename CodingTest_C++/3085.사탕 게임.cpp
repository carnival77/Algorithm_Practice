#include<vector>
#include<iostream>
#include<algorithm>
#include<string>
using namespace std;

int check(vector<string>& a) {
    int ans = 1;
    int n = a.size();
    for (int i = 0; i < n; i++) {
        int cnt = 1;
        for (int j = 1; j < n; j++) {
            if (a[i][j] == a[i][j - 1]) {
                cnt += 1;
            }
            else {
                cnt = 1;
            }
            if (ans < cnt) ans = cnt;
        }
        cnt = 1;
        for (int j = 1; j < n; j++) {
            if (a[j][i] == a[j - 1][i]) {
                cnt += 1;
            }
            else {
                cnt = 1;
            }
            if (ans < cnt) ans = cnt;
        }
    }

    return ans;
}

int main() {
    int n;
    cin >> n;
    vector<string> a(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }
    int ans = 0;
    for (int x = 0; x < n; x++) {
        for (int y = 0; y < n; y++) {
            if (x + 1 < n) {
                swap(a[x][y], a[x + 1][y]);
                int temp = check(a);
                if (ans < temp) ans = temp;
                swap(a[x][y], a[x + 1][y]);
            }
            if (y + 1 < n) {
                swap(a[x][y], a[x][y + 1]);
                int temp = check(a);
                if (ans < temp) ans = temp;
                swap(a[x][y], a[x][y + 1]);
            }
        }
    }
    cout << ans << '\n';
    return 0;
}