//Ǯ��
//1. �ൿ 3����(x+1,x-1,2x) ��� 0 or 1�ʾ� �ҿ�ǹǷ� BFS �� Ǯ�� ����
//2. ��ġ = ����. �̵� ������ ����� �� = ��ġ ���� ����.
//3. �ð����⵵ : ���� 1��(10��) + ���� 2��(20��) = 30��. O(40��). 2�� ���� Ǯ�� ����.
//4. ������ ���� : 0~10��. �׷��Ƿ� 2*X �ϴ� �����̵��� ����ϸ� �ִ� Ž�� ������ 20��
//5. �����̵��� ��� 0�ʰ� �ɸ���. ��, �� �ൿ���� 0 or 1�ʰ� �ҿ�ǹǷ�
//		ť�� now_q, next_q �� ����. �����̵��� ������ �ൿ���� next_q�� ����Ѵ�.
//		ť�� �� ������ ���Ǹ�, �ش� ���� ��Ҹ� �� ������ ���� ���� ť�� ���ŵȴ�.

#include <iostream>
#include <queue>
#include <deque>
using namespace std;
bool c[1000000];
int d[1000000];
int MAX = 1000000;
int main() {
    int n, m;
    cin >> n >> m;
    c[n] = true;
    d[n] = 0;
    queue<int> q;
    queue<int> next_queue;
    q.push(n);
    while (!q.empty()) {
        int now = q.front();
        q.pop();
        if (now * 2 < MAX) {
            if (c[now * 2] == false) {
                q.push(now * 2);
                c[now * 2] = true;
                d[now * 2] = d[now];
            }
        }
        if (now - 1 >= 0) {
            if (c[now - 1] == false) {
                next_queue.push(now - 1);
                c[now - 1] = true;
                d[now - 1] = d[now] + 1;
            }
        }
        if (now + 1 < MAX) {
            if (c[now + 1] == false) {
                next_queue.push(now + 1);
                c[now + 1] = true;
                d[now + 1] = d[now] + 1;
            }
        }
        if (q.empty()) {
            q = next_queue;
            next_queue = queue<int>();
        }
    }
    cout << d[m] << '\n';
    return 0;
}