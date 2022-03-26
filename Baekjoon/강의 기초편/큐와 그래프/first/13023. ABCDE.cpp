////풀이
////1. A->B , C->D : 간선그래프로 연결 여부 확인
////2. B->C : 인접행렬로 연결 여부 확인
////3. D->E : 인접그래프로 연결 여부 확인 

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
bool a[2000][2000]; // 인접행렬
vector<int> g[2000]; // 인접그래프
vector<pair<int, int>> edges; // 간선그래프 
int main() {
    int n, m;
    cin >> n >> m;
    for (int i = 0; i < m; i++) {
        int from, to;
        cin >> from >> to;
        edges.push_back({ from, to });
        edges.push_back({ to, from });
        a[from][to] = a[to][from] = true;
        g[from].push_back(to);
        g[to].push_back(from);
    }
    // (A,B)와 (C,D)가 서로 다른 간선이 되도록 2중 for문으로 탐색
    m *= 2;
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < m; j++) {
            // A -> B
            int A = edges[i].first;
            int B = edges[i].second;
            // C -> D
            int C = edges[j].first;
            int D = edges[j].second;
            // A,B,C,D,E 가 서로 다른 점이도록
            if (A == B || A == C || A == D || B == C || B == D || C == D) {
                continue;
            }
            // B -> C
            if (!a[B][C]) {
                continue;
            }
            // D -> E
            for (int E : g[D]) {
                if (A == E || B == E || C == E || D == E) {
                    continue;
                }
                cout << 1 << '\n';
                return 0;
            }
        }
    }
    cout << 0 << '\n';
    return 0;
}
