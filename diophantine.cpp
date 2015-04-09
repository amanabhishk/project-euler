#include <stdio.h>
using namespace std;

int coins[] = {1,2,5,10,20,50,100,200};
int res[201];

void ways(int m, int sum)
{
	res[0] = 1;
	for (int i=0; i<m; i++)
		for (int j=coins[i]; j<=sum; j++)
			res[j] += res[j-coins[i]];
}

int main()
{
	ways (8,200);
	printf ("%d\n", res[200]);
}