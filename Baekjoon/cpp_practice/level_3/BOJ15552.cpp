#include<iostream>
using namespace std;
int T,A,B;
int main() {
	cin.tie(NULL);
	std::ios_base::sync_with_stdio(false);
	//입출력 방식이 느리면 시간초과가 날수 있다. 위 두줄을 입력해 줌으로써 이를 방지할 수 있다.
	cin >> T;
	for (int i = 0; i < T; i++) {
		cin >> A >> B;
		cout << A + B << "\n";
	}
	return 0;
}