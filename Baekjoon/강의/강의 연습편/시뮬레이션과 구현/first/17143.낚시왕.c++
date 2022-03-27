#include <iostream>
#include <algorithm>
#include <vector>
#include <tuple>
using namespace std;
struct Fish {
    int size = 0;
    int speed = 0;
    int direction = 0;
};
// up, down, right, left
int dx[] = {-1,1,0,0};
int dy[] = {0,0,1,-1};
int n, m;
Fish fish[100][100];
Fish nfish[100][100];
tuple<int,int,int> get_next(int x, int y, int speed, int direction) {
    for (int k=0; k<speed; k++) {
        if (direction == 0) { // up
            if (x == 0) {
                x = 1;
                direction = 1;
            } else {
                x -= 1;
            }
        } else if (direction == 1) { // down
            if (x == n-1) {
                x = n-2;
                direction = 0;
            } else {
                x += 1;
            }
        } else if (direction == 2) { // right
            if (y == m-1) {
                y = m-2;
                direction = 3;
            } else {
                y += 1;
            }
        } else if (direction == 3) { // left
            if (y == 0) {
                y = 1;
                direction = 2;
            } else {
                y -= 1;
            }
        }
    }
    return make_tuple(x, y, direction);
}
int main() {
    int mm;
    cin >> n >> m >> mm;
    while (mm--) {
        int x, y, s, d, z;
        cin >> x >> y >> s >> d >> z;
        x -= 1;
        y -= 1;
        d -= 1;
        fish[x][y] = Fish({z, s, d});
    }
    long long ans = 0;
    for (int j=0; j<m; j++) {
        for (int i=0; i<n; i++) {
            if (fish[i][j].size > 0) {
                ans += fish[i][j].size;
                fish[i][j].size = 0;
                break;
            }
        }
        for (int l1=0; l1<n; l1++) {
            for (int l2=0; l2<m; l2++) {
                if (fish[l1][l2].size == 0) continue;
                auto f = fish[l1][l2];
                int x, y, direction;
                tie(x, y, direction) = get_next(l1, l2, f.speed, f.direction);
                if (nfish[x][y].size == 0 || nfish[x][y].size < f.size) {
                    nfish[x][y] = Fish({f.size, f.speed, direction});
                }
            }
        }
        for (int l1=0; l1<n; l1++) {
            for (int l2=0; l2<m; l2++) {
                fish[l1][l2] = nfish[l1][l2];
                nfish[l1][l2].size = 0;
            }
        }
    }
    cout << ans << '\n';
    return 0;
}