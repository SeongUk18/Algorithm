#include<iostream>
using namespace std;
int N;
int main() {
	cin.tie(NULL);
	std::ios_base::sync_with_stdio(false);
	cin >> N;
	int i = 0;
	int end = N;
	while (true) {
		int A, B, C, D;
		A = N / 10;
		B = N % 10;
		C = (A + B)%10;
		D = 10 * B + C;
		i++;
		if (end == D)
			break;
		else
			N = D;
	}
	cout << i;
	return 0;
}