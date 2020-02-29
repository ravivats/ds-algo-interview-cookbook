/* 
 * spiral-order-matrix-traversal.cpp
 * ds-algo-interview-cookbook
 *
 * Print the elements of the matrix while traversing it in a spiral manner
 * Created by Ravi Vats on 20/01/20.
*/  

#include <iostream>
#include <cstdio>
#include <vector>
using namespace std;

void horizontalTraversal(const vector<vector<int>>&, int, int, int, int, int, int);
void verticalTraversal(const vector<vector<int>>&, int, int, int, int, int, int);

void spiralOrder(const vector<vector<int> > &A) {
    int R = 0, C = 0;
    R = int(A.size());
    if (R != 0) {
        C = int(A[0].size());
    }
    auto currI = 0, currJ = 0;
    cout << "A["<< currI << "][" << currJ << "]: " << A[currI][currJ] << endl;
    horizontalTraversal(A, currI, currJ, C , R, 1, 1);
}

int main() {
    std::vector<std::vector<int> > input { { 1, 2, 3, 4, 5 }, { 16, 17, 18, 19, 6 },{ 15, 24, 25, 20, 7 },
        { 14, 23, 22, 21, 8}, { 13, 12, 11, 10, 9},};
    spiralOrder(input);
    return 0;
}

void horizontalTraversal(const vector<vector<int> > &A, int i, int j, int horizontalLimit, int verticalLimit, int nextStep, int updateWhenNegative) {
    // base case
    if (horizontalLimit == 1) {
        return;
    }
    for (auto index=0; index < horizontalLimit - 1; index++) {
        j += nextStep;
        cout << "A["<< i << "][" << j << "]: " << A[i][j] << endl;
    }
    if (updateWhenNegative < 0) {
        verticalLimit -= 1;
    }
    verticalTraversal(A, i, j, horizontalLimit, verticalLimit, nextStep, updateWhenNegative - 1);
}

void verticalTraversal(const vector<vector<int> > &A, int i, int j, int horizontalLimit, int verticalLimit, int nextStep, int updateWhenNegative) {
    // base case
    if (verticalLimit == 1) {
        return;
    }
    for (auto index=0; index < verticalLimit - 1; index++) {
        i += nextStep;
        cout << "A["<< i << "][" << j << "]: " << A[i][j] << endl;
    }
    if (updateWhenNegative < 0) {
        horizontalLimit -= 1;
    }
    horizontalTraversal(A, i, j, horizontalLimit, verticalLimit, nextStep * -1, updateWhenNegative -1);
}
