#include<iostream>
using namespace std;
int T,A,B;
int main() {
	cin.tie(NULL);
	std::ios_base::sync_with_stdio(false);
	//����� ����� ������ �ð��ʰ��� ���� �ִ�. �� ������ �Է��� �����ν� �̸� ������ �� �ִ�.
	cin >> T;
	for (int i = 0; i < T; i++) {
		cin >> A >> B;
		cout << A + B << "\n";
	}
	return 0;
}