#include<iostream>
using namespace std;
int M, H, C, duration;
int main() {
	cin >> H >> M;
	cin >> duration;
	C = 60 * H + M + duration;
	if (C >= 60*24) {
		C = C-60*24;
		cout << C / 60 << " " << C % 60;
	}
	else
		cout << C / 60 << " " << C % 60;

	return 0;
}