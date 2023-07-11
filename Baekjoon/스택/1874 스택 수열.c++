#include <iostream>
#include <stack>
#include <vector>

using namespace std;

int main() {
    vector<int> input = {8, 4, 3, 6, 8, 7, 5, 2, 1};

    stack<int> array;
    vector<char> result;

    int current = 1;
    int index = 0;

    while (index < input[0]) {
        if (!array.empty() && array.top() == input[index]) {
            array.pop();
            result.push_back('-');
            index++;
        } else {
            array.push(current);
            result.push_back('+');
            current++;
        }
    }

    if (!array.empty()) {
        cout << "NO\n";
    } else {
        for (char symbol : result) {
            cout << symbol << ' ';
        }
        cout << '\n';
    }

    return 0;
}
